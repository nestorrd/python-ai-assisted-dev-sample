# Inventory Sample Behavior and Tests

Use this reference when applying the `tdd-python` workflow to the inventory sample.
It describes existing behavior so new work can preserve current contracts and add
tests at the appropriate layer.

## Behavior map

| Area | Existing behavior | Existing tests |
|------|-------------------|----------------|
| Transaction parsing | Trims whitespace, skips blank lines, parses `item,delta`, and reports malformed rows with line numbers. | `tests/test_inventory.py` |
| Inventory summary | Accumulates deltas by item and rejects a transaction that would make a quantity negative. | `tests/test_inventory.py` |
| Text report | Returns `No inventory data.` for an empty inventory and sorts item names for stable output. | `tests/test_inventory.py` |
| Command-line app | Reads a transaction file, prints the report, and exits with an error for missing files or invalid transactions. | `tests/test_cli.py` |

## TDD guidance

1. Read the relevant function in `app/inventory.py` or entry point in `app/__main__.py`.
2. Add a focused test to the matching module under `tests/` and run it to confirm the expected failure.
3. Implement the smallest change that satisfies the new behavior without breaking the existing cases above.
4. Run `python -m pytest` and, for application changes, `python -m pytest --cov=app --cov-branch --cov-report=term-missing`.

The sample input is in `sample-transactions.txt`. Treat it as demonstration data, not
as a source of additional requirements.
