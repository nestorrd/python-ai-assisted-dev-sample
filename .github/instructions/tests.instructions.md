<!-- 
Specific Path instructions: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=vscode#creating-path-specific-custom-instructions-1 -->
---
applyTo: "tests/*.py"
---

# Test Authorship Header

Every new test function you create **must** be preceded by a Python comment block that identifies who wrote it and when.

## Format

```python
# Author: <output of `git config user.name`>
# Date: <today's date in YYYY-MM-DD format>
def test_example() -> None:
    ...
```

## Rules

- Place the comment block **immediately above** the `def test_` line, with no blank line between the comment and the function signature.
- For the `# Author:` value, run `git config user.name` and use its output. Never hardcode a name.
- Use today's date in `YYYY-MM-DD` format for the `# Date:` value.
- Apply this header to **every new test function** added to any file under `tests/`.
- Do **not** add or modify headers on existing tests that already have them.
- Do **not** add a header to helper functions, fixtures, or non-test functions (i.e., functions whose name does not start with `test_`).

## Example

```python
# Author: Contoso User  # (example — resolved from git config user.name at generation time)
# Date: 2026-04-16
def test_parse_transactions_returns_empty_list_for_blank_input() -> None:
    assert parse_transactions("") == []
```
