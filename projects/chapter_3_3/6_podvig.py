from math import sqrt


class Complex:
    def __init__(self, real, img) -> None:
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, new_real):
        if type(new_real) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__real = new_real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, new_img):
        if type(new_img) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__img = new_img

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)
