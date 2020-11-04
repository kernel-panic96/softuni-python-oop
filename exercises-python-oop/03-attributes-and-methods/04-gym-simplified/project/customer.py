from typing import ClassVar


class Customer:
    name: str
    address: str
    email: str
    _id: ClassVar[int] = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self._id
        self.__class__._id += 1

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'

    @classmethod
    def get_next_id(cls):
        return cls._id
