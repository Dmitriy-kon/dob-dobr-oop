class Ellipse:
    def __init__(self, x1=None, x2=None, y1=None, y2=None) -> None:
        if x1 and x2 and y1 and y2:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2

    def __bool__(self):
        return all(map(lambda x: x in vars(self), ("x1", "y1", "x2", "y2")))

    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x1, self.y2
        raise AttributeError("нет координат для извлечения")


el1 = Ellipse()
el2 = Ellipse()
el3 = Ellipse(1, 2, 3, 4)
el4 = Ellipse(2, 3, 4, 5)

lst_geom = [el1, el2, el3, el4]
[geom.get_coords() for geom in lst_geom if geom]

for i in lst_geom:
    if i:
        i.get_coords()
# lst_geom = [i.get_coords() for i in lst_geom if bool(i)]

print(lst_geom)

exit()


class Ellipse:
    __slots__ = ("x1", "y1", "x2", "y2")

    def __init__(self, *args):
        [
            setattr(self, name, args[id])
            for id, name in enumerate(self.__slots__)
            if len(args) == len(self.__slots__)
        ]

    def __bool__(self):
        return all(
            map(
                lambda v: isinstance(v, int),
                (getattr(self, name, None) for name in self.__slots__),
            )
        )

    def get_coords(self):
        if self:
            return self.x1, self.x2, self.y1, self.y2
        raise AttributeError("нет координат для извлечения")


lst_geom = [Ellipse(*params) for params in ((), (), (1, 2, 3, 4), (9, 8, 7, 6))]
[geom.get_coords() for geom in lst_geom if geom]
