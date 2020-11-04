from project.pokemon import Pokemon
from project.trainer import Trainer


pokemon = Pokemon("Pikachu", 90)
pokemon2 = Pokemon("Pikachu2", 90)
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
print(trainer.add_pokemon(pokemon2))
print(trainer.trainer_data())
