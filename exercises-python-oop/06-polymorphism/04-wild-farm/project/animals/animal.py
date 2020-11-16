from abc import ABC, abstractmethod
from typing import Union

from project.food import Food


class Animal(ABC):  # metaclasses
    name: str
    weight: float
    food_eaten: int

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    def feed(self, food: Food) -> Union[None, str]:
        if self._FOOD_PREFERENCES is not None and not isinstance(food, self._FOOD_PREFERENCES):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * self._WEIGHT_GAIN_PER_FOOD
        self.food_eaten += food.quantity
        return None

    @property
    @abstractmethod
    def _FOOD_PREFERENCES(self):
        ...

    @property
    @abstractmethod
    def _WEIGHT_GAIN_PER_FOOD(self):
        ...

    @abstractmethod
    def make_sound(self) -> str:
        ...


class Bird(Animal):
    wing_size: float

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return '{type} [{name}, {wing_size}, {weight}, {food_eaten}]'.format(
            type=self.__class__.__name__,
            name=self.name,
            wing_size=self.wing_size,
            weight=self.weight,
            food_eaten=self.food_eaten
        )


class Mammal(Animal):
    living_region: str

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return '{type} [{name}, {weight}, {region}, {eaten}]'.format(
            type=self.__class__.__name__,
            name=self.name,
            weight=self.weight,
            region=self.living_region,
            eaten=self.food_eaten,
        )
