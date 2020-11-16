from typing import List


class Person:
    name: str
    surname: str

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other) -> 'Person':
        if not isinstance(other, self.__class__):
            self_class, other_class = self.__class__.__name__, other.__class__.__name__
            raise TypeError(
                f"unsupported operand type(s) for +: '{self_class}' and '{other_class}'"
            )

        return self.__class__(name=self.name, surname=other.surname)


class Group:
    name: str
    people: List[Person]

    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __str__(self):
        return f'Group {self.name} with members {", ".join(map(str, self.people))}'

    def __getitem__(self, key):
        return f'Person {key}: {self.people[key]}'

    def __add__(self, other: 'Group'):
        if self.__class__ is not other.__class__:
            raise TypeError(
                'unsupported operand type(s) for +: '
                f"{self.__class__.__name__}' and '{other.__class__.__name__}'"
            )
        return Group('Does not matter', self.people + other.people)

    def __len__(self):
        return len(self.people)
