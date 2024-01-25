class RadiusVector:
    def __init__(self, *args) -> None:
        self.coords = list(args)

    def __getitem__(self, index):
        return tuple(self.coords[index]) if isinstance(index, slice) else self.coords[index]

    
    def __setitem__(self, index, value):
        self.coords[index] = tuple(value) if isinstance(index, slice) else value


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[:])
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5
print(v[:])