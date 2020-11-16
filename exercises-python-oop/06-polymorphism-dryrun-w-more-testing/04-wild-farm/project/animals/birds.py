from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    def make_sound(self):
        return 'Hoot Hoot'

    @property
    def _food_preferences(self):
        return tuple([Meat])

    @property
    def _weight_gain_per_food(self):
        return 0.25


class Hen(Bird):
    def make_sound(self):
        return 'Cluck'

    @property
    def _food_preferences(self):
        return None

    @property
    def _weight_gain_per_food(self):
        return 0.35
