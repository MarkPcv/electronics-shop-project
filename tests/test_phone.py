import pytest
from src.phone import Phone

@pytest.fixture
def phone1():
    return Phone("iPhone X", 90_000, 10, 1)

def test_phone_init(phone1):
    """
    Checks correct Phone class instance initialization
    """
    assert phone1.name == "iPhone X"
    assert phone1.price == 90000
    assert phone1.quantity == 10
    assert phone1.number_of_sim == 1

def test_phone_repr(phone1):
    """
    Checks __repr__ dunder-method
    """
    assert repr(phone1) == "Phone('iPhone X', 90000, 10, 1)"

def test_sim_setter(phone1):
    """
    Checks number_of_sim setter
    """
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
    # Check exception for value not digit or less or equal to zero
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
        phone1.number_of_sim = 1.5
        phone1.number_of_sim = -4
