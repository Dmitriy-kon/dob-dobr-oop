class Record:
    def __init__(self, **kwargs) -> None:
        for i, j in kwargs.items():
            setattr(self, i, j)

    def __getitem__(self, index):
        if isinstance(index, int) or 0 <= index <= len(self):
            for inx, i in enumerate(vars(self)):
                if inx == index:
                    return getattr(self, i)
        raise IndexError("неверный индекс поля")

    def __setitem__(self, index, value):
        if isinstance(index, int) or 0 <= index <= len(self):
            for inx, i in enumerate(vars(self)):
                if inx == index:
                    return setattr(self, i, value)
        raise IndexError("неверный индекс поля")

    def __len__(self):
        return len(vars(self))


r = Record(pk=1, title="Python ООП", author="Балакирев")
print(r[1])
r[1] = 21
print(vars(r))
