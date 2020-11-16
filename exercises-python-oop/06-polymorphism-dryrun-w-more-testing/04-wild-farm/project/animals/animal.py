from abc import ABC, abstractmethod, abstractproperty
from typing import Tuple, Union

from project.food import Food


class Animal(ABC):
    name: str
    weight: float
    food_eaten: float

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self) -> str:
        ...

    def feed(self, food) -> Union[None, str]:
        if self._food_preferences and not isinstance(food, self._food_preferences):  # type: ignore
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += self._weight_gain_per_food * food.quantity
        self.food_eaten += food.quantity
        return None

    @abstractproperty
    def _food_preferences(self) -> Union[Tuple[Food], None]:
        ...

    @abstractproperty
    def _weight_gain_per_food(self) -> float:
        pass


class Bird(Animal):
    wing_size: float

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name=name, weight=weight)
        self.wing_size = wing_size

    def __repr__(self):
        return '{type} [{name}, {wing_size}, {weight}, {food_eaten}]'.format(
            type=self.__class__.__name__,
            name=self.name,
            wing_size=self.wing_size,
            weight=self.weight,
            food_eaten=self.food_eaten,
        )


class Mammal(Animal):
    living_region: str

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return '{type} [{name}, {weight}, {region}, {food_eaten}]'.format(
            type=self.__class__.__name__,
            name=self.name,
            weight=self.weight,
            region=self.living_region,
            food_eaten=self.food_eaten
        )
