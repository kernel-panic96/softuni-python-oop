from project.animals.animal import Mammal
from project.food import Fruit, Meat, Vegetable


class Mouse(Mammal):
    _FOOD_PREFERENCES = (Vegetable, Fruit)
    _WEIGHT_GAIN_PER_FOOD = 0.10

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    _FOOD_PREFERENCES = tuple([Meat])
    _WEIGHT_GAIN_PER_FOOD = 0.40

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    _FOOD_PREFERENCES = (Vegetable, Meat)
    _WEIGHT_GAIN_PER_FOOD = 0.30

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    _FOOD_PREFERENCES = tuple([Meat])
    _WEIGHT_GAIN_PER_FOOD = 1.00

    def make_sound(self):
        return 'ROAR!!!'
