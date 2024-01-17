from typing import Any

class Dimensions:
    attrs = ("MIN_DIMENSION", "MAX_DIMENSION")

    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __verify_value(cls, value):
        return (
            type(value) in (int, float)
            and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
        )

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @a.setter
    def a(self, new_a):
        if self.__verify_value(new_a):
            self.__a = new_a

    @b.setter
    def b(self, new_b):
        if self.__verify_value(new_b):
            self.__b = new_b

    @c.setter
    def c(self, new_c):
        if self.__verify_value(new_c):
            self.__c = new_c

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.attrs:
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено."
            )
        super().__setattr__(key, value)
