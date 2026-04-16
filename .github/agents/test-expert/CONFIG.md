# Test Expert Agent - Configuration & Metadata

## Agent Profile

**Name:** Test Expert  
**Version:** 1.0  
**Status:** Active  
**Last Updated:** 2026-04-16  
**Author:** GitHub Copilot  
**Category:** Quality Assurance & Testing  

---

## Overview

The Test Expert agent is a specialized testing automation expert that generates comprehensive test suites achieving 100% line and branch coverage. It combines pytest best practices, TDD workflow knowledge, and coverage analysis to create production-grade tests that document behavior and prevent regressions.

---

## Core Capabilities

### 1. Coverage Analysis
- **Analyze code** and identify uncovered lines/branches
- **Generate coverage reports** with detailed gap analysis
- **Map coverage** to specific functions and classes
- **Risk assess** uncovered code areas
- **Track coverage trends** across time

### 2. Test Generation
- **Write failing tests first** following Red-Green-Refactor cycle
- **Create parametrized tests** for comprehensive input coverage
- **Generate fixtures** for shared setup and dependency injection
- **Structure tests** using Arrange-Act-Assert pattern
- **Name tests descriptively** for self-documenting code

### 3. Architecture & Quality
- **Follow pytest conventions** and modern Python patterns
- **Implement proper assertions** with clear error messages
- **Maintain test isolation** (no interdependencies)
- **Apply DRY principles** using fixtures and parametrization
- **Use context managers** for resource management
- **Test all code paths** (happy, error, edge cases)

### 4. Project Compliance
- **Enforce author headers** (Author: and Date: fields)
- **Respect path-specific instructions** (.github/instructions/)
- **Integrate with TDD workflow** (.github/skills/tdd-python/)
- **Achieve 100% coverage targets** (line + branch)
- **Follow naming conventions** and project patterns

---

## Supported Languages

- **Primary:** Python 3.11+
- **Testing Framework:** pytest 8.3+
- **Coverage Tool:** pytest-cov 6.x+

---

## When to Invoke

The Test Expert agent should be invoked when you need to:

- ✅ Create tests for new functions/classes
- ✅ Identify and fix coverage gaps
- ✅ Achieve 100% line and branch coverage
- ✅ Improve existing test architecture
- ✅ Test error paths and edge cases
- ✅ Implement TDD Red phase (failing tests)
- ✅ Create parametrized tests for multiple scenarios
- ✅ Develop comprehensive test suites

---

## How to Invoke

### Via GitHub Copilot Chat

```
@test-expert <description of test needs>
```

**Example:**
```
@test-expert Generate tests covering all uncovered lines in app/inventory.py 
and verify 100% coverage is achieved
```

### Via Chat with Context

Include relevant files or coverage reports:

```
I have app/inventory.py with 87% coverage. Lines 42, 45, 48 are uncovered.
@test-expert Create failing tests first that exercise these lines, 
then verify coverage reaches 100%.
```

### Detailed Request Format

```
Use the Test Expert Agent to:
1. [Analyze/Generate/Review] [specific scope]
2. [Follow TDD / Ensure 100% coverage / Improve architecture]
3. [Specific requirements or constraints]
4. [Verification steps expected]
```

---

## Input Requirements

### Minimal Input
- File path to source code (e.g., `app/inventory.py`)
- Coverage goal (e.g., "100% coverage")

### Recommended Input
- Current coverage report output
- Specific uncovered lines/branches
- Behavioral requirements (what should be tested)
- Edge cases to consider
- Error scenarios to cover

### Optional Input
- Existing test examples to follow pattern
- Performance constraints
- Special testing requirements
- Project-specific conventions

---

## Output Specifications

### 1. Coverage Gap Report
- List of uncovered lines/branches
- Risk assessment (critical vs. minor)
- Code paths not exercised
- Recommendations for testing

### 2. Test Implementation
- Complete test functions with author headers
- Parametrized tests for multiple scenarios
- Shared fixtures in `conftest.py`
- Clear test naming following convention
- Docstrings explaining complex tests

