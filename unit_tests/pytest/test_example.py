'''
This is a starter guide to pytest.

Install pytest with pip:
    pip install -U pytest
    pytest --version

Run all tests in current directory and all sub-directories (only applies to files starting with
test_, functions starting or ending with test and classes starting with Test):
    pytest
    pytest -vv
    pytest -q
- run tests in a module:
    pytest test_module.py
- run tests in a directory and subdirectories
    pytest testing/
- run tests by keyword expression
    pytest -k 'MyClass and not method'
- run tests by collection arguments
    pytest tests/test_module.py::test_function
    pytest tests/test_module.py::TestClass
    pytest tests/test_module.py::TestClass:test_method
- run tests decorated with a mark
    pytest -m test_mark

Flags:
    -vv -> verbose
    -q -> quiet
'''
import pytest

# Test a function result
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3

# Test an exception is raised
def throw_exc():
    raise SystemExit(1)

def test_raises():
    with pytest.raises(SystemExit):
        throw_exc()

# Group multiple tests in a class
class TestExample:

    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        greeting = 'Hellow World!'
        assert 'orld' in greeting

# Compare floating-point values
def calculate_floats(a, b):
    return a + b

def test_calculate_floats():
    assert calculate_floats(0.1, 0.2) == pytest.approx(0.3)
