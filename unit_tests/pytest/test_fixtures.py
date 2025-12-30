'''
Fixtures allow you to setup the necessary environment for your tests.

At a basic level, test functions request fixtures they require by declaring them as arguments.

When pytest goes to run a test, it looks at the parameters in that test function’s signature, and then searches for fixtures that have the same names as those parameters. Once pytest finds them, it runs those fixtures, captures what they returned (if anything), and passes those objects into the test function as arguments.

Fixtures' options:
    autouse=True
    scope=function|class|module|package|session
'''
import pytest

# Basic fixture test
ANIMALS = ['cat', 'dog', 'cow']

class Animal:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


@pytest.fixture
def animal_farm():
    return [Animal('cat'), Animal('dog'), Animal('cow')]

def test_farm_size(animal_farm):
    assert len(animal_farm) == 3

def test_animals(animal_farm):
    assert all(animal.get_name() in ANIMALS for animal in animal_farm)

# Test fixture calling another fixture/s
@pytest.fixture
def first_entry():
    return 'a'

@pytest.fixture
def first_int():
    return 1

@pytest.fixture
def order(first_entry):
    return [first_entry]

@pytest.fixture
def multi_fixture(order, first_int):
    order.append(first_int)
    return order

def test_string(order):
    order.append('b')

    assert order == ['a', 'b']

def test_int(order):
    order.append(1)

    assert order == ['a', 1]

def test_second(multi_fixture):
    assert multi_fixture == ['a', 1]
