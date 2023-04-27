from csv import DictReader

class InstantiateCSVError(Exception):
    """
    Class for tracking exceptions during CSV reading
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "File 'item.csv' is corrupted"

class ItemHandler:
    """
    Class handler for processing data from a CSV file
    """
    def __init__(self, row: dict):

        if not row['price'].replace('.', '').isnumeric():
            raise InstantiateCSVError
        elif not row['quantity'].isnumeric():
            raise InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Converts string to integer
        Caution: if string represents float function will round it down
        Example: '5.999' returns 5
        """
        return int(float(string))

    @classmethod
    def instantiate_from_csv(cls, path:str = '../src/items.csv') -> None:
        """
        Creates class instances from CSV file
        """
        cls.all = []  # clear list of instances
        PATH = path  # path to csv file
        ENCODING = 'windows-1251'  # encoding for csv file

        try:
            open(PATH, newline='', encoding=ENCODING)
        except FileNotFoundError:
            raise FileNotFoundError("File 'items.csv' does not exist")
        else:
            # read each row of csv file and create a new instance
            with open(PATH, newline='', encoding=ENCODING) as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    try:
                        ItemHandler(row)
                    except InstantiateCSVError:
                        raise InstantiateCSVError()
                    else:
                        Item(row['name'],
                             float(row['price']),
                             int(row['quantity']))


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name        # private attribute
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        """
        Provides a string representation of class object for user
        """
        return self.__name

    def __repr__(self):
        """
        Provides a DETAILED representation of class object for developer
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Getter for attribute "name"
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Setter for attribute "name"
        """
        try:
            if len(new_name) <= 10:
                self.__name = new_name
            else:
                raise ValueError
        except ValueError:
            print("Name must contain no more than 10 characters")

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('You cannot add different classes')
