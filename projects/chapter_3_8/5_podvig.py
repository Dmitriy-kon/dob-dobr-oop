class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__check_type(value)
        setattr(instance, self.name, value)

    def __check_type(self, value):
        if not isinstance(value, int):
            raise ValueError("возможны только целочисленные значения")


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0) -> None:
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell) -> None:
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cell = cell
        self.__table = tuple(tuple(self.cell() for _ in range(cols)) for _ in range(rows))

    @property
    def cells(self):
        return self.__table
    
    def __check_index(self, row, col):
        if not 0 <= row < self.rows or not 0 <= col < self.cols:
            raise IndexError('неверные индексы')

    def __getitem__(self, index):
        row, col = index
        self.__check_index(row, col)
        return self.__table[row][col].value

    def __setitem__(self, index, value):
        row, col = index
        self.__check_index(row, col)
        self.__table[row][col].value = value
        
table = TableValues(2, 3, cell=CellInteger)
# print(table[0, 1])
table[1, 1] = 10

for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()