class CoordDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        res = {type(i) for i in value}
        if res <= {int, float}:
            setattr(instance, self.name, value)


class RadiusVector:
    coords = CoordDescriptor()

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.coords = [0 for _ in range(args[0])]
        else:
            self.coords = list(args)

    def set_coords(self, *args):
        try:
            for index, i in enumerate(args):
                self.coords[index] = i
        except IndexError:
            return

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        spam = 0
        for i in self.coords:
            spam += i * i
        return spam**0.5
