class Skill:
    name: str
    mana_cost: int

    def __init__(self, name: str, mana_cost: int):
        self.name = name
        self.mana_cost = mana_cost

    def __str__(self):
        return f'{self.name} - {self.mana_cost}'
