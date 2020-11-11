from typing import ClassVar

from project.food.dessert import Dessert


class Cake(Dessert):
    CAKE_GRAMS: ClassVar[int] = 250
    CAKE_CALORIES: ClassVar[int] = 1000
    CAKE_PRICE: ClassVar[int] = 5

    def __init__(self, name):
        super().__init__(
            name,
            self.__class__.CAKE_PRICE,
            self.__class__.CAKE_GRAMS,
            self.__class__.CAKE_CALORIES
        )