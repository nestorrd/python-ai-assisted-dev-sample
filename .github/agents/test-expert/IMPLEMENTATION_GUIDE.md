# Test Expert Agent - Implementation Guide

## Quick Start

### 1. Analyze Current Coverage

```bash
pytest --cov=app --cov-branch --cov-report=term-missing
```

Review the output to identify:
- Which modules have gaps
- Which lines/branches are uncovered
- The overall coverage percentage

### 2. Invoke Test Expert Agent

Ask the agent to generate tests for uncovered areas:

**Scenario A: Generate tests for specific module**
```
"Use the Test Expert Agent to generate tests covering all uncovered lines and 
branches in app/inventory.py. Follow TDD workflow: write failing tests first, 
then verify they pass. Include author headers and reach 100% coverage."
```

**Scenario B: Improve overall coverage**
```
"Use the Test Expert Agent to analyze app/ coverage gaps and create a comprehensive 
test suite that achieves 100% line and branch coverage. Include edge cases, error 
paths, and happy paths for all functions."
```

**Scenario C: Review test quality**
```
"Use the Test Expert Agent to review tests/test_inventory.py and suggest improvements 
for architecture, naming, and coverage. Identify any gaps and create additional tests."
```

### 3. Implementation Process

The agent will:

1. **Analyze** the source code and coverage report
2. **Identify** uncovered lines, branches, and edge cases
3. **Design** test cases following pytest best practices
4. **Implement** new test functions with author headers
5. **Verify** that tests fail initially (Red phase)
6. **Confirm** that coverage reaches 100%

### 4. Review and Merge

After the agent provides test implementations:

```bash
# Verify all tests pass
pytest

# Confirm coverage is 100%
pytest --cov=app --cov-branch --cov-report=term-missing

# Review test quality (readability, naming, structure)
# Then commit and merge
```

---

## Test Expert Responsibilities

### Coverage Analysis
- ✅ Identify uncovered lines and branches
- ✅ Assess risk and priority of gaps
- ✅ Map coverage to source functions
- ✅ Detect missing edge cases

### Test Design
- ✅ Name tests descriptively (test_<subject>_<behavior>_<outcome>)
- ✅ Structure tests using Arrange-Act-Assert pattern
- ✅ Cover happy paths, error paths, edge cases
- ✅ Use parametrized tests for multiple scenarios
- ✅ Create fixtures for shared setup

### Code Quality
- ✅ Follow pytest conventions
- ✅ Use clear, specific assertions
- ✅ Maintain test isolation
- ✅ Keep tests DRY with fixtures
- ✅ Ensure tests are maintainable

### Compliance
- ✅ Add author headers (Author: and Date: fields)
- ✅ Use correct date format (YYYY-MM-DD)
- ✅ Follow path-specific instructions
- ✅ Achieve 100% coverage target
- ✅ Integrate with existing test suite

---

## Common Invocation Patterns

### Pattern 1: New Feature Tests
**Situation:** You've implemented a new function and need test coverage.

```
"Generate comprehensive tests for the new calculate_total() function in app/inventory.py. 
Write failing tests first following TDD. Cover:
- Valid inputs (happy path)
- Invalid inputs (error paths)
- Edge cases (empty list, zero values, large numbers)
Target 100% coverage."
```

### Pattern 2: Uncovered Code Coverage
**Situation:** Coverage report shows 87%, with specific lines uncovered.

```
"The coverage report shows app/inventory.py line 42, 45, 48 are uncovered in the 
summarize() function. Create tests that exercise these code paths, then verify 
coverage reaches 100%."
```

### Pattern 3: Test Refactoring
**Situation:** Existing tests work but are hard to maintain.

```
"Review tests/test_inventory.py and suggest architectural improvements. Are there 
opportunities to use fixtures, parametrization, or better naming? Create improved 
versions of tests that are harder to break."
```

### Pattern 4: Error Path Coverage
**Situation:** You want to ensure all error handling is tested.

```
"Analyze app/inventory.py and identify all error paths (try/except blocks, validation 
checks, guard clauses). Write tests that exercise every error scenario. Verify coverage 
report shows all error branches are tested."
```

---

## Test Organization Best Practices

### File Structure

```
tests/
├── test_inventory.py      # Tests for app/inventory.py
├── test_cli.py            # Tests for app/__main__.py or CLI code
└── conftest.py            # Shared fixtures and test configuration
```

### Fixture Organization

```python
# conftest.py - Shared fixtures
@pytest.fixture
def sample_transactions():
    """Fixture providing test transaction data."""
    return "apples,3\nbananas,-1\n"

@pytest.fixture
def tmp_inventory(tmp_path):
    """Fixture providing temporary directory for file operations."""
    inventory_file = tmp_path / "inventory.txt"
    inventory_file.write_text("apples,5\n")
    return inventory_file
```

### Test Grouping

```python
# Grouped by function with clear organization
class TestParseTransactions:
    def test_valid_input(self): ...
    def test_missing_comma_error(self): ...
    def test_empty_input(self): ...

class TestSummarizeInventory:
    def test_single_item(self): ...
    def test_multiple_items(self): ...
    def test_empty_inventory(self): ...
```

