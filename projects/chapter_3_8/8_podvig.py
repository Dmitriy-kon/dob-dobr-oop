class Cell:
    def __init__(self) -> None:
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free

    def __repr__(self) -> str:
        return f"Cell({self.value})"


class TicTacToe:
    def __init__(self) -> None:
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for i in self.pole:
            for j in i:
                j.is_free = True
                j.value = 0

    def _check_index(self, indx):
        if isinstance(indx, slice):
            return
        if not 0 <= indx < 3:
            raise IndexError("неверный индекс клетки")

    def __getitem__(self, index):
        all([self._check_index(i) for i in index])
        x, y = index
        res = []

        if isinstance(x, slice):
            for i in self.pole[x]:
                res.append(i[y].value)
            return tuple(res)
        if isinstance(y, slice):
            return tuple(i.value for i in self.pole[x])

        return self.pole[x][y].value

    def __setitem__(self, index, value):
        all([self._check_index(i) for i in index])
        self.pole[index[0]][index[1]].value = value


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()

# for i in g.pole:
#     for j in i:
#         print(j, end=" ")
#     print()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3
# for i in g.pole:
#     for j in i:
#         print(j, end=" ")
#     print()
# print("-" * 25)
# print(g[0, :], g[1, :], g[:, 0], sep="\n")
# exit()
assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"