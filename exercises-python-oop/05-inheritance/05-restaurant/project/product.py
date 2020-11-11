class Product:
    _name: str
    _price: float

    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        self._price = val
