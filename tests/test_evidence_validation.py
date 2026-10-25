"""Accepted-package discovery, malformed-record and missingness regression tests."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from model.packages import load_accepted_packages, accepted_package_hashes, PackageError
from scripts.validate_evidence import validate


def claim(evidence_id="TEST-1"):
    return {"evidence_id":evidence_id,"claim":"A bounded fixture claim.","publisher":"Fixture publisher",
            "url":"https://example.org/source","epistemic_status":"synthetic_test_fixture","source_class":"test_fixture",
            "locator":"Table 1, row 1","publication_date":"2025-01-02","observation_period":"2024-01/2024-12",
            "retrieved_at":"2026-10-25T12:00:00Z",
            "quantities":[{"value":0,"unit":"accepted trials","denominator":10,"population":"specified test population",
                           "period":"2024","measurement_status":"test_fixture"}]}


class EvidenceContracts(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        (self.root/"data").mkdir()
        self.entry={"package_id":"fixture","path":"data/accepted_cards.json","status":"accepted","owner_lane":"test"}
        self.index={"schema_version":"accepted-evidence-packages/1.0","packages":[self.entry]}
        self.data={"evidence":[claim()],"cards":[{"id":"CARD-1","evidence_ids":["TEST-1"]}]}
        self.save()

    def tearDown(self):self.temp.cleanup()

    def save(self):
        (self.root/"data/package_index.json").write_text(json.dumps(self.index))
        (self.root/"data/accepted_cards.json").write_text(json.dumps(self.data))

    def report(self):self.save();return validate(self.root)

    def test_registry_does_not_auto_accept_matching_filenames(self):
        # Invalid draft would poison glob-based discovery. It must not be read.
        (self.root/"data/unreviewed_evidence.json").write_text("not JSON")
        self.assertEqual(self.report()["status"],"pass")
        snapshot=load_accepted_packages(self.root)
        self.assertEqual([p["path"] for p in snapshot["packages"]],["data/accepted_cards.json"])
        self.assertEqual(set(accepted_package_hashes(self.root)["hashes"]),{"data/accepted_cards.json"})
        # Reviewed names need not end in _evidence.json.
        (self.root/"data/new_review.json").write_text(json.dumps({"evidence":[claim("TEST-2")]}))
        self.index["packages"].append({"package_id":"second","path":"data/new_review.json","status":"accepted"})
        self.assertEqual(self.report()["evidence_records"],2)

    def test_malformed_claim_has_no_silent_defaults(self):
        for field in ("claim","publisher","url","epistemic_status","source_class","locator","publication_date","observation_period","retrieved_at"):
            self.data["evidence"]=[claim()];del self.data["evidence"][0][field]
            with self.subTest(field=field):self.assertEqual(self.report()["status"],"failed")
        self.data["evidence"]=["source URL only"]
        self.assertEqual(self.report()["status"],"failed")

    def test_explicit_null_needs_reason_and_is_not_zero(self):
        record=self.data["evidence"][0]
        record["publication_date"]=None
        self.assertEqual(self.report()["status"],"failed")
        record["missingness"]={"publication_date":"Undated artifact; retrieval is not publication."}
        self.assertEqual(self.report()["status"],"pass")
        self.assertEqual(record["quantities"][0]["value"],0)
        record["quantities"][0]={"value":None,"reason":"No measured throughput denominator supplied."}
        report=self.report()
        self.assertEqual(report["status"],"pass")
        self.assertEqual(report["null_quantity_markers"],1)
        self.assertEqual(report["reported_quantities"],0)
        del record["quantities"][0]["reason"]
        self.assertEqual(self.report()["status"],"failed")

    def test_measured_quantity_requires_units_and_context(self):
        for field in ("unit","denominator","population","period","measurement_status"):
            self.data["evidence"]=[claim()]
            record=self.data["evidence"][0]
            del record["quantities"][0][field]
            # Eliminate explicit context inheritance when testing required fields.
            if field=="period":record["observation_period"]=None;record["observation_period_missing_reason"]="Not measured"
            if field=="measurement_status":del record["epistemic_status"]
            with self.subTest(field=field):
                report=self.report()
                # Explicit null period with a source reason is a valid unknown,
                # not fabricated period metadata. Other omissions must fail.
                self.assertEqual(report["status"],"pass" if field=="period" else "failed")
        self.data["evidence"]=[claim()]
        self.data["evidence"][0]["quantities"][0]["value"]="0"
        self.assertEqual(self.report()["status"],"failed")
        self.data["evidence"][0]["quantities"][0]["value"]=True
        self.assertEqual(self.report()["status"],"failed")

    def test_aliases_and_explicit_context_inheritance_are_read_only(self):
        record=self.data["evidence"][0]
        for a,b in (("url","source_url"),("retrieved_at","retrieval_date"),("locator","source_locator"),("publisher","source_publisher"),("claim","precise_claim")):
            record[b]=record.pop(a)
        record["population"]="specified parent population"
        q=record["quantities"][0]
        for field in ("population","period","measurement_status"):del q[field]
        before=copy.deepcopy(self.data)
        report=self.report()
        self.assertEqual(report["status"],"pass")
        self.assertEqual(report["inherited_quantity_context_fields"],3)
        self.assertEqual(self.data,before)
        self.assertEqual(json.loads((self.root/"data/accepted_cards.json").read_text()),before)
        del record["population"];record["geography"]="US"
        self.assertEqual(self.report()["status"],"failed")

    def test_unresolved_analogy_or_conflicting_references_fail(self):
        for key in ("evidence_ids","source_evidence","target_evidence","conflicting_evidence_ids"):
            self.data["cards"]=[{key:["UNACCEPTED-1"]}]
            with self.subTest(key=key):
                report=self.report()
                self.assertEqual(report["status"],"failed")
                self.assertTrue(any("unresolved" in x for x in report["errors"]))

    def test_metrics_cannot_evade_checks_by_changing_container_type(self):
        for bad in ("not an array",{},None):
            self.data["evidence"][0]["metrics"]=bad
            with self.subTest(value=bad):self.assertEqual(self.report()["status"],"failed")

    def test_external_registry_duplicates_and_each_locator_are_validated(self):
        self.data["external_evidence_registry"]=[{"evidence_id":"TEST-1","path":"data/accepted_cards.json"}]
        self.assertEqual(self.report()["status"],"pass")
        self.data["external_evidence_registry"].append({"evidence_id":"TEST-1","path":"data/wrong.json"})
        report=self.report()
        self.assertEqual(report["status"],"failed")
        self.assertTrue(any("duplicate external" in x for x in report["errors"]))
        self.assertTrue(any("locator disagrees" in x for x in report["errors"]))

    def test_registry_rejects_duplicate_missing_or_unsafe_paths(self):
        original=copy.deepcopy(self.index)
        for path in ("../outside.json","data/missing.json","/tmp/other.json",".","./"):
            self.index=copy.deepcopy(original);self.index["packages"][0]["path"]=path
            with self.subTest(path=path):self.assertEqual(self.report()["status"],"failed")
        self.index=copy.deepcopy(original);self.index["packages"].append(copy.deepcopy(self.entry))
        self.assertEqual(self.report()["status"],"failed")
        self.index=copy.deepcopy(original);self.index["packages"][0]["status"]="pending_review"
        self.assertEqual(self.report()["status"],"failed")

    def test_bad_dates_urls_and_nonstandard_numbers_fail(self):
        for field,value in (("publication_date","2025-02-30"),("publication_date","2025-01-02x12:00:00"),("retrieved_at","yesterday"),("url","javascript:alert(1)"),("url","https://["),("url","https://bad host.example/a"),("url","https://example.org:invalid/a")):
            self.data["evidence"]=[claim()];self.data["evidence"][0][field]=value
            with self.subTest(field=field):self.assertEqual(self.report()["status"],"failed")
        self.data["evidence"]=[claim()];self.data["evidence"][0]["quantities"][0]["value"]=float('nan')
        self.assertEqual(self.report()["status"],"failed")

    def test_duplicate_json_keys_fail_before_record_validation(self):
        (self.root/"data/accepted_cards.json").write_text('{"evidence": [{"evidence_id":"TEST-1","claim":"first","claim":"second"}]}')
        report=validate(self.root)
        self.assertEqual(report["status"],"failed")
        self.assertTrue(any("Duplicate JSON object key: claim" in x for x in report["errors"]))


if __name__=="__main__":unittest.main()
