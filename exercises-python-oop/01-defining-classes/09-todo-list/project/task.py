from typing import List


class Task:
    name: str
    due_date: str
    comments: List[str]
    completed: bool

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        """Changes the name of the task

        returns the new name.
        returns 'Name cannot be the same.' if the new_name is the same as the current name
        """

        if new_name == self.name:
            return 'Name cannot be the same.'

        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str) -> str:
        """Changes the due date of the task

        returns the new date.
        returns 'Date cannot be the same.' if the new_date is the same as the current date
        """

        if new_date == self.due_date:
            return 'Date cannot be the same.'

        self.due_date = new_date
        return new_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        """Edits a comment.

        returns all of the comments, comma separated ", ".
        returns 'Cannot find comment.' if the comment is not in the task
        """

        if not 0 <= comment_number < len(self.comments):
            return 'Cannot find comment.'

        self.comments[comment_number] = new_comment
        return ', '.join(self.comments)

    def details(self) -> str:
        return f'Name: {self.name} - Due Date: {self.due_date}'
