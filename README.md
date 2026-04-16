# python-ai-assisted-dev-sample

Minimal Python 3.11 application for parsing inventory transactions and producing a text report

## Structure

```text
.
|-- .devcontainer/
|   `-- devcontainer.json
|-- .github/
|   |-- agents/
|   |   `-- test-expert/              # Test automation agent
|   |-- instructions/
|   |   |-- app.instructions.md       # TDD requirements for app/
|   |   `-- tests.instructions.md     # Author header requirements
|   `-- workflows/
|       `-- ci.yml
|-- app/
|   |-- __init__.py
|   |-- __main__.py
|   `-- inventory.py
|-- tests/
|   |-- test_cli.py
|   `-- test_inventory.py
`-- pyproject.toml
```

## Execute the application

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

## Test Expert Agent

The **Test Expert** agent generates comprehensive test suites achieving 100% line and branch coverage using modern Python testing patterns.

### Quick Start
```bash
# Check current coverage
pytest --cov=app --cov-branch --cov-report=term-missing

# Invoke Test Expert Agent
@test-expert Generate tests for uncovered code in app/inventory.py
```

### Features
- 🎯 **Coverage Analysis** - Identifies uncovered lines and branches
- 🧪 **Test Generation** - Creates comprehensive test suites
- 🏗️ **Best Practices** - Follows pytest conventions and TDD workflow
- ✅ **Compliance** - Enforces author headers and 100% coverage

### Documentation
- [Agent Overview](.github/agents/test-expert/README.md)
- [Complete Specification](.github/agents/test-expert/agent.md)
- [Quick Reference](.github/agents/test-expert/QUICK_REFERENCE.md)
- [Implementation Guide](.github/agents/test-expert/IMPLEMENTATION_GUIDE.md)
- [Technical Configuration](.github/agents/test-expert/CONFIG.md)