import math
from typing import ClassVar, List


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE: ClassVar[int] = 4
    pages: int
    photos: List[List[str]]

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        return cls(math.ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page_idx, page in enumerate(self.photos):
            if len(page) == self.MAX_PHOTOS_PER_PAGE:
                continue
            page.append(label)
            return f'{label} photo added successfully on page {page_idx+1} slot {len(page)}'
        return 'No more free spots'

    def display(self):
        pages = [('[] ' * len(page)).rstrip(' ') + '\n' for page in self.photos]
        delim = '-' * 11 + '\n'

        return delim + (delim).join(pages) + delim


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
