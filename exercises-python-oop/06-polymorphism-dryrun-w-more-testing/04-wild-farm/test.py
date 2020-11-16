# test animals abstraction and inheritance
import unittest

from project.animals.animal import Animal, Bird, Mammal
from project.animals.birds import Hen, Owl
from project.animals.mammals import Cat, Dog, Mouse, Tiger
from project.food import Fruit, Meat, Seed, Vegetable


class WildFarmTests(unittest.TestCase):
    def test_animals_abs_and_inheritance(self):
        self.assertEqual(Animal.__bases__[0].__name__, "ABC")
        self.assertTrue(len(list(Animal.__abstractmethods__)) > 0)
        self.assertTrue("Animal" in [x.__name__ for x in Bird.__bases__])
        self.assertTrue("ABC" in [x.__name__ for x in Bird.mro()])
        self.assertTrue("Animal" in [x.__name__ for x in Mammal.__bases__])
        self.assertTrue("ABC" in [x.__name__ for x in Mammal.mro()])
        self.assertEqual(Mouse.__bases__[0].__name__, "Mammal")
        self.assertEqual(Dog.__bases__[0].__name__, "Mammal")
        self.assertEqual(Tiger.__bases__[0].__name__, "Mammal")
        self.assertEqual(Cat.__bases__[0].__name__, "Mammal")
        self.assertEqual(Owl.__bases__[0].__name__, "Bird")
        self.assertEqual(Hen.__bases__[0].__name__, "Bird")

if __name__ == "__main__":
    unittest.main()
