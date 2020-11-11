from typing import ClassVar

from project.food.main_dish import MainDish


class Salmon(MainDish):
    SALMON_GRAMS: ClassVar[int] = 22

    def __init__(self, name, price):
        super().__init__(name, price, self.__class__.SALMON_GRAMS)