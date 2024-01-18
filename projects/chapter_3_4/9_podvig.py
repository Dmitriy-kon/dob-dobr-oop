class Box3D:
    def __init__(self, width, height, depth) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if isinstance(other, Box3D):
            return Box3D(
                self.width + other.width,
                self.height + other.height,
                self.depth + other.depth,
            )

    def __mul__(self, other: int):
        res = Box3D(self.width * other, self.height * other, self.depth * other)
        return res

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(
                self.width - other.width,
                self.height - other.height,
                self.depth - other.depth,
            )

    def __floordiv__(self, other):
        if isinstance(other, int):
            return Box3D(
                self.width // other,
                self.height // other,
                self.depth // other,
            )

    def __mod__(self, other):
        if isinstance(other, int):
            return Box3D(
                self.width % other,
                self.height % other,
                self.depth % other,
            )
