from src.item import Item

class Phone(Item):
    # Initialization
    def __init__(self, name: str, price: float, quantity: int,
                 number_of_sim: int) -> None:
        # Initialization of parent class
        super().__init__(name, price, quantity)
        # Add new attributes
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Provides a DETAILED representation of class object for developer
        """
        return (f"Phone('{self.name}', {self.price}, "
                f"{self.quantity}, {self.number_of_sim})")

    @property
    def number_of_sim(self) -> int:
        """
        Getter for attribute "number_of_sim"
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number: int) -> None:
        """
        Setter for attribute "number_of_sim"
        """
        if new_number > 0 and isinstance(new_number, int):
            self.__number_of_sim = new_number
        else:
            raise ValueError('Number of SIM cards must '
                             'be integer greater than zero')
    