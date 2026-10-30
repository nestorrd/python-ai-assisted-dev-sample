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
|   |   |-- inventory-mcp-demo.agent.md
|   |   |-- frontend-expert.agent.md
|   |   `-- test-expert.agent.md
|   |-- instructions/
|   |   |-- app.instructions.md
|   |   `-- tests.instructions.md
|   |-- prompts/
|   |   `-- implement-feature.prompt.md
|   |-- skills/
|   |   `-- tdd-python/
|   |       |-- SKILL.md
|   |       `-- references/
|   |           `-- INVENTORY_TEST_CASES.md
|   `-- workflows/
|       |-- ci.yml
|       `-- copilot-setup-steps.yml
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
  - `test-expert` helps improve test coverage; `frontend-expert` advises on Python UI architecture; `inventory-mcp-demo` shows read-only tool scoping and an optional MCP configuration template.
- `.github/prompts/implement-feature.prompt.md`
  - Reusable feature-implementation prompt with `${input:...}` parameters and links to relevant source and tests.
- `.github/skills/tdd-python/references/INVENTORY_TEST_CASES.md`
  - On-demand reference mapping the sample's current behavior to its tests.
- `.github/workflows/copilot-setup-steps.yml`
  - Optional environment setup for GitHub Copilot coding agent tasks.

Prompt files remain supported by GitHub Copilot, but are in public preview and
availability varies by IDE and version. They are invoked for a specific interaction;
repository instructions apply automatically within their supported scope. In a
supported IDE, try `/implement-feature` and provide a feature and area when prompted.

## Walkthrough: issue to pull request

This sample can demonstrate a supervised GitHub Copilot coding-agent task:

1. **Check availability.** The repository must have GitHub Copilot coding agent enabled for the account and repository, with the required organization policies and GitHub Actions access. Availability and controls depend on the Copilot plan and organization settings.
2. **Create a focused issue.** For example: “Add a transaction report option.” Include the desired behavior, acceptance criteria, and likely files such as `app/__main__.py` and `tests/test_cli.py`.
3. **Assign the issue to Copilot.** On GitHub, use **Assign to Copilot**. The coding agent works asynchronously and opens a draft pull request; review its changes and ask for revisions before marking it ready.
4. **Review CI.** Copilot-created pull requests may require approval before GitHub Actions workflows run. After reviewing the changes, click **Approve and run workflows** if that option is shown; then inspect the `.github/workflows/ci.yml` result, which installs the development dependencies and runs `pytest`. Review the diff and checks yourself before merging.

The optional `.github/workflows/copilot-setup-steps.yml` prepares Python 3.11 and
installs this project's development dependencies in the coding-agent environment.
It is a manually runnable setup workflow; it does not replace the pull-request CI.
For a different environment, the coding agent may require different setup steps.

`inventory-mcp-demo.agent.md` is a read/search-only configuration example, not the
agent to assign for code changes. Its optional custom MCP server block is commented
out because this repository does not provide an MCP server. Custom MCP configuration
requires an approved, available server, organization or enterprise policy that permits
the configuration, and any required Agents secrets. The
`mcp-servers` agent-profile property is not used by VS Code or other IDE custom agents;
the example targets GitHub Copilot on GitHub.

For current format and compatibility details, see the [official GitHub Copilot
documentation](#official-github-copilot-documentation).

## Official GitHub Copilot documentation

- [Custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide)
- [Custom agents](https://docs.github.com/en/copilot/concepts/customizations/custom-agents)
- [Custom agent configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Agent skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)
- [Prompt files](https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-files)
- [Configure MCP servers for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers)
- [Configure secrets and variables for Copilot coding agent](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/configure-secrets-and-variables)
- [Improve a project with Copilot coding agent](https://docs.github.com/en/copilot/tutorials/cloud-agent/improve-a-project)
- [Customize the coding-agent environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment)

## CI

- `.github/workflows/ci.yml`
  - Runs automated checks for pushes and pull requests.
  