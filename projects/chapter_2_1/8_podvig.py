class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if all([isinstance(i, Point) for i in args]):
            self.__sp = args[0]
            self.__ep = args[1]
            
        elif all(map(lambda x: type(x) in (int, float), args)):
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep
    
    def get_coords(self):
        return self.__sp, self.__ep
    
    def draw(self):
        x1, y1 = self.get_coords()[0]
        x2, y2 = self.get_coords()[1]
        print(f'Прямоугольник с координатами: ({x1}, {y1}) ({x2}, {y2})')

rect = Rectangle(0, 0, 20, 34)