# Test Expert Agent

A sophisticated testing automation agent that generates comprehensive test suites achieving **100% line and branch coverage** using modern Python testing patterns and TDD workflow.

---

## 📚 Documentation Index

| Document | Purpose | Audience |
|----------|---------|----------|
| **[agent.md](agent.md)** | Complete agent specification and capabilities | Developers, QA Engineers |
| **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** | Cheat sheet for common tasks and commands | Quick lookup, first-time users |
| **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** | Step-by-step guide to invoke and use the agent | Hands-on implementation |
| **[CONFIG.md](CONFIG.md)** | Technical configuration and integration details | System architects, integrators |

---

## 🚀 Quick Start

### 1. Check Current Coverage
```bash
pytest --cov=app --cov-branch --cov-report=term-missing
```

### 2. Invoke Test Expert
```
@test-expert Generate comprehensive tests for app/inventory.py 
covering all uncovered lines and achieving 100% coverage
```

### 3. Run Tests
```bash
pytest
```

### 4. Verify Coverage
```bash
pytest --cov=app --cov-branch --cov-report=term-missing
```

---

## ✨ Key Features

### 🎯 Coverage Analysis
- Identifies uncovered lines and branches
- Assesses risk and priority of gaps
- Maps coverage to specific code paths
- Tracks coverage trends

### 🧪 Test Generation
- Writes failing tests first (TDD Red phase)
- Creates parametrized tests for multiple scenarios
- Generates fixtures for reusable setup
- Names tests descriptively (self-documenting)

### 🏗️ Architecture & Quality
- Follows pytest conventions and modern patterns
- Uses Arrange-Act-Assert structure
- Maintains test isolation and independence
- Applies DRY principles via fixtures
- Tests happy paths, error paths, edge cases

### ✅ Project Compliance
- Enforces author headers on new tests
- Respects path-specific instructions
- Integrates with TDD workflow
- Achieves 100% coverage targets
- Compatible with existing test suite

---

## 📋 When to Use

| Situation | Action |
|-----------|--------|
| **New function created** | Ask agent to generate tests covering all behaviors |
| **Coverage gap exists** | Ask agent to create tests for uncovered lines |
| **Want to improve tests** | Ask agent to review and suggest improvements |
| **Need error path tests** | Ask agent to test all exception scenarios |
| **Reach 100% coverage** | Ask agent to generate tests achieving target |

---

## 🔧 How to Invoke

### Basic Invocation
```
@test-expert <what you need>
```

### Examples

**Generate tests for new code:**
```
@test-expert Create comprehensive tests for the new calculate_total() 
function in app/inventory.py. Cover happy paths, error paths, and 
edge cases. Target 100% coverage.
```

**Fix coverage gaps:**
```
@test-expert Lines 42, 45, 48 in app/inventory.py are uncovered. 
Write tests that exercise these code paths.
```

**Improve existing tests:**
```
@test-expert Review tests/test_inventory.py and suggest architectural 
improvements using fixtures, parametrization, and better naming.
```

---

## 📖 Test Format

Every test follows this standard structure:

```python
# Author: <your git username>
# Date: YYYY-MM-DD
def test_<subject>_<behavior>_<expected_outcome>() -> None:
    # ARRANGE - Set up test data and dependencies
    input_data = "apples,3\nbananas,-1"
    expected = [("apples", 3), ("bananas", -1)]
    
    # ACT - Call the function under test
    result = parse_transactions(input_data)
    
    # ASSERT - Verify the result
    assert result == expected
```

---

## 📊 Coverage Targets

- **Line Coverage:** 100% (every line executed)
- **Branch Coverage:** 100% (every if/else branch tested)
- **Function Coverage:** 100% (every function has tests)

### Check Coverage
```bash
pytest --cov=app --cov-branch --cov-report=term-missing
```

### Generate HTML Report
```bash
pytest --cov=app --cov-branch --cov-report=html
# Open htmlcov/index.html in browser
```

---

## 🎓 Best Practices

### ✅ DO

- Write descriptive test names
- Use Arrange-Act-Assert pattern
- Test happy paths, error paths, edge cases
- Create fixtures for shared setup
- Use parametrization for multiple inputs
- Maintain test isolation

### ❌ DON'T

- Use vague test names (`test_function`)
- Mix setup/execution/verification without clear separation
- Skip error path testing
- Create test interdependencies
- Repeat setup code across tests
- Test private/internal functions

