from typing import List

from project.song import Song


class Album:
    name: str
    songs: List[Song]
    published: bool

    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song.name in [s.name for s in self.songs]:
            return 'Song is already in the album.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str) -> str:
        song_names = [s.name for s in self.songs]
        if song_name not in song_names:
            return 'Song is not in the album.'
        if self.published:
            return 'Cannot remove songs. Album is published.'

        del self.songs[song_names.index(song_name)]
        return f'Removed song {song_name} from album {self.name}.'

    def publish(self) -> str:
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self) -> str:
        return f'Album {self.name}\n' + '\n'.join(
            ['== ' + s.get_info() for s in self.songs])
