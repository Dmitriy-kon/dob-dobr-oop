from typing import Any

class Book:
    _validate = {"title": str, "author": str, "pages": int}

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self._validate and isinstance(__value, self._validate[__name]):
            super().__setattr__(__name, __value)

    def __str__(self) -> str:
        return f"Книга: {self.title}; {self.author}; {self.pages}"
