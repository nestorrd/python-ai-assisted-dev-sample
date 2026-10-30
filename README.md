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
|   |   `-- test-expert.agent.md
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

## GitHub Copilot customizations

This example demonstrates repository-wide instructions, path-specific instructions,
custom agents, a reusable skill, and a prompt file:

- `.github/copilot-instructions.md`
  - Repository-wide instructions.
- `.github/instructions/app.instructions.md`
  - TDD and coverage guidance for Python application files.
- `.github/instructions/tests.instructions.md`
  - Every new `test_` function in `tests/` must include `# Author:` and `# Date:` headers.
- `.github/skills/tdd-python/SKILL.md`
  - Reusable Red-Green-Refactor workflow.
- `.github/agents/*.agent.md`
  - `test-expert` helps improve test coverage; `frontend-expert` advises on Python UI architecture.
- `.github/prompts/implement-feature.prompt.md`
  - Reusable feature-implementation prompt for supported IDEs.

Prompt files remain supported by GitHub Copilot, but are in public preview and
availability varies by IDE and version. They are invoked for a specific interaction;
repository instructions apply automatically within their supported scope.

For current format and compatibility details, see the [official GitHub Copilot
documentation](#official-github-copilot-documentation).

## Official GitHub Copilot documentation

- [Custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide)
- [Custom agents](https://docs.github.com/en/copilot/concepts/customizations/custom-agents)
- [Custom agent configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Agent skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)
- [Prompt files](https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-files)

## CI

- `.github/workflows/ci.yml`
  - Runs automated checks for pushes and pull requests.
  