### 3. Verification Commands
- Commands to run new tests
- Coverage check commands
- Proof that coverage reached 100%
- All tests passing confirmation

### 4. Integration Instructions
- Where to place new test files
- Import statements needed
- Configuration changes (if any)
- CI/CD integration notes

---

## Output Format Standards

### Test Function Template
```python
# Author: <git config user.name>
# Date: YYYY-MM-DD
def test_<subject>_<behavior>_<expected_outcome>() -> None:
    # ARRANGE
    ...
    
    # ACT
    ...
    
    # ASSERT
    ...
```

### Fixture Template
```python
@pytest.fixture
def fixture_name():
    """Clear description of what fixture provides."""
    # Setup
    resource = ...
    yield resource
    # Teardown (optional)
```

### Parametrized Test Template
```python
@pytest.mark.parametrize("input,expected", [
    (test_case_1_input, test_case_1_expected),
    (test_case_2_input, test_case_2_expected),
])
def test_<function>_<behavior>(input, expected) -> None:
    assert <function>(input) == expected
```

---

## Project Integration Points

### Related Instructions
- **App Development:** `.github/instructions/app.instructions.md`
  - Enforces TDD workflow
  - Requires 100% coverage
  - All code in `app/` requires tests first

- **Test Requirements:** `.github/instructions/tests.instructions.md`
  - Author header format
  - Date format (YYYY-MM-DD)
  - Applies to all new tests

### Related Skills
- **TDD Python:** `.github/skills/tdd-python/SKILL.md`
  - Red-Green-Refactor cycle
  - Failing test first approach
  - Refactoring guidance

### Related Files
- **Coverage Config:** `pyproject.toml`
  - pytest configuration
  - Coverage thresholds (100%)
  - Test discovery paths

---

## Coverage Standards

### Line Coverage
- **Target:** 100%
- **Meaning:** Every executable line must be run by at least one test
- **Check:** `pytest --cov=app --cov-report=term-missing`

### Branch Coverage
- **Target:** 100%
- **Meaning:** Every `if`/`elif`/`else` and exception branch must be tested
- **Check:** `pytest --cov=app --cov-branch --cov-report=term-missing`

### Test Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| **Happy Path** | Normal usage with valid inputs | Valid transactions, proper format |
| **Error Path** | Invalid inputs, exceptions | Missing fields, type errors |
| **Edge Cases** | Boundary conditions | Empty input, single item, max values |
| **Branch Coverage** | All conditional branches | if/else paths, exception handlers |

---

## Best Practices Enforced

### Test Naming
```python
# ✅ GOOD: test_<subject>_<behavior>_<outcome>
def test_parse_transactions_with_valid_input_returns_list():
    ...

# ❌ AVOID: vague naming
def test_parse():
    ...
```

### Assertion Clarity
```python
# ✅ GOOD: specific, clear assertions
assert len(result) == 3, "Expected 3 items in result"
assert result[0] == ("apples", 3), f"First item should be ('apples', 3), got {result[0]}"

# ❌ AVOID: vague assertions
assert result
```

### Test Isolation
```python
# ✅ GOOD: Each test is independent
def test_feature_a(): ...
def test_feature_b(): ...  # Doesn't depend on test_feature_a

# ❌ AVOID: Tests that depend on execution order
def test_setup():
    global state
    state = ...

def test_uses_state():  # Depends on test_setup running first
    ...
```

### DRY Code
```python
# ✅ GOOD: Shared fixture
@pytest.fixture
def transactions():
    return "apples,3\nbananas,-1\n"

def test_parse(transactions):
    assert len(parse_transactions(transactions)) == 2

# ❌ AVOID: Repeated setup
def test_parse_1():
    text = "apples,3\nbananas,-1\n"
    assert len(parse_transactions(text)) == 2

def test_parse_2():
    text = "apples,3\nbananas,-1\n"
    assert parse_transactions(text)[0] == ("apples", 3)
```

---

## Success Metrics

### Code Quality
- ✅ All tests follow Arrange-Act-Assert pattern
- ✅ Test names are descriptive and meaningful
- ✅ No test interdependencies
- ✅ Fixtures used for shared setup
- ✅ Parametrization for multiple test cases

