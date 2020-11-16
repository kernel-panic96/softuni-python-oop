from project.animals.animal import Mammal
from project.food import Fruit, Meat, Vegetable


class Tiger(Mammal):
    def make_sound(self):
        return 'ROAR!!!'

    @property
    def _food_preferences(self):
        return tuple([Meat])

    @property
    def _weight_gain_per_food(self):
        return 1.00


class Dog(Mammal):
    def make_sound(self):
        return 'Woof!'

    @property
    def _food_preferences(self):
        return tuple([Meat])

    @property
    def _weight_gain_per_food(self):
        return 0.40


class Cat(Mammal):
    def make_sound(self):
        return 'Meow'

    @property
    def _food_preferences(self):
        return (Meat, Vegetable)

    @property
    def _weight_gain_per_food(self):
        return 0.30


class Mouse(Mammal):
    def make_sound(self):
        return 'Squeak'

    @property
    def _food_preferences(self):
        return (Vegetable, Fruit)

    @property
    def _weight_gain_per_food(self):
        return 0.10
