from typing import Any, List

from project.category import Category
from project.topic import Topic


class Document:
    id: int
    category_id: int
    topic_id: int
    file_name: str
    tags: List[str]

    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str) -> 'Document':
        return cls(
            id,
            category_id=category.id,
            topic_id=topic.id,
            file_name=file_name
        )

    # NOTE(yavor): This has a failure scenario which is being silenced.
    # Silencing errors is generally not good, top level code should
    # determine whether to silence or not. Handling of errors should be separate
    def add_tag(self, tag_content: str) -> None:
        if tag_content in self.tags:
            return
        self.tags.append(tag_content)

    # NOTE(yavor): same as `add_tag` note
    def remove_tag(self, tag_content: str) -> None:
        if tag_content not in self.tags:
            return
        self.tags.remove(tag_content)

    def edit(self, file_name: str) -> None:
        self.file_name = file_name

    def __repr__(self):
        tags = ', '.join(self.tags)
        return f'Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {tags}'
