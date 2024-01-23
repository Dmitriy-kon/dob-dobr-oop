from math import sqrt
from typing import Any


class TriangleLength:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)

    def verify_value(self, value):
        if not isinstance(value, (int, float)) and value <= 0:
            raise ValueError("Длина стороны треугольника должна быть положительной")


class Triangle:
    a, b, c = TriangleLength(), TriangleLength(), TriangleLength()

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    #     self.verify_triangle(self.a, self.b, self.c)

    # def verify_triangle(self, a, b, c):
    #     if a > b + c or b > a + c or c > a + b:
    #         raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        if self.a and self.b and self.c:
            return int(self.a + self.b + self.c)

    def __call__(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __setattr__(self, key, value) -> None:
        if (key == "a" and not self.__is_triangle(value, self.b, self.c) or \
            key == "b" and not self.__is_triangle(self.a, value, self.c) or \
            key == "c" and not self.__is_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)
    
    @staticmethod
    def __is_triangle(a, b, c):
        if a and b and c:
            return a< b + c and b < a + c and c < a + b
        return True
        


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
tr = Triangle(3.4, 4, 5)
print(len(tr))
print(tr())
assert 6.7 < tr() < 6.8, "метод __call__ вернул не верное значение для треугольника со сторонами (3.4, 4, 5)"