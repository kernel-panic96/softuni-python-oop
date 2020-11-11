from project import *


animals = [
    Animal('animal'),
    Reptile('reptile'),
    Mammal('mammal'),
    Lizard('lizard'),
    Snake('snake'),
    Gorilla('gorilla'),
    Bear('bear')
]

for a in animals:
    print(a.__dict__)
    print(a.name)