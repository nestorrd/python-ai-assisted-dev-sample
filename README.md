# python-ai-assisted-dev-sample

Minimal Python 3.11 application for parsing inventory transactions and producing a text report.

## Project Structure

```text
.
|-- .devcontainer/
|   `-- devcontainer.json
|-- .github/
|   |-- copilot-instructions.md
|   |-- agents/
|   |   |-- frontend-expert.agent.md
|   |   |-- test-expert.agent.md
|   |   |-- frontend-expert/
|   |   |   |-- README.md
|   |   |   |-- QUICK_REFERENCE.md
|   |   |   |-- IMPLEMENTATION_GUIDE.md
|   |   |   `-- CONFIG.md
|   |   `-- test-expert/
|   |       |-- README.md
|   |       |-- QUICK_REFERENCE.md
|   |       |-- IMPLEMENTATION_GUIDE.md
|   |       `-- CONFIG.md
|   |-- instructions/
|   |   |-- app.instructions.md
|   |   `-- tests.instructions.md
|   |-- prompts/
|   |   `-- implement-feature.prompt.md
|   |-- skills/
|   |   `-- tdd-python/
|   |       `-- SKILL.md
|   `-- workflows/
|       `-- ci.yml
|-- app/
|   |-- __init__.py
|   |-- __main__.py
|   `-- inventory.py
|-- tests/
|   |-- test_cli.py
|   `-- test_inventory.py
|-- sample-transactions.txt
|-- pyproject.toml
`-- README.md
```

## Getting Started

```bash
python -m pip install -e .[dev]
python -m app sample-transactions.txt
pytest
```

## Test coverage

```bash
python -m pip install -e .[dev]
pytest
```

## Project Conventions

### Test-Driven Development (TDD)

All code in `app/` must follow the TDD workflow:

1. Write failing tests first
2. Implement minimal code to pass tests
3. Refactor while keeping tests green
4. Target 100% line and branch coverage

See [.github/instructions/app.instructions.md](.github/instructions/app.instructions.md) for details.

### Test Requirements

Every new test function must include author headers:

```python
# Author: <your git username>
# Date: YYYY-MM-DD
def test_example() -> None:
    ...
```

See [.github/instructions/tests.instructions.md](.github/instructions/tests.instructions.md) for details.

## Copilot Instructions Overview

The repository uses layered instructions in `.github`:

- `.github/copilot-instructions.md`
  - Repository-wide rules for workflow, README maintenance, and local ADR logging in `log/`.
- `.github/instructions/app.instructions.md`
  - Any changes in `app/` must follow TDD: fail first, pass, refactor, then verify full coverage.
- `.github/instructions/tests.instructions.md`
  - Every new `test_` function in `tests/` must include `# Author:` and `# Date:` headers.
- `.github/skills/tdd-python/SKILL.md`
  - Detailed Red-Green-Refactor guidance used when implementing Python code.

## Available Agents (Overview)

- `test-expert`
  - Focused on generating and improving tests with strong line and branch coverage.
- `frontend-expert`
  - Focused on building modern, responsive frontends for Python applications.

Agent definitions and references are under `.github/agents/`.

## Prompt

- `.github/prompts/implement-feature.prompt.md`
  - Reusable prompt for implementing features while following repository rules.

## CI

- `.github/workflows/ci.yml`
  - Runs automated checks for pushes and pull requests.