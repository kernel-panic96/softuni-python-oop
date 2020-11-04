# TODO: typing, the problem definitions have types sooo show typing


class Programmer:
    def __init__(self, name: str, language: str, skills: int) -> None:
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        if language != self.language:
            return f'{self.name} does not know {language}'

        self.skills += skills_earned
        return f'{self.name} watched {course_name}'

    def change_language(self, new_language: str, skills_needed: int):
        if self.skills < skills_needed:
            return f'{self.name} needs {skills_needed - self.skills} more skills'

        if new_language != self.language:
            self.language, old_language = new_language, self.language
            return f'{self.name} switched from {old_language} to {new_language}'

        return f'{self.name} already knows {new_language}'


programmer = Programmer('Yavor Lulchev', 'Python', 80)
# print(programmer.change_language('Haskell', 70))
# print(programmer.language)
