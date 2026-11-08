"""Exact compatible part stock, dated qualification and discrete replacements.

This replaces the generic monthly module balance only in an explicitly typed
contract. It never converts fractional annual spares into a failure schedule.
"""
from dataclasses import asdict, dataclass

from model.engine import catalog
from model.monthly_deployment import TypedComponentSystem, _name

POOLS = ('actuator_h', 'actuator_q', 'embedded_lpddr_boards')


def integer(value, minimum=0, maximum=1_000_000):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError('Bounded whole component quantity or date required')


def vector(value):
    if not isinstance(value, dict) or set(value) != set(POOLS):
        raise ValueError('Component vector must name exactly the three compatible pools')
    for quantity in value.values(): integer(quantity)
    return dict(value)


def zero(): return {kind: 0 for kind in POOLS}


@dataclass(frozen=True)
class ComponentReceipt:
    receipt_id: str
    pool: str
    quantity: int
    announced_month: int = 0
    received_month: int | None = None
    qualified_month: int | None = None

    def __post_init__(self):
        _name(self.receipt_id)
        if self.pool not in POOLS: raise ValueError('Unknown component pool')
        integer(self.quantity, 1); integer(self.announced_month, maximum=120)
        for month in (self.received_month, self.qualified_month):
            if month is not None: integer(month, maximum=120)
        if self.received_month is None and self.qualified_month is not None:
            raise ValueError('Qualification cannot precede physical receipt')
        if self.received_month is not None and self.received_month < self.announced_month:
            raise ValueError('Receipt cannot precede this declared announcement')
        if self.qualified_month is not None and self.qualified_month < self.received_month:
            raise ValueError('Qualification cannot precede physical receipt')


@dataclass(frozen=True)
class Replacement:
    requirement_id: str
    unit_id: str
    due_month: int
    parts: dict

    def __post_init__(self):
        _name(self.requirement_id); _name(self.unit_id); integer(self.due_month, maximum=120)
        object.__setattr__(self, 'parts', vector(self.parts))
        if not sum(self.parts.values()): raise ValueError('A replacement requirement must consume a compatible part')


@dataclass(frozen=True)
class ComponentContract:
    system_id: str
    onboard_configuration: str
    opening_qualified_parts: dict
    receipts: tuple[ComponentReceipt, ...] = ()
    replacements: tuple[Replacement, ...] = ()

    def __post_init__(self):
        if self.system_id not in ('SYN-H', 'SYN-Q'): raise ValueError('Only named synthetic system BOMs are defined')
        if self.onboard_configuration not in ('standard', 'high_memory'): raise ValueError('Unknown onboard component configuration')
        object.__setattr__(self, 'opening_qualified_parts', vector(self.opening_qualified_parts))
        for name, cls, key in [('receipts', ComponentReceipt, 'receipt_id'), ('replacements', Replacement, 'requirement_id')]:
            rows = getattr(self, name)
            if not isinstance(rows, tuple) or any(not isinstance(x, cls) for x in rows): raise ValueError('Explicit immutable component rows required')
            if len({getattr(x, key) for x in rows}) != len(rows): raise ValueError('Duplicate component record identity')
        if len({x.unit_id for x in self.replacements}) != len(self.replacements):
            raise ValueError('This bounded contract permits one replacement requirement per physical unit')


def read_components(value):
    if not isinstance(value, dict): raise ValueError('Explicit component contract required')
    try:
        x = dict(value)
        for name, cls in [('receipts', ComponentReceipt), ('replacements', Replacement)]:
            rows = x.get(name, [])
            if not isinstance(rows, list): raise ValueError('Component records must be arrays')
            x[name] = tuple(cls(**row) for row in rows)
        return ComponentContract(**x)
    except TypeError as exc:
        raise ValueError('Invalid component contract fields') from exc


