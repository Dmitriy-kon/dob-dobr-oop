from typing import Any


class WordString:
    def __init__(self, string=None):
        self.__string: str = string

    def __len__(self):
        return len(self.string.split())

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        indx, *_ = args
        return self.string.split()[indx]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
