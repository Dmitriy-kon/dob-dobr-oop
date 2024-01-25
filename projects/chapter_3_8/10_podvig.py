class Cell:
    def __init__(self, value) -> None:
        self.value = value


class Sparsetable:
    def __init__(self) -> None:
        self.rows = self.cols = 0
        self.table = {}

    # def _check_index(self, row, col):
    #     if not 0 <= row < self.rows or not 0 <= col < self.cols:
    #         raise IndexError("ячейка с указанными индексами не существует")

    def update_index(self):
        self.rows = max(key[0] for key in self.table) + 1
        self.cols = max(key[1] for key in self.table) + 1

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        try:
            del self.table[(row, col)]
            self.update_index()

        except KeyError:
            raise IndexError("ячейка с указанными индексами не существует")

    def __getitem__(self, item):
        try:
            return self.table[(item[0], item[1])].value
        except KeyError:
            raise ValueError("данные по указанным индексам отсутствуют")

    def __setitem__(self, key, value):
        item = (key[0], key[1])

        if item not in self.table:
            self.table[item] = Cell(value)
            self.update_index()
        else:
            self.table[item] = Cell(value)
