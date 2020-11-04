from typing import ClassVar


class Subscription:
    date: str
    customer_id: int
    trainer_id: int
    exercise_id: int
    id: int

    _id: ClassVar[int] = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self._id
        self.__class__._id += 1

    @classmethod
    def get_next_id(cls):
        return cls._id

    def __repr__(self):
        return f'Subscription <{self.id}> on {self.date}'
