# Test Expert Quick Reference

## 🎯 What This Agent Does

The Test Expert agent **creates comprehensive test suites** that achieve **100% line and branch coverage** using modern Python testing best practices and TDD workflow.

---

## ⚡ Quick Commands

### Check Current Coverage
```bash
pytest --cov=app --cov-branch --cov-report=term-missing
```

### Run All Tests
```bash
pytest
```

### Run Specific Test
```bash
pytest tests/test_inventory.py::test_parse_transactions
```

### Generate Coverage Report (HTML)
```bash
pytest --cov=app --cov-branch --cov-report=html
# Then open htmlcov/index.html
```

---

## 📋 When to Use Test Expert

| Scenario | Prompt |
|----------|--------|
| **New function needs tests** | "Create comprehensive tests for `function_name()` in `app/module.py` covering happy paths, error paths, and edge cases." |
| **Coverage gap exists** | "Generate tests for uncovered lines [list line numbers] in `app/module.py`." |
| **Improve test quality** | "Review `tests/test_module.py` and suggest improvements for architecture and clarity." |
| **Reach 100% coverage** | "Create a test suite achieving 100% coverage for `app/module.py`." |
| **Error path testing** | "Write tests for all error scenarios in `function_name()` including exception cases." |

---

## ✅ Test Format Template

Every test the agent creates follows this structure:

```python
# Author: <your git username>
# Date: YYYY-MM-DD
def test_<subject>_<behavior>_<expected_outcome>() -> None:
    # ARRANGE: Set up test data
    input_data = ...
    expected_result = ...
    
    # ACT: Call function under test
    result = function_under_test(input_data)
    
    # ASSERT: Verify result
    assert result == expected_result
```

---

## 🎓 Testing Best Practices

### ✅ DO

- ✅ Name tests descriptively: `test_parse_transactions_with_valid_input_returns_list`
- ✅ Use Arrange-Act-Assert pattern
- ✅ Test happy paths, error paths, and edge cases
- ✅ Use `pytest.raises()` for exception testing
- ✅ Use parametrized tests `@pytest.mark.parametrize` for multiple inputs
- ✅ Create fixtures for shared setup

### ❌ DON'T

- ❌ Use vague test names: `test_function` or `test_something`
- ❌ Mix Arrange/Act/Assert without clear separation
- ❌ Skip error path testing
- ❌ Use bare `except:` in tests
- ❌ Create test interdependencies (tests affecting each other)
- ❌ Repeat setup code in every test

---

## 📊 Coverage Targets

| Metric | Target | Check Command |
|--------|--------|---|
| **Line Coverage** | 100% | `pytest --cov=app --cov-report=term-missing` |
| **Branch Coverage** | 100% | `pytest --cov=app --cov-branch --cov-report=term-missing` |
| **All Functions Tested** | 100% | `pytest --cov=app --cov-report=term-missing` |

---

## 🔍 Analyze Coverage Output

```
------------ coverage: platform win32, pytest-8.3.2, pytest-cov-6.x.x-----------
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
app/__init__.py       10      0   100%
app/inventory.py      25      3    88%   42, 45, 48
app/__main__.py       15      0   100%
-----------------------------------------------
TOTAL                 50      3    94%
```

**Interpretation:**
- `Stmts`: Total statements in module
- `Miss`: Uncovered statements
- `Missing`: Line numbers not covered by tests
- **Action:** Create tests for lines 42, 45, 48 in `app/inventory.py`

---

## 🧪 Common Test Patterns

### Test Happy Path
```python
def test_parse_transactions_with_valid_input_returns_list() -> None:
    result = parse_transactions("apples,3\nbananas,-1")
    assert result == [("apples", 3), ("bananas", -1)]
```

### Test Error Path
```python
def test_parse_transactions_with_missing_comma_raises_valueerror() -> None:
    with pytest.raises(ValueError, match="transaction must be 'item,delta'"):
        parse_transactions("apples 3")
```

### Test Edge Case
```python
def test_parse_transactions_with_empty_input_returns_empty_list() -> None:
    result = parse_transactions("")
    assert result == []
```

### Test with Fixture
```python
@pytest.fixture
def sample_transactions():
    return "apples,3\nbananas,-1\n"

def test_parse_transactions(sample_transactions) -> None:
    result = parse_transactions(sample_transactions)
    assert len(result) == 2
```

