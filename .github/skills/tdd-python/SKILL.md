---
name: tdd-python
description: 'Test-Driven Development (TDD) workflow for Python. Use when asked to add a new feature, function, class, or module to a Python codebase. Enforces the Red-Green-Refactor cycle: write a failing test first, then write the minimum production code to pass it, then refactor. Activates when the user mentions TDD, test-first, red-green-refactor, write tests before code, or asks to implement new functionality in Python.'
---

# TDD for Python

Enforces the Red-Green-Refactor cycle when adding new code to a Python project. No production code is written until a failing test exists that demands it.

## When to Use This Skill

- User asks to implement a new function, class, or module in Python
- User mentions "TDD", "test-first", or "red-green-refactor"
- User says "write tests before implementation" or "use TDD"
- User opens a GitHub issue and asks to implement it with tests

## Prerequisites

- `pytest` installed (check with `pytest --version`; install via `pip install pytest`)
- An existing test directory (e.g., `tests/`) with at least an `__init__.py` or `conftest.py`, or a flat test file layout

## Step-by-Step Workflows

### Red-Green-Refactor Cycle

Follow these three phases strictly and in order for every new piece of code.

#### Phase 1 — Red: Write a Failing Test

1. Identify the smallest testable behaviour to implement next.  
   Ask: *"What is the simplest input/output or state change this code must produce?"*
2. Create or open the relevant test file (e.g., `tests/test_<module>.py`).
3. Write **one** test that:
   - Has a clear, behaviour-describing name: `test_<action>_<condition>_<expected_result>`
   - Imports the symbol to be created (it does not exist yet — that is intentional)
   - Contains a single `assert` or a focused set of related assertions
   - Uses `pytest.raises` for expected exceptions
4. Run the test suite and confirm it **fails** (red):
   ```bash
   pytest tests/ -v
   ```
   The failure must be because the production code is missing, not because the test itself is broken.
5. Do **not** write any production code yet.

#### Phase 2 — Green: Write the Minimum Production Code

1. Open (or create) the production module referenced by the test.
2. Write the **simplest code** that makes the failing test pass — nothing more.  
   - Hard-coding a return value is acceptable if it makes the test green; a later test will force a real implementation.
   - Do not add logic, parameters, or abstractions not demanded by the current test.
3. Run the suite again and confirm **all tests pass** (green):
   ```bash
   pytest tests/ -v
   ```
4. If other tests break, fix only what was broken by the new code; do not touch unrelated tests.

#### Phase 3 — Refactor: Improve Without Changing Behaviour

1. Review the production code for duplication, poor naming, or structural issues.
2. Review the test code for the same.
3. Apply improvements in small, safe steps.
4. After **every** change, run the full suite to confirm nothing regressed:
   ```bash
   pytest tests/ -v
   ```
5. When all tests are still green and the code is clean, the cycle is complete.

### Starting a New Feature (Multiple Cycles)

Repeat the Red-Green-Refactor cycle for each behaviour:

1. List all expected behaviours as plain-English bullet points before writing any code.
2. Pick the simplest one and run one complete Red-Green-Refactor cycle.
3. Pick the next simplest behaviour and repeat.
4. Continue until all behaviours are implemented and tested.

## Gotchas

- **Never write production code before a failing test exists.** If the test passes on the first run, either the test is wrong or the feature already exists.
- **One failing test at a time.** Resist the urge to write all tests upfront and then implement everything. Keep the cycle tight and fast.
- **Failing for the right reason.** A `ModuleNotFoundError` or `ImportError` is acceptable red — it means the module does not exist yet. A `SyntaxError` in the test itself means fix the test first.
- **Hard-coding is not cheating in the Green phase.** The next test will force generalisation. This is by design (triangulation).
- **Do not refactor in the Red phase.** Refactoring is only safe when all tests are green.
- **Commit after each Green phase** so you always have a known-good checkpoint to return to.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Test passes immediately (stays green) | Check whether the feature already exists, or whether the test actually exercises the right code path |
| `ImportError` on the symbol under test | Expected in Red phase — create the module/function stub to unblock the import, then confirm the test fails for the right reason |
| Many tests fail after a small change | The production code change was too large; revert to last green commit and take a smaller step |
| Refactoring breaks tests | Undo the refactor, run tests, confirm green, then retry the refactor in a smaller increment |
| `pytest` not found | Run `pip install pytest` or `pip install -e .[dev]` if a `pyproject.toml` with a `dev` extra is present |

## References

- [pytest documentation](https://docs.pytest.org/)
- [Test-Driven Development by Example — Kent Beck](https://www.oreilly.com/library/view/test-driven-development/0321146530/)
- [TDD Red-Green-Refactor cheatsheet](https://www.jamesshore.com/v2/blog/2005/red-green-refactor)