class ComponentInventory:
    def __init__(self, contract):
        if not isinstance(contract, ComponentContract): raise ValueError('Typed component contract required')
        self.contract = contract
        system = next(x for x in catalog()['systems'] if x['system_id'] == contract.system_id)
        self.bom = {**zero(), system['actuator_pool']: system['actuator_units'],
                    'embedded_lpddr_boards': 2 if contract.onboard_configuration == 'high_memory' else system['board_units']}
        self.available = dict(contract.opening_qualified_parts)
        self.quarantine = {}
        self.completed_replacements = set()
        self.issued_starts = set()
        self.events = []
        self.months = []

    def validate_plan(self, plan):
        if not isinstance(plan.system, TypedComponentSystem) or plan.system.system_id != self.contract.system_id:
            raise ValueError('Component BOM and physical system must match')
        if plan.opening_components or any(plan.qualified_component_receipts):
            raise ValueError('Generic inventory must be inactive in the typed contract')
        if any(x.announced_month >= plan.months for x in self.contract.receipts):
            raise ValueError('Component announcement lies outside the observation window')
        for req in self.contract.replacements:
            if req.due_month >= plan.months: raise ValueError('Replacement requirement lies outside the observation window')
            if any(req.parts[k] > self.bom[k] for k in POOLS):
                raise ValueError('Replacement must fit this physical system and declared configuration')

    def validate_units(self, units, plan):
        names = {x.unit_id for x in units} | {f'start-{s.order_id}-{i+1}' for s in plan.starts for i in range(s.quantity)}
        if any(x.unit_id not in names for x in self.contract.replacements):
            raise ValueError('Replacement names an unknown physical unit')

    def held_by_pool(self):
        held = zero()
        for receipt in self.contract.receipts:
            held[receipt.pool] += self.quarantine.get(receipt.receipt_id, 0)
        return held

    def record(self, month, phase, action, **detail):
        self.events.append({'month': month, 'phase': phase, 'action': action, **detail})

    def open_month(self, month, units):
        self.opening = dict(self.available); self.held_opening = self.held_by_pool()
        self.arrived = zero(); self.released = zero(); self.service_used = zero(); self.start_used = zero(); self.protected = zero()
        for receipt in self.contract.receipts:
            if receipt.announced_month == month:
                self.record(month, 1, 'component_announcement', receipt_id=receipt.receipt_id,
                            pool=receipt.pool, quantity=receipt.quantity, available_inventory_added=0)

    def requirements(self, month, unit):
        return [r for r in self.contract.replacements if r.unit_id == unit.unit_id and r.due_month <= month and
                r.requirement_id not in self.completed_replacements]

    def service_need(self, month, unit):
        return {k: sum(r.parts[k] for r in self.requirements(month, unit)) for k in POOLS}

    def service_reason(self, month, unit):
        needed = self.service_need(month, unit)
        return 'compatible_replacement_parts' if any(needed[k] > self.available[k] for k in POOLS) else ''

    def issue_service(self, month, phase, unit):
        requirements = self.requirements(month, unit); needed = self.service_need(month, unit)
        assert all(needed[k] <= self.available[k] for k in POOLS)
        for k in POOLS:
            self.available[k] -= needed[k]; self.service_used[k] += needed[k]
        for r in requirements: self.completed_replacements.add(r.requirement_id)
        if requirements:
            self.record(month, phase, 'funded_replacement_issue', unit_id=unit.unit_id,
                        requirement_ids=[r.requirement_id for r in requirements], parts=needed,
                        cash_basis='included_once_in_the_existing_paid_support_booking')

    def receive_and_qualify(self, month):
        for receipt in self.contract.receipts:
            if receipt.received_month == month:
                assert receipt.receipt_id not in self.quarantine
                self.quarantine[receipt.receipt_id] = receipt.quantity
                self.arrived[receipt.pool] += receipt.quantity
                self.record(month, 4, 'physical_component_receipt', receipt_id=receipt.receipt_id,
                            pool=receipt.pool, quantity=receipt.quantity, cash_basis='consigned_until_paid_issue')
            if receipt.qualified_month == month:
                quantity = self.quarantine.pop(receipt.receipt_id)
                assert quantity == receipt.quantity
                self.available[receipt.pool] += quantity; self.released[receipt.pool] += quantity
                self.record(month, 4, 'component_qualification_release', receipt_id=receipt.receipt_id,
                            pool=receipt.pool, quantity=quantity)

    def protect_existing(self, month, unsupported):
        self.protected = {k: min(self.available[k], sum(self.service_need(month, u)[k] for u in unsupported)) for k in POOLS}

    def start_reason(self, month, start):
        return 'compatible_manufacturing_parts' if any(self.bom[k] * start.quantity > self.available[k] - self.protected[k] for k in POOLS) else ''

    def issue_start(self, month, start, unit_ids):
        assert start.order_id not in self.issued_starts
        needed = {k: self.bom[k] * start.quantity for k in POOLS}
        assert all(needed[k] <= self.available[k] - self.protected[k] for k in POOLS)
        for k in POOLS:
            self.available[k] -= needed[k]; self.start_used[k] += needed[k]
        self.issued_starts.add(start.order_id)
        self.record(month, 5, 'funded_manufacturing_issue', order_id=start.order_id, unit_ids=list(unit_ids),
                    parts=needed, cash_basis='included_once_in_the_existing_bundled_start_payment')

    def close_month(self, month, units):
        held = self.held_by_pool()
        for kind in POOLS:
            assert self.opening[kind] + self.released[kind] - self.service_used[kind] - self.start_used[kind] == self.available[kind]
            assert self.held_opening[kind] + self.arrived[kind] - self.released[kind] == held[kind]
            assert 0 <= self.protected[kind] <= self.available[kind]
            assert self.available[kind] >= 0 and held[kind] >= 0
        row = {'month': month, 'qualified_opening': self.opening, 'quarantine_opening': self.held_opening,
            'received': dict(self.arrived), 'qualified_release': dict(self.released),
            'service_issued': dict(self.service_used), 'manufacturing_issued': dict(self.start_used),
            'qualified_closing': dict(self.available), 'quarantine_closing': held,
            'protected_for_unsupported_existing': dict(self.protected)}
        self.months.append(row)
        return row

    def result(self, units):
        existing = {u['unit_id']: u for u in units}
        requirements = []
        for req in self.contract.replacements:
            unit = existing.get(req.unit_id)
            requirements.append({**asdict(req), 'completed': req.requirement_id in self.completed_replacements,
                'unit_present_at_close': unit is not None,
                'physical_state_at_close': unit['status'] if unit else 'not_created',
                'scope': 'one declared calendar replacement, conditional on the named unit existing; not a measured failure process'})
        return {'schema_version': 'compatible-component-inventory/0.1',
            'evidence_status': 'synthetic_catalog_BOM_and_declared_receipt_replacement_contract',
            'inputs': asdict(self.contract), 'manufacturing_bom_per_start': dict(self.bom),
            'months': self.months, 'events': self.events, 'replacement_outcomes': requirements,
            'closing_qualified_parts': dict(self.available), 'closing_quarantined_parts': self.held_by_pool(),
            'cash_boundary': 'Components are supplier-funded/consigned until paid issue. Manufacturing/support bundles include consumed materials once; no new bill is added. Opening stocks and supplier financing before issue are outside the window.',
            'maintenance_boundary': 'One explicit replacement requirement per named unit. Its labor is assumed within the existing support booking and allocation. Fractional annual spare rates do not set its date, probability, labor or cost.',
            'annual_boundary': 'Manufacturing compatibility and whole-start BOM are mapped from the synthetic annual catalog. Actual receipt/qualification dates are declared independently; the annual six-cell supply and maintenance trajectories are not imported or jointly executed.'}