### Parametrized Test
```python
@pytest.mark.parametrize("input_text,expected", [
    ("apples,3", [("apples", 3)]),
    ("", []),
    ("item,1\nitem,2", [("item", 1), ("item", 2)]),
])
def test_parse_transactions_various_inputs(input_text, expected) -> None:
    assert parse_transactions(input_text) == expected
```

---

## 🚀 TDD Workflow (Red-Green-Refactor)

### 🔴 Red Phase
Test fails because function doesn't exist or is incomplete:
```bash
pytest tests/test_new_feature.py
# FAILED - as expected
```

### 🟢 Green Phase
Implement minimal code to make test pass:
```python
def function_under_test():
    return expected_value
```

### 🔵 Refactor Phase
Improve code quality while keeping tests green:
```bash
pytest  # Still passing
pytest --cov=app --cov-branch --cov-report=term-missing  # Coverage improved
```

---

## 📝 Author Header Rules

Every NEW test function must have author and date:

```python
# Author: Contoso User           # From: git config user.name
# Date: 2026-04-16               # Format: YYYY-MM-DD
def test_example() -> None:
    assert True
```

**Rules:**
- Place header directly above `def test_` line
- No blank line between header and function definition
- Use `git config user.name` for author
- Use today's date in YYYY-MM-DD format
- Only for functions starting with `test_` (not fixtures or helpers)

---

## 🔗 Project Integration

### File Locations
- **App code:** `app/`
- **Tests:** `tests/`
- **Agent instructions:** `.github/agents/test-expert/`
- **App TDD rules:** `.github/instructions/app.instructions.md`
- **Test rules:** `.github/instructions/tests.instructions.md`

### Related Skills & Instructions
- **TDD Workflow:** `.github/skills/tdd-python/SKILL.md`
- **App Requirements:** `.github/instructions/app.instructions.md`
- **Test Requirements:** `.github/instructions/tests.instructions.md`

---

## 🎯 Success Criteria

✅ Tests pass: `pytest` (exit code 0)  
✅ Coverage is 100%: `pytest --cov=app --cov-branch --cov-report=term-missing`  
✅ All new tests have author headers  
✅ Test names are descriptive  
✅ Tests follow Arrange-Act-Assert pattern  
✅ Tests are isolated (no interdependencies)  
✅ Code is committed and reviewed  

---

## 💡 Pro Tips

1. **Use HTML Coverage Reports** - Run `pytest --cov=app --cov-branch --cov-report=html` then open `htmlcov/index.html` for visual coverage analysis

2. **Parametrize for Multiple Scenarios** - Instead of writing 5 similar tests, use `@pytest.mark.parametrize` with 5 different inputs

3. **Create Fixtures Early** - If multiple tests use the same setup, create a fixture in `conftest.py` instead of repeating code

4. **Test Names as Documentation** - Good test names explain what's being tested without needing to read the test code

5. **Match Exception Messages** - Use `match="pattern"` in `pytest.raises()` to verify error messages are helpful

6. **Run Coverage After Each Change** - Make it a habit: write test → verify it fails → write code → verify coverage improves

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Coverage won't reach 100% | Run `pytest --cov=app --cov-branch --cov-report=term-missing`, create tests for listed lines |
| Test fails unpredictably | Check for shared state, ensure proper test isolation using fixtures |
| Can't import app code in tests | Run `python -m pip install -e .` to install package in development mode |
| Not sure what to test | Ask Test Expert: "What code paths are uncovered in [module]?" |
| Tests are hard to understand | Use Arrange-Act-Assert pattern, create fixtures, improve test naming |

---

## 🎓 Learning Resources

- **Pytest Docs:** https://docs.pytest.org/
- **Python Testing Best Practices:** https://realpython.com/python-testing/
- **TDD Guide:** https://en.wikipedia.org/wiki/Test-driven_development
- **AAA Pattern:** Arrange-Act-Assert structure for clear tests

---

## 📞 Invoke the Agent

### Simple Invocation
```
@test-expert Generate tests for uncovered code in app/inventory.py
```

### Detailed Invocation
```
Use the Test Expert Agent to:
1. Analyze current coverage of app/inventory.py
2. Identify all uncovered lines and branches
3. Create failing tests first following TDD
4. Verify tests pass and coverage reaches 100%
5. Include author headers on all new tests
```

---

**Last Updated:** 2026-04-16  
**Test Expert Version:** 1.0

