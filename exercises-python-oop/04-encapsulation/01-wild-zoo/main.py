import unittest

from project import Caretaker, Cheetah, Keeper, Lion, Tiger, Vet, Zoo


class TestFoo(unittest.TestCase):
    def test_foo(self):
        z = Zoo("My Zoo", 500, 3, 3)
        z.hire_worker(Vet("Leo", 35, 100))
        z.hire_worker(Keeper("Tigy", 40, 100))
        z.hire_worker(Caretaker("Chi", 24, 100))
        res = z.workers_status()
        self.assertEqual(res, "You have 3 workers\n----- 1 Keepers:\nName: Tigy, Age: 40, Salary: 100\n----- 1 Caretakers:\nName: Chi, Age: 24, Salary: 100\n----- 1 Vets:\nName: Leo, Age: 35, Salary: 100")