---

## 🔄 TDD Workflow

Test Expert integrates with the TDD Red-Green-Refactor cycle:

### 🔴 Red Phase
Agent writes failing tests that describe desired behavior
```bash
pytest tests/test_new_feature.py
# FAILED - as expected
```

### 🟢 Green Phase
You implement minimal code to pass tests
```python
def function_under_test():
    return expected_value
```

### 🔵 Refactor Phase
Improve code quality while keeping tests green
```bash
pytest  # Still passing
pytest --cov=app --cov-branch --cov-report=term-missing  # 100% coverage
```

---

## 🛠️ Common Commands

| Task | Command |
|------|---------|
| Run all tests | `pytest` |
| Check coverage | `pytest --cov=app --cov-branch --cov-report=term-missing` |
| HTML coverage report | `pytest --cov=app --cov-branch --cov-report=html` |
| Run specific test | `pytest tests/test_inventory.py::test_parse_transactions` |
| Verbose output | `pytest -v` |
| Stop on first failure | `pytest -x` |

---

## 📍 File Structure

```
.github/
├── agents/
│   └── test-expert/
│       ├── README.md                    # This file
│       ├── agent.md                     # Complete agent specification
│       ├── QUICK_REFERENCE.md          # Cheat sheet
│       ├── IMPLEMENTATION_GUIDE.md      # How to use
│       └── CONFIG.md                    # Technical details
├── instructions/
│   ├── app.instructions.md              # App development rules (TDD required)
│   └── tests.instructions.md            # Test file rules (author headers)
└── skills/
    └── tdd-python/                      # TDD workflow skill
```

---

## 🔗 Related Resources

- **TDD Skill:** `.github/skills/tdd-python/` - Red-Green-Refactor guidance
- **App Instructions:** `.github/instructions/app.instructions.md` - All app code requires TDD
- **Test Instructions:** `.github/instructions/tests.instructions.md` - Author headers required
- **Pytest Documentation:** https://docs.pytest.org/
- **Coverage.py:** https://coverage.readthedocs.io/

---

## ✓ Success Criteria

After using Test Expert, verify:

- [ ] All new tests have author headers (Author: and Date:)
- [ ] Test names follow pattern: `test_<subject>_<behavior>_<outcome>`
- [ ] Tests pass: `pytest` (exit code 0)
- [ ] Coverage is 100%: `pytest --cov=app --cov-branch --cov-report=term-missing`
- [ ] Tests follow Arrange-Act-Assert pattern
- [ ] No test interdependencies
- [ ] Fixtures used for shared setup
- [ ] Code committed and reviewed

---

## 🆘 Common Issues

| Problem | Solution |
|---------|----------|
| **Coverage won't reach 100%** | Run `pytest --cov=app --cov-branch --cov-report=term-missing` and create tests for listed lines |
| **Tests fail unpredictably** | Check for shared state, ensure proper test isolation using fixtures |
| **Hard to understand tests** | Use Arrange-Act-Assert pattern, create fixtures, improve naming |
| **Not sure what to test** | Ask: "What code paths are uncovered in [module]?" |

---

## 📞 Getting Help

1. **See common patterns:** Review [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
2. **Step-by-step guide:** Follow [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)
3. **Complete specification:** Read [agent.md](agent.md)
4. **Technical details:** Consult [CONFIG.md](CONFIG.md)
5. **Project conventions:** Check `.github/instructions/`

---

## 📝 Example Invocation

```
@test-expert I've just created a new parse_inventory() function 
in app/inventory.py that takes a file path and returns a dictionary 
of item counts. It should:
- Parse lines in "item,count" format
- Raise ValueError for invalid format
- Return empty dict for empty files

Create comprehensive tests achieving 100% coverage, including happy 
paths, error cases, and edge cases. Write failing tests first 
following TDD.
```

Expected output:
- Complete test suite with all scenarios
- Author headers on all tests
- Parametrized tests for multiple inputs
- Error tests with proper exception matching
- Verification commands and results

---

## 🎯 Next Steps

1. **First time?** Start with [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
2. **Want details?** Read [agent.md](agent.md)
3. **Ready to use?** Follow [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)
4. **Need technical info?** Check [CONFIG.md](CONFIG.md)
5. **Have coverage gaps?** Invoke `@test-expert` and describe what to test

---

**Created:** 2026-04-16  
**Version:** 1.0  
**Status:** Active  

