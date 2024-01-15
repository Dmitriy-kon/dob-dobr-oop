class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x, y) -> None:
        if self.__validate_data(x):
            self.__x = x
        else:
            self.__x = 0

        if self.__validate_data(y):
            self.__y = y
        else:
            self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if self.__validate_data(new_x):
            self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if self.__validate_data(new_y):
            self.__y = new_y

    def norm2(vector):
        return vector.x**2 + vector.y**2

    @classmethod
    def __validate_data(cls, data):
        return type(data) in {int, float} and cls.MIN_COORD <= data <= cls.MAX_COORD
