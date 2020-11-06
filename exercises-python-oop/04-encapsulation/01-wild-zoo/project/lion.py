class Lion:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    @classmethod
    def get_needs(cls):
        return 50

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'
