from typing import List

from project.player import Player


class Guild:
    name: str
    players: List[Player]

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f'Player {player.name} is already in the guild.'
        if player.guild != Player.NO_GUILD:
            return f'Player {player.name} is in another guild.'

        player.guild = self.name
        self.players.append(player)
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str) -> str:
        guild_members_names = [p.name for p in self.players]
        if player_name not in guild_members_names:
            return f'Player {player_name} is not in the guild.'

        player_idx = guild_members_names.index(player_name)
        player = self.players[player_idx]

        # player.leave_guild()   # XXX
        self.players.remove(player)
        return f'Player {player.name} has been removed from the guild.'

    def guild_info(self):
        # XXX DOES NOT WORK
        # return '\n'.join([
        #     f'Guild: {self.name}',
        # ] + [
        #     p.player_info() for p in self.players
        # ])
        return f'Guild: {self.name}\n' + '\n'.join(
            [p.player_info() for p in self.players])
