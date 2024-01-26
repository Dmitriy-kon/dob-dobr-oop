import pytest


class Matrix:
    def __init__(self, rows, cols=None, fill_value=None, table=None) -> None:
        if isinstance(rows, list):
            self.rows = len(rows)
            self.cols = len(rows[0])
            self.__check_squere(rows)
            self.table = rows

        else:
            if (
                not isinstance(rows, int)
                or not isinstance(cols, int)
                or not isinstance(fill_value, (int, float))
            ):
                raise TypeError(
                    "аргументы rows, cols - целые числа; fill_value - произвольное число"
                )

            self.rows = rows
            self.cols = cols
            self.fill_value = fill_value
            self.table = [[self.fill_value for _ in range(cols)] for _ in range(rows)]

    def __check_type(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("значения матрицы должны быть числами")

    def __check_squere(self, lst):
        if not all(len(r) == self.cols for r in lst) or not all(
            self.__is_digit(x) for row in lst for x in row
        ):
            raise TypeError("список должен быть прямоугольным, состоящим из чисел")
        # for i in lst:
        #     if self.cols != len(i) or not all([isinstance(j, (int, float)) for j in i]):
        #         raise TypeError("список должен быть прямоугольным, состоящим из чисел")

    def __is_digit(self, x):
        return isinstance(x, (int, float))

    def __check_index(self, row, col):
        if not (0 <= row < self.rows) or (not 0 <= col < self.cols):
            raise IndexError("недопустимые значения индексов")

    def __getitem__(self, item):
        row, col = item
        self.__check_index(row, col)
        return self.table[row][col]

    def __setitem__(self, key, value):
        row, col = key
        self.__check_index(row, col)
        self.__check_type(value)
        self.table[row][col] = value

    def __add__(self, other):
        if isinstance(other, int):
            return Matrix(
                [
                    [self[i, j] + other for j in range(self.cols)]
                    for i in range(self.rows)
                ],
            )
            self.table = [[i + other for i in j] for j in self.table]
            return Matrix(
                rows=self.rows,
                cols=self.cols,
                fill_value=self.fill_value,
                table=self.table,
            )
        if isinstance(other, Matrix):
            self.__check_matrix_size(other)
            return Matrix(
                [
                    [self[i, j] + other[i, j] for j in range(self.cols)]
                    for i in range(self.rows)
                ],
            )
            new_table = [
                [k + h for k, h in zip(i, j)] for i, j in zip(self.table, other.table)
            ]
            return Matrix(
                rows=self.rows,
                cols=self.cols,
                fill_value=self.fill_value,
                table=new_table,
            )

    def __sub__(self, other):
        if isinstance(other, int):
            return Matrix(
                [
                    [self[i, j] - other for j in range(self.cols)]
                    for i in range(self.rows)
                ],
            )
            self.table = [[i - other for i in j] for j in self.table]
            return Matrix(
                rows=self.rows,
                cols=self.cols,
                fill_value=self.fill_value,
                table=self.table,
            )
        if isinstance(other, Matrix):
            self.__check_matrix_size(other)
            return Matrix(
                [
                    [self[i, j] - other[i, j] for j in range(self.cols)]
                    for i in range(self.rows)
                ],
            )
            new_table = [
                [k - h for k, h in zip(i, j)] for i, j in zip(self.table, other.table)
            ]
            return Matrix(
                rows=self.rows,
                cols=self.cols,
                fill_value=self.fill_value,
                table=new_table,
            )

    def __check_matrix_size(self, matrix):
        rows, cols = matrix.rows, matrix.cols
        if self.rows != rows or self.cols != cols:
            raise ValueError("операции возможны только с матрицами равных размеров")

        # if self.__get_matrix_size(matrix) != self.__get_matrix_size(self):
        #     raise ValueError("операции возможны только с матрицами равных размеров")

    def __get_matrix_size(self, matrix):
        row = len(matrix.table)
        col = len(matrix.table[0])
        return row, col

    def __iter__(self):
        return ((f"{j}".ljust(3) for j in i) for i in self.table)


flag = False
# todo Test 1 - check init attrs

# Positive checks
try:
    mt = Matrix(2, 3, -45)
    flag = True
except TypeError:
    flag = False
finally:
    assert flag, "If raised TypeError exception then invalid validations"
    flag = False

try:
    mt = Matrix([[-45, -45], [-45, -45]])
    flag = True
except TypeError:
    flag = False
finally:
    assert flag, "If raised TypeError exception then invalid validations"
    flag = False

# Negative checks
try:
    mt = Matrix("2", 3, -45)
except TypeError:
    flag = True
finally:
    assert flag, "Not raised TypeError with incorrect attrs"
    flag = False

try:
    mt = Matrix([[10, 10], ["10", 10]])
except TypeError:
    flag = True
finally:
    assert flag, "Not raised TypeError with incorrect fill_value"
    flag = False


# todo Test 2 - check get/set dunder methods

# Positive checks
try:
    assert (
        mt[0, 0] == -45
    ), "Wrong number. Incorrect matrix structure or mixed up row and col, should be -45"
    mt[0, 0] = 10
    assert (
        mt[0, 0] == 10
    ), "Wrong number. Incorrect matrix structure or mixed up row and col, should be 10"
    mt[0, 1] = 1.7
    assert (
        mt[0, 1] == 1.7
    ), "Wrong number. Incorrect matrix structure or mixed up row and col, should be 1.7"
    flag = True
except (IndexError, TypeError):
    flag = False
finally:
    assert flag, "If raised IndexError or TypeError exception then invalid validations"
    flag = False

# Negative checks
try:
    print(mt[-1, 0])
except IndexError:
    flag = True
finally:
    assert flag, "Not raised IndexError with incorrect first index"
    flag = False

try:
    mt[0, 0] = "1"
except TypeError:
    flag = True
finally:
    assert flag, "Not raised TypeError with incorrect input value"
    flag = False


# todo Test 3 - check operations with matrix and numbers +/-

# Positive checks
mt_1 = Matrix(2, 2, 2)
mt_2 = Matrix(2, 2, 2)

try:
    op_add = mt_1 + mt_2
    assert op_add.matrix == [
        [4, 4],
        [4, 4],
    ], f"Incorrect matrix with op_add - {op_add.matrix}"
    op_sub = mt_1 - mt_2
    assert op_sub.matrix == [
        [0, 0],
        [0, 0],
    ], f"Incorrect matrix with op_sub - {op_sub.matrix}"
    op_add_num = mt_1 + 3
    assert op_add_num.matrix == [
        [5, 5],
        [5, 5],
    ], f"Incorrect matrix with op_add_num - {op_add_num.matrix}"
    op_sub_num = mt_1 - 3
    assert op_sub_num.matrix == [
        [-1, -1],
        [-1, -1],
    ], f"Incorrect matrix with op_sub_num - {op_sub_num.matrix}"
    flag = True
except ValueError:
    flag = False
finally:
    assert flag, "If raised ValueError exception then invalid validations"
    flag = False

# Negative checks
mt_1 = Matrix(2, 2, 2)
mt_2 = Matrix(2, 4, 2)

try:
    op_add_fail = mt_1 + mt_2
except ValueError:
    flag = True
finally:
    assert flag, "Not raised ValueError because different in dimensions of matrix"
    flag = False
