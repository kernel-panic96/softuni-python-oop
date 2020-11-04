from typing import List

from project.pokemon import Pokemon


class Trainer:
    name: str
    pokemon: List[Pokemon]

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        for caught_pokemon in self.pokemon:
            if caught_pokemon.name == pokemon.name:
                return 'This pokemon is already caught'

        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str) -> str:
        found_at_index = -1
        for index, pokemon in enumerate(self.pokemon):
            if pokemon.name == pokemon_name:
                found_at_index = index
        if found_at_index == -1:
            return 'Pokemon is not caught'

        self.pokemon.pop(found_at_index)
        return f'You have released {pokemon_name}'

    def trainer_data(self) -> str:
        trainer_lines = [
            f'Pokemon Trainer {self.name}',
            f'Pokemon count {len(self.pokemon)}'
        ]

        all_pokemon_lines = []
        for pokemon in self.pokemon:
            all_pokemon_lines.append(f'- {pokemon.pokemon_details()}')

        return '\n'.join(trainer_lines + all_pokemon_lines)
