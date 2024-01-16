from typing import Any


class Book:

    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ("title", "author") and isinstance(__value, str):
            super().__setattr__(__name, __value)
        elif __name in ("pages", "year") and isinstance(__value, int):
            super().__setattr__(__name, __value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
print(book.__dict__)