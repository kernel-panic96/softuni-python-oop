from typing import List

from project.task import Task


class Section:
    """The Section class is a container for various tasks and aids in managing them"""

    name: str
    tasks: List[Task]

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        """Adds a task to the section.

        returns - Task <task details> is added to the section
        returns 'Task is already in the section <section name>' if the tasks already is in the section
        """

        if new_task.name in [t.name for t in self.tasks]:
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str) -> str:
        """Completes a task from the section.

        returns - Completed task <task name>
        returns 'Could not find task with the name <task name>' if the task is not in the section
        """

        task_names = [t.name for t in self.tasks]

        if task_name not in task_names:
            return f'Could not find task with the name {task_name}'

        task = self.tasks[task_names.index(task_name)]
        task.completed = True
        return f'Completed task {task.name}'

    def clean_section(self) -> str:
        """Removes all *completed* tasks from the section.

        returns - 'Cleared <number of tasks that got cleared>'
        """
        amount_of_tasks = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f'Cleared {amount_of_tasks - len(self.tasks)} tasks.'

    def view_section(self) -> str:
        """Returns a string representation of the section and it's tasks."""

        return f'Section {self.name}:\n' + '\n'.join(
            [t.details() for t in self.tasks]
        )
