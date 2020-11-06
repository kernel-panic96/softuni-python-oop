from collections import defaultdict
from typing import List, Union

from project import Caretaker, Cheetah, Keeper, Lion, Tiger, Vet

Animal = Union[Tiger, Cheetah, Lion]
Worker = Union[Vet, Caretaker, Keeper]


class Zoo:
    animals: List[Animal]
    workers: List[Worker]

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) >= self.__animal_capacity:
            return 'Not enough space for animal'
        if self.__budget < price:
            return 'Not enough budget'

        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) >= self.__workers_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name: str) -> str:
        workers = [w for w in self.workers if w.name == worker_name]
        if not workers:
            return f'There is no {worker_name} in the zoo'

        self.workers.remove(workers[0])
        return f'{worker_name} fired successfully'

    def pay_workers(self):
        salaries_expense = sum([w.salary for w in self.workers])

        if salaries_expense > self.__budget:
            return 'You have no budget to pay your workers. They are unhappy'
        self.__budget -= salaries_expense
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        animals_expense = sum([a.get_needs() for a in self.animals])
        if animals_expense > self.__budget:
            return 'You have no budget to tend the animals. They are unhappy.'

        self.__budget -= animals_expense
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, profit):
        self.__budget += profit

    def animals_status(self):
        animals_by_type = defaultdict(list)
        for a in self.animals:
            animals_by_type[a.__class__.__name__].append(a)

        return '\n'.join([
            f'You have {len(self.animals)} animals',
            f'----- {len(animals_by_type["Lion"])} Lions:'
        ] + [
            repr(lion) for lion in animals_by_type['Lion']
        ] + [
            f'----- {len(animals_by_type["Tiger"])} Tigers:'
        ] + [
            repr(tiger) for tiger in animals_by_type['Tiger']
        ] + [
            f'----- {len(animals_by_type["Cheetah"])} Cheetahs:'
        ] + [
            repr(cheetah) for cheetah in animals_by_type['Cheetah']
        ])

    def workers_status(self):
        workers_by_type = defaultdict(list)
        for w in self.workers:
            workers_by_type[w.__class__.__name__].append(w)

        return '\n'.join([
            f'You have {len(self.workers)} workers',
            f'----- {len(workers_by_type["Keeper"])} Keepers:'
        ] + [
            repr(w) for w in workers_by_type['Keeper']
        ] + [
            f'----- {len(workers_by_type["Caretaker"])} Caretakers:'
        ] + [
            repr(w) for w in workers_by_type['Caretaker']
        ] + [
            f'----- {len(workers_by_type["Vet"])} Vets:'
        ] + [
            repr(w) for w in workers_by_type['Vet']
        ])
