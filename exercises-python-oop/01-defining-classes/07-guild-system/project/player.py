from project.skill import Skill


class Player:
    name: str
    hp: int
    mp: int
    skills: dict
    guild: str

    NO_GUILD = 'Unaffiliated'

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.NO_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return 'Skill already added'
        self.skills[skill_name] = Skill(skill_name, mana_cost)
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self):
        lines = [
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}",
        ] + [f'==={skill}' for skill in self.skills.values()]

        return '\n'.join(lines) + '\n'  # XXX

    def leave_guild(self):
        self.guild = self.NO_GUILD
