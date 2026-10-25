#!/usr/bin/env python3
"""Re-extract a bounded BLS crosswalk from the unchanged source workbooks, offline.

Standard-library reader for these two static tabular sources, not an Excel engine.
No requirement percentages are multiplied by employment or converted into hours.
"""
import argparse
from collections import Counter
import hashlib
from io import BytesIO
import json
from pathlib import Path
import posixpath
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT/"data/sources/physical_requirements"
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
sys.path.insert(0, str(ROOT))
from model.physical_requirements import TARGETS, METRICS


def xlsx_rows(blob, sheet_name):
    """Yield original row numbers and scalar cell values, preserving strings/dashes."""
    with zipfile.ZipFile(BytesIO(blob)) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            tree = ET.fromstring(z.read("xl/sharedStrings.xml"))
            shared = ["".join(n.itertext()) for n in tree]
        rels = {r.attrib["Id"]: r.attrib["Target"] for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        sheets = ET.fromstring(z.read("xl/workbook.xml")).find("s:sheets", NS)
        matches = [s for s in sheets if s.attrib["name"] == sheet_name]
        if len(matches) != 1:
            raise ValueError(f"Expected exactly one sheet named {sheet_name}")
        target = rels[matches[0].attrib[f"{{{NS['r']}}}id"]]
        path = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/"+target)
        with z.open(path) as stream:
            for _, row in ET.iterparse(stream, events=("end",)):
                if row.tag != f"{{{NS['s']}}}row":
                    continue
                values = []
                for cell in row.findall("s:c", NS):
                    if cell.find("s:f", NS) is not None:
                        raise ValueError("Unexpected source formula; cached values are not calculation proof")
                    letters = "".join(c for c in cell.attrib["r"] if c.isalpha())
                    column = 0
                    for char in letters:
                        column = column*26+ord(char)-64
                    while len(values) < column:
                        values.append(None)
                    kind = cell.attrib.get("t")
                    value = cell.find("s:v", NS)
                    text = value.text if value is not None else None
                    if kind == "s":
                        value = shared[int(text)]
                    elif kind == "inlineStr":
                        value = "".join(cell.find("s:is", NS).itertext())
                    elif text is None:
                        value = None
                    elif kind == "b":
                        value = bool(int(text))
                    elif kind in (None, "n"):
                        number = float(text)
                        value = int(number) if number.is_integer() else number
                    else:
                        value = text
                    values[column-1] = value
                yield int(row.attrib["r"]), values
                row.clear()


def source_inputs(root=ROOT):
    manifest = json.loads((root/"data/sources/physical_requirements/source_manifest.json").read_text())
    sources = {}
    for source in manifest["sources"]:
        blob = (root/source["path"]).read_bytes()
        if hashlib.sha256(blob).hexdigest() != source["sha256"]:
            raise ValueError("Source hash mismatch: "+source["path"])
        sources[Path(source["path"]).name] = blob
    return manifest, sources


def extract(root=ROOT):
    manifest, sources = source_inputs(root)
    ors_blob = sources["ors_2025_complete.xlsx"]
    ors = iter(xlsx_rows(ors_blob, "ORS 2025 dataset"))
    _, header = next(ors)
    required = ["SERIES ID", "SERIES TITLE", "2018 SOC CODE", "OCCUPATION", "REQUIREMENT", "ESTIMATE CODE", "ESTIMATE TEXT", "CATEGORY CODE", "CATEGORY", "ADDITIVE CODE", "ADDITIVE", "DATATYPE CODE", "DATATYPE", "ESTIMATE", "STANDARD ERROR", "DATA FOOTNOTE", "STANDARD ERROR FOOTNOTE", "SERIES FOOTNOTE"]
    if header != required:
        raise ValueError("ORS header changed; review source schema")
    selected, observed_keys, count = [], set(), 0
    for number, values in ors:
        count += 1
        row = dict(zip(header, values))
        key = (row["2018 SOC CODE"], row["ESTIMATE CODE"])
        if key[0] in TARGETS and key[1] in METRICS:
            if key in observed_keys:
                raise ValueError("Duplicate ORS occupation/estimate key")
            if row["OCCUPATION"] != TARGETS[key[0]][0] or row["REQUIREMENT"] != "Physical demands":
                raise ValueError("ORS occupation or requirement identity changed")
            observed_keys.add(key)
            selected.append({"source_row": number, "cells": row})
    footnotes = {str(values[0]): values[1] for number, values in xlsx_rows(ors_blob, "Footnote codes") if number > 1}
    technical = dict((str(number), values) for number, values in xlsx_rows(ors_blob, "File information"))
    with zipfile.ZipFile(BytesIO(sources["oesm25nat.zip"])) as z:
        member = "oesm25nat/national_M2025_dl.xlsx"
        oews_blob = z.read(member)
    oews = iter(xlsx_rows(oews_blob, "national_M2025_dl"))
    _, oews_header = next(oews)
    wanted = {soc[:2]+"-"+soc[2:] for soc in TARGETS} | {"51-2090"}
    oews_selected, national_codes, oews_count = [], [], 0
    for number, values in oews:
        oews_count += 1
        row = dict(zip(oews_header, values))
        if (row["AREA"], row["NAICS"], row["OWN_CODE"]) != ("99", "000000", "1235"):
            continue
        national_codes.append({"code": row["OCC_CODE"], "group": row["O_GROUP"]})
        if row["OCC_CODE"] in wanted:
            oews_selected.append({"source_row": number, "cells": row})
    return {
        "schema_version": "physical-requirements-source-rows/1.0",
        "sources": manifest["sources"], "retrieved_at": manifest["retrieved_at"],
        "ors_sheet": "ORS 2025 dataset", "ors_data_row_count": count,
        "ors_rows": selected,
        "ors_missing_keys": [{"soc": soc, "estimate_code": code} for soc in TARGETS for code in METRICS if (soc,code) not in observed_keys],
        "ors_footnotes": footnotes, "ors_file_information": technical,
        "oews_sheet": "national_M2025_dl", "oews_archive_member": member,
        "oews_workbook_sha256": hashlib.sha256(oews_blob).hexdigest(),
        "oews_data_row_count": oews_count, "oews_rows": oews_selected,
        "oews_exact_code_presence": {soc: sum(x["code"] == soc[:2]+"-"+soc[2:] and x["group"] == "detailed" for x in national_codes) for soc in TARGETS},
        "oews_aggregate_aliases": dict(Counter(x["cells"]["OCC_CODE"] for x in oews_selected)),
        "boundary": "Source rows and category aliases only; no multiplied employment, inferred physical hours or robot-addressable totals.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify the saved extraction without writing")
    args = parser.parse_args()
    output = ROOT/"data/sources/physical_requirements/selected_rows.json"
    result = extract()
    text = json.dumps(result, indent=2, ensure_ascii=False)+"\n"
    if args.check:
        if output.read_text() != text:
            raise SystemExit("Saved extraction differs from the source workbooks")
    else:
        output.write_text(text)
    print(json.dumps({"status": "pass", "ors_rows": len(result["ors_rows"]), "ors_missing": len(result["ors_missing_keys"]), "oews_rows": len(result["oews_rows"]), "exact_code_presence": result["oews_exact_code_presence"]}))


if __name__ == "__main__":
    main()
