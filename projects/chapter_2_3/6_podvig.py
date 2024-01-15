class FloatValue:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value

class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for _ in range(m)] for _ in range(n)]

table = TableSheet(5, 3)

def alter_table(n, m):
    gen = _get_value()
    
    for i in range(n):
        for j in range(m):
            value = next(gen)
            table.cells[i][j] = Cell(value)

def _get_value():
    return (float(i) for i in range(1, 16))

alter_table(5,3)