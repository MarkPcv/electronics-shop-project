import pytest
from src.keyboard import Keyboard

@pytest.fixture
def keyboard1():
    return Keyboard("HyperX Alloy FPS", 15_000, 5)

def test_keyboard_init(keyboard1):
    """
    Checks correct Keyboard class instance initialization
    """
    assert keyboard1.name == "HyperX Alloy FPS"
    assert keyboard1.price == 15000
    assert keyboard1.quantity == 5
    assert keyboard1.language == "EN"

def test_keyboard_lang_operations(keyboard1):
    """
    Checks change_lang() method and prohibited setter
    """
    keyboard1.change_lang()
    assert keyboard1.language == "RU"
    keyboard1.change_lang()
    assert keyboard1.language == "EN"
    # Check setter
    with pytest.raises(AttributeError):
        keyboard1.language = "KZ"