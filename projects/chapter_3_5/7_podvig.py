from typing import Any


filenames = [
    "boat.jpg",
    "ans.web.png",
    "text.txt",
    "www.python.doc",
    "my.ava.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.xls",
]


class FileAcceptor:
    def __init__(self, *args) -> None:
        self.ext = args

    def __call__(self, filename) -> Any:
        return filename.lower().endswith(self.ext)

    def __add__(self, other) -> Any:
        return FileAcceptor(*self.ext, *other.ext)
