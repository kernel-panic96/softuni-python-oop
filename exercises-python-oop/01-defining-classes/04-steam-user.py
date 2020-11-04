# TODO: cleaner error handling TODO: don't return different types
# TODO: without self


class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f'{self.username} is playing {game}'

        return f'{game} is not in library'

    def buy_game(self, game):
        if game in self.games:
            return f'{game} is already in your library'

        self.games.append(game)
        return f'{self.username} bought {game}'

    def stats(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'

# early return
me = SteamUser('Curious', ['Diablo', 'Counter-Strike', "Sid Meier's Civilizations VI"])
print(me.play('Minecraft', 2))
print(me.played_hours)
print(me.buy_game('Minecraft'))
print(me.play('Minecraft', 2))
print(me.played_hours)
print(me.stats())
