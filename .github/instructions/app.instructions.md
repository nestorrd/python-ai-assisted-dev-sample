<!-- 
Specific Path instructions: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=vscode#creating-path-specific-custom-instructions-1 -->
---
applyTo: "app/*.py"
---

# Development Workflow for App Code

When adding or modifying any code in `app/`, always follow the **TDD (Test-Driven Development)** workflow using the `tdd-python` skill.

## Mandatory TDD Requirement

**No production code may be written without a failing test first.** For every new function, class, or behaviour:

1. Invoke the `tdd-python` skill and follow its Red-Green-Refactor cycle exactly.
2. Write the failing test in `tests/` before touching any file in `app/`.
3. Only write the minimum production code needed to make the test pass.
4. Refactor only when all tests are green.

## Coverage Goals

- Aim for **100% line and branch coverage** of all code in `app/`.
- Every public function and every code branch (including error paths, edge cases, and guard clauses) must have at least one dedicated test.
- After implementing a feature, run `pytest --cov=app --cov-branch --cov-report=term-missing` and address any uncovered lines before considering the work done.

## What Must Be Tested

- **Happy paths**: typical valid inputs producing expected outputs.
- **Error paths**: invalid inputs, missing files, malformed data — anything that raises an exception or returns an error.
- **Edge cases**: empty inputs, zero values, boundary conditions.
- **All branches**: every `if`/`elif`/`else` and `try`/`except` block.

## Workflow Summary

```
1. Read the requirement.
2. List all behaviours as bullet points.
3. For each behaviour → run one full Red-Green-Refactor cycle (tdd-python skill).
4. After all cycles → run pytest --cov=app --cov-branch --cov-report=term-missing.
5. For any uncovered line → add a test and repeat the cycle.
```
