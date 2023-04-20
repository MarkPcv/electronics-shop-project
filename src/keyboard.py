from src.item import Item

class KeyLang:

    def __init__(self):
        """
        Initialization of instance
        """
        self.__language = "EN"

    @property
    def language(self):
        """
        Getter for language attribute
        """
        return self.__language


    def change_lang(self):
        """
        Changes language of keyboard
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self



class Keyboard(Item, KeyLang):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Initialization of instance
        """
        # Initialization of first parent class
        super().__init__(name, price, quantity)


