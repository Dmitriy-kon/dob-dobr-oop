from typing import Any


class Circle:
    keys = {"x": (int, float), "y": (int, float), "radius": (int, float)}

    def __init__(self, x, y, radius) -> None:
        self.__x = self.__y = self.__radius = None
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        self.__y = new_y

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.keys and type(value) not in self.keys[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == "radius" and value <= 0:
            return
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False
