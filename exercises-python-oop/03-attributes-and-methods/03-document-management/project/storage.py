from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    categories: List[Category]
    topics: List[Topic]
    documents: List[Document]

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category) -> None:
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        [t for t in self.topics if t.id == topic_id][0].edit(new_topic, new_storage_folder)

    def edit_category(self, category_id: int, new_name: str) -> None:
        [c for c in self.categories if c.id == category_id][0].edit(new_name)

    def edit_document(self, document_id: int, new_file_name: str):
        [d for d in self.documents if d.id == document_id][0].edit(new_file_name)

    def delete_category(self, category_id: int):
        self.categories.remove([c for c in self.categories if c.id == category_id][0])

    def delete_topic(self, topic_id: int):
        self.topics.remove([t for t in self.topics if t.id == topic_id][0])

    def delete_document(self, document_id: int):
        self.documents.remove([d for d in self.documents if d.id == document_id][0])

    def get_document(self, document_id: int):
        return [d for d in self.documents if d.id == document_id][0]

    def __repr__(self):
        return '\n'.join(repr(d) for d in self.documents)
