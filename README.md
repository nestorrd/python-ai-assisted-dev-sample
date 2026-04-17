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
- [Complete Specification](.github/agents/test-expert.agent.md)
- [Quick Reference](.github/agents/test-expert/QUICK_REFERENCE.md)
- [Implementation Guide](.github/agents/test-expert/IMPLEMENTATION_GUIDE.md)
- [Technical Configuration](.github/agents/test-expert/CONFIG.md)

## Frontend Expert Agent

The **Frontend Expert** agent helps design and build modern frontends for Python applications with a pragmatic bias toward Python-first stacks and maintainable UI architecture.

### Quick Start
```text
@frontend-expert Build a polished localhost dashboard for this Python app.
Choose the best frontend architecture, favor a Python-first stack, and make it responsive and accessible.
```

### Recommended Stack Bias
- **FastHTML + HTMX** for server-first dashboards, forms, tables, and workflow screens
- **NiceGUI** for Python-native internal tools and rapid dashboards
- **Reflex** for richer full-stack Python applications
- **FastAPI + React/Vite** only when heavy client-side state is justified

### Features
- Purposeful visual systems with stronger hierarchy and design tokens
- Responsive layouts with explicit loading, empty, error, and success states
- Pragmatic architecture choices that avoid unnecessary SPA complexity
- Clean integration between Python code, templates, APIs, and live updates

### Documentation
- [Agent Overview](.github/agents/frontend-expert/README.md)
- [Complete Specification](.github/agents/frontend-expert.agent.md)
- [Quick Reference](.github/agents/frontend-expert/QUICK_REFERENCE.md)
- [Implementation Guide](.github/agents/frontend-expert/IMPLEMENTATION_GUIDE.md)
- [Technical Configuration](.github/agents/frontend-expert/CONFIG.md)

## Feature Prompt

Use the workspace prompt below when you want Copilot to implement a feature while following this repository's development rules.

### Quick Start
```text
/Implement Feature Add support for a new transaction type and update the CLI output.
```

The prompt automatically directs Copilot to use the repository instructions, TDD workflow, test header rules, README updates, and local ADR process.

### Prompt File
- [.github/prompts/implement-feature.prompt.md](.github/prompts/implement-feature.prompt.md)