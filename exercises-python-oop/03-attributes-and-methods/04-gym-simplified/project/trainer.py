from typing import ClassVar


class Trainer:
    name: str
    id: int

    _id: ClassVar[int] = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self._id
        self.__class__._id += 1

    @classmethod
    def get_next_id(cls):
        return cls._id

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'
