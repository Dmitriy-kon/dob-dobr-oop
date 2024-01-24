class Vector:
    def __init__(self, *args) -> None:
        self.vec = args

    def __len__(self):
        return len(self.vec)

    def __check_lenth(self, other):
        if len(self) != len(other):
            raise ArithmeticError("размерности векторов не совпадают")

    def __add__(self, other):
        self.__check_lenth(other)
        return Vector(*map(lambda x, y: x + y, self.vec, other.vec))

    def __sub__(self, other):
        self.__check_lenth(other)
        return Vector(*map(lambda x, y: x - y, self.vec, other.vec))

    def __mull__(self, other):
        self.__check_lenth(other)
        return Vector(*map(lambda x, y: x * y, self.vec, other.vec))

    def __iadd__(self, other):
        if isinstance(other, int):
            self.vec = [x + other for x in self.vec]
        elif isinstance(other, Vector):
            self.vec = [x + y for x, y in zip(self.vec, other.vec)]
        return self
    
    def __isub__(self, other):
        if isinstance(other, int):
            self.vec = [x - other for x in self.vec]
        elif isinstance(other, Vector):
            self.vec = [x - y for x, y in zip(self.vec, other.vec)]
        return self
    
    def __eq__(self, other):
        return all([i == j for i, j in zip(self.vec, other.vec)])
