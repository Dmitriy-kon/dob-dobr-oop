from typing import Any


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


class Module:
    def __init__(self, name) -> None:
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    def __init__(self, title, practices, duration) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "title" and isinstance(__value, str):
            super().__setattr__(__name, __value)
        elif __name in ("duration", "practices") and isinstance(__value, int):
            super().__setattr__(__name, __value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, __name: str) -> None:
        if __name in ("duration", "title", "practices"):
            raise AttributeError("Атрибут duration удалять запрещено.")

        super().__delattr__(__name)
    
    def __getattr__(self, __name: str) -> Any:
        return False
