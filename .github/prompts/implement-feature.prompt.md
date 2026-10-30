---
name: "Implement Feature"
description: "Implement a repository feature request while following this project's TDD, test header, README, and ADR requirements. Use when you want Copilot to build or change functionality in this workspace."
argument-hint: "Describe the feature to implement"
agent: "agent"
---
<!-- https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files -->
Implement the following feature request for this repository:

${input:feature:Describe the behavior or feature to implement}

Requested area (optional): ${input:area:Name an app module, CLI area, or leave this blank}

Before editing anything, read and follow these repository rules and assets:
- [Repository instructions](../copilot-instructions.md)
- [App instructions](../instructions/app.instructions.md)
- [Test instructions](../instructions/tests.instructions.md)
- [TDD skill](../skills/tdd-python/SKILL.md)
- [Inventory application code](../../app/inventory.py)
- [Inventory behavior tests](../../tests/test_inventory.py)
- [CLI tests](../../tests/test_cli.py)

Treat the linked code and tests as starting context, not as the complete scope.
Inspect other relevant files when the requested area requires them.

Execution requirements:
- Treat the user's prompt text as the feature request and restate the requested behavior briefly before making changes.
- If code under `app/` must change, follow strict TDD: list behaviors, write a failing test first, implement the minimum production code, then refactor.
- If you add new tests under `tests/`, include the required `# Author:` and `# Date:` header immediately above each new test function.
- Keep changes minimal and focused on the requested behavior. Do not fix unrelated issues unless they block the feature.
- Run the relevant validation commands. If `app/` changes, run `pytest --cov=app --cov-branch --cov-report=term-missing`.
- Update [README.md](../../README.md) if the feature changes behavior, usage, or developer workflow.
- For non-trivial work, create a local ADR in `log/YYYY-MM-DD-<short-slug>.md` using the template from [Repository instructions](../copilot-instructions.md).

Response format:
- Brief plan
- Changes made
- Validation run and outcome
- Any follow-up risks or open questions