from src.item import Item

class Phone(Item):
    # Initialization
    def __init__(self, name: str, price: float, quantity: int,
                 number_of_sim: int) -> None:
        # Initialization of parent class
        super().__init__(name, price, quantity)
        # Add new attributes
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Provides a DETAILED representation of class object for developer
        """
        return (f"Phone('{self.name}', {self.price}, "
                f"{self.quantity}, {self.number_of_sim})")

    