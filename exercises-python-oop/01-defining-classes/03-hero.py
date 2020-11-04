class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health = max(0, self.health - damage)

        if self.health == 0:
            return f'{self.name} was defeated'

    def heal(self, amount):
        if self.health == 0:
            return

        self.health += amount


hero = Hero('Peter', 100)
print(hero.defend(100))
print(hero.defend(100))
print(hero.heal(100))
print(hero.health)