---

## Metrics & Targets

### Coverage Goals

- **Line Coverage:** 100% - Every line of code must be executed
- **Branch Coverage:** 100% - Every `if`/`elif`/`else` branch must be tested
- **Function Coverage:** 100% - Every function must have at least one test

### Test Quality Metrics

| Metric | Target | Why |
|--------|--------|-----|
| Tests per public function | 3-5 | Covers happy path, error cases, edge cases |
| Parametrized test combinations | 5-10 per test | Comprehensive input coverage |
| Assertion clarity | 100% understandable | Tests serve as documentation |
| Test isolation | No shared state | Tests run independently |

### Coverage Reporting

```bash
# Terminal output shows coverage by file and percentage
# Missing lines are explicitly listed
pytest --cov=app --cov-branch --cov-report=term-missing

# HTML report provides visual analysis
pytest --cov=app --cov-branch --cov-report=html
# Open htmlcov/index.html to see line-by-line coverage
```

---

## Integration Checklist

When Test Expert provides new tests:

- [ ] All tests have author headers (Author: and Date:)
- [ ] Test names follow pattern: `test_<subject>_<behavior>_<outcome>`
- [ ] Tests use Arrange-Act-Assert pattern
- [ ] Error tests use `pytest.raises()` with message matching
- [ ] Related tests use fixtures to reduce duplication
- [ ] All tests pass: `pytest`
- [ ] Coverage is 100%: `pytest --cov=app --cov-branch --cov-report=term-missing`
- [ ] No imports of private/internal functions (functions starting with `_`)
- [ ] Tests are maintainable and clear to future readers

---

## Advanced Scenarios

### Scenario 1: Testing with Temporary Files

```python
def test_main_with_file_input(tmp_path):
    # ARRANGE
    input_file = tmp_path / "transactions.txt"
    input_file.write_text("apples,3\n")
    
    # ACT
    result = main([str(input_file)])
    
    # ASSERT
    assert result == 0
```

### Scenario 2: Testing Exception Messages

```python
def test_invalid_delta_shows_helpful_error():
    with pytest.raises(ValueError) as exc_info:
        parse_transactions("apples,not-a-number")
    
    assert "delta must be an integer" in str(exc_info.value)
```

### Scenario 3: Testing with Multiple Inputs

```python
@pytest.mark.parametrize("input_text,expected_length", [
    ("apples,3\nbananas,2", 2),
    ("", 0),
    ("single,1", 1),
])
def test_parse_transactions_various_inputs(input_text, expected_length):
    result = parse_transactions(input_text)
    assert len(result) == expected_length
```

### Scenario 4: Testing with Captured Output

```python
def test_report_formatting(capsys):
    report = format_report({"apples": 2, "bananas": 3})
    
    assert report == "apples: 2\nbananas: 3\n"
```

---

## Troubleshooting

### Issue: Coverage Won't Reach 100%

**Solution:**
1. Run coverage report: `pytest --cov=app --cov-branch --cov-report=term-missing`
2. Review uncovered lines - they're listed in output
3. Ask Test Expert: "Create tests for these specific lines: [list]"
4. Re-run coverage to verify improvement

### Issue: Tests Are Flaky (Sometimes Pass, Sometimes Fail)

**Solution:**
1. Check for shared state or dependencies between tests
2. Ensure proper test isolation (no global state modification)
3. Use fixtures for setup/teardown instead of shared variables
4. Ask Test Expert: "Review tests for isolation issues"

### Issue: Test Code Is Hard to Understand

**Solution:**
1. Check test naming - should be descriptive
2. Verify Arrange-Act-Assert structure is clear
3. Use fixtures to reduce setup code
4. Add comments explaining complex test logic
5. Ask Test Expert: "Refactor this test for clarity"

---

## Running the Agent

### Via GitHub Copilot Chat

```
@test-expert Generate tests covering all uncovered lines in app/inventory.py
```

### Via Command Line

If implementing as a subagent:

```python
runSubagent(
    agentName="test-expert",
    description="Generate coverage tests",
    prompt="Create tests to achieve 100% coverage in app/"
)
```

---

## Related Resources

- **TDD Skill:** `.github/skills/tdd-python/` - Red-Green-Refactor workflow
- **App Instructions:** `.github/instructions/app.instructions.md` - TDD requirements
- **Test Instructions:** `.github/instructions/tests.instructions.md` - Author headers
- **Pytest Documentation:** https://docs.pytest.org/
- **Coverage.py:** https://coverage.readthedocs.io/

---

## Contact & Feedback

This agent is designed to work within the repository's TDD workflow and 100% coverage mandate. For issues, improvements, or feedback:

1. Check coverage reports first: `pytest --cov=app --cov-branch --cov-report=term-missing`
2. Review existing test structure in `tests/`
3. Consult `.github/instructions/` for project-specific rules
4. Iterate with the agent to refine test implementation