### Coverage
- ✅ 100% line coverage achieved
- ✅ 100% branch coverage achieved
- ✅ All error paths tested
- ✅ All edge cases covered
- ✅ All public functions have tests

### Compliance
- ✅ Author headers on all new tests
- ✅ Correct date format (YYYY-MM-DD)
- ✅ All tests pass (`pytest` exit code 0)
- ✅ No pre-existing tests modified (unless refactoring)
- ✅ Integration with existing test suite

---

## Common Invocation Scenarios

### Scenario 1: New Module Testing
**Context:** Just created `app/new_module.py`  
**Request:** "Create comprehensive tests for app/new_module.py achieving 100% coverage"  
**Output:** Complete test suite with all functions, edge cases, error paths

### Scenario 2: Coverage Gap Fixing
**Context:** Coverage report shows 87% coverage  
**Request:** "Generate tests for lines [42, 45, 48] in app/inventory.py"  
**Output:** Minimal tests targeting only uncovered lines

### Scenario 3: Test Refactoring
**Context:** Existing tests work but need improvement  
**Request:** "Review tests/test_inventory.py and suggest architectural improvements"  
**Output:** Refactored tests with better organization, fixtures, parametrization

### Scenario 4: Error Path Coverage
**Context:** Need to test exception handling  
**Request:** "Create tests for all error scenarios in app/parser.py"  
**Output:** Tests for each exception, validation check, and error condition

---

## Configuration

### Python Version
- **Minimum:** Python 3.11
- **Tested:** Python 3.11 (see devcontainer)
- **Type Hints:** Full type annotations expected

### Testing Framework
- **Framework:** pytest 8.3+
- **Coverage:** pytest-cov 6.x+
- **Fixtures:** Standard pytest fixtures and conftest.py

### Coverage Thresholds
- **Line Coverage:** ≥ 100% (fail-under=100)
- **Branch Coverage:** ≥ 100% (when running with --cov-branch)
- **Enforcement:** Via pytest addopts in pyproject.toml

### Path-Specific Rules
- **app/:** All code requires TDD approach (test first)
- **tests/:** All new functions require author headers
- **Tests must:** Achieve 100% coverage before merging

---

## Workflow Integration

### Pre-Test Phase
1. Request new feature implementation (follows TDD)
2. Run `pytest` to understand current state
3. Check coverage: `pytest --cov=app --cov-branch --cov-report=term-missing`

### Test Expert Phase
1. Invoke agent with coverage analysis and requirements
2. Agent generates failing tests first (Red phase)
3. Agent provides verification commands

### Implementation Phase
1. Implement minimal code to pass tests (Green phase)
2. Run `pytest` to verify tests pass
3. Refactor while keeping tests green (Refactor phase)
4. Verify coverage is 100%

### Verification Phase
1. Run `pytest` - all tests pass
2. Run `pytest --cov=app --cov-branch --cov-report=term-missing` - 100% coverage
3. Review test quality and architecture
4. Commit and merge

---

## Related Documentation

- **Agent Guide:** `agent.md`
- **Implementation Guide:** `IMPLEMENTATION_GUIDE.md`
- **Quick Reference:** `QUICK_REFERENCE.md`
- **App Instructions:** `.github/instructions/app.instructions.md`
- **Test Instructions:** `.github/instructions/tests.instructions.md`
- **TDD Skill:** `.github/skills/tdd-python/SKILL.md`

---

## Maintenance & Updates

### Version History
- **1.0 (2026-04-16):** Initial release
  - Coverage analysis capability
  - Test generation with TDD support
  - Pytest best practices
  - 100% coverage enforcement

### Future Enhancements
- Performance testing patterns
- Integration testing templates
- Mutation testing integration
- Test performance profiling
- Snapshot testing patterns

### Support & Feedback
For issues or improvements, please:
1. Run coverage analysis to understand current state
2. Review test architecture in `tests/`
3. Check related instructions in `.github/`
4. Provide feedback with specific use cases

