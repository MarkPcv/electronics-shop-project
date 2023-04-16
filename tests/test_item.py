"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item_book():
    return Item("Book", 500, 10)


@pytest.fixture
def item_bag():
    return Item("Bag", 1000, 5)

@pytest.fixture
def phone():
    return Phone('iPhone', 70000, 20, 1)

def test_show_all(item_book, item_bag):
    """
    Checks total number of class instances
    """
    assert len(Item.all) == 2


def test_item_init(item_book):
    """
    Checks correct Item class instance initialization
    """
    assert item_book.name == "Book"
    assert item_book.price == 500
    assert item_book.quantity == 10


def test_calculate_total_price(item_book):
    """
    Checks correct calculation of total price of item
    """
    assert item_book.calculate_total_price() == 5000


def test_apply_discount(item_book):
    """
    Checks that correct discount is applied
    """
    item_book.pay_rate = 0.65
    item_book.apply_discount()
    assert item_book.price == 325


def test_instantiate_from_csv():
    """
    Checks that all instances from csv file has been created
    """
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number(item_bag):
    """
    Checks conversion of string to integer
    """
    assert item_bag.string_to_number('7') == 7
    assert item_bag.string_to_number('7.0') == 7
    assert item_bag.string_to_number('7.5') == 7


def test_name_getter(item_bag):
    """
    Checks name getter
    """
    assert item_bag.name == 'Bag'


def test_name_setter(item_bag):
    """
    Checks name setter
    """
    item_bag.name = 'Box'
    assert item_bag.name == 'Box'
    # Check exception for >10 chars
    item_bag.name = 'SuperPuperBag'
    assert item_bag.name == 'Box'


def test_item_repr(item_bag):
    """
    Checks __repr__ dunder-method
    """
    assert repr(item_bag) == "Item('Bag', 1000, 5)"


def test_item_str(item_book):
    """
    Checks __str__ dunder-method
    """
    assert str(item_book) == "Book"


def test_item_add(item_book, phone):
    """
    Check __add__ dunder-method
    """
    integer_object = 30
    assert item_book + phone == 30
    assert phone + phone == 40
    assert phone + item_book == 30
    with pytest.raises(ValueError):
        phone + integer_object
