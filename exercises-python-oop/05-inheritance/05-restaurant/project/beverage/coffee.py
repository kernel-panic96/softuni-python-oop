from typing import ClassVar

from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS: ClassVar[int] = 50
    COFFEE_PRICE: ClassVar[float] = 3.50

    __caffeine: float

    def __init__(self, name, caffeine):
        super().__init__(
            name=name,
            price=self.__class__.COFFEE_PRICE,
            milliliters=self.__class__.COFFEE_MILLILITERS,
        )
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, val):
        self.__caffeine = val


# dict
# d = DotableDict({x: 1, y: {'z': 2})
# d["x.y.z"]
# __getitem__(self, val)