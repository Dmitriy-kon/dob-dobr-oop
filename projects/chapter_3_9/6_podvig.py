class TriangleListIterator:
    def __init__(self, lst=None) -> None:
        if lst is None:
            self.lst = []
        else:
            self.lst = list(lst)

        self._row = 0
        self._stop = 1
        self._cur = 0

    def __iter__(self):
        return (self)

    def __next__(self):
        if self._cur == self._stop:
            self._row += 1
            self._stop += 1
            self._cur = 0

        if self._cur < self._stop and self._row < len(self.lst):
            res = self.lst[self._row][self._cur]
            self._cur += 1
            return res
        else:
            self._row = 0
            self._stop = 1
            self._cur = 0
            raise StopIteration


    # def __iter__(self):
    #     for i in range(len(self.lst)):
    #         for j in range(i+1):
    #             yield self.lst[i][j]
    
# triangle_lst = [
#     ["x00"],
#     ["x10", "x11"],
#     ["x20", "x21", "x22"],
#     ["x30", "x31", "x32", "x33"],
# ]
# square_lst = [
#     ["x00", "x01", "x02", "x03"],
#     ["x10", "x11", "x12", "x13"],
#     ["x20", "x21", "x22", "x23"],
#     ["x30", "x31", "x32", "x33"],
# ]
# linear_lst = ["x00", "x10", "x11", "x20", "x21", "x22", "x30", "x31", "x32", "x33"]
# it_1 = TriangleListIterator(triangle_lst)
# it_2 = TriangleListIterator(square_lst)
# for i in it_2:
#     print(i, end=" ")
# print()
# print(*linear_lst, sep=" ")


# exit()

# Test 1
triangle_lst = [
    ["x00"],
    ["x10", "x11"],
    ["x20", "x21", "x22"],
    ["x30", "x31", "x32", "x33"],
]
linear_lst = ["x00", "x10", "x11", "x20", "x21", "x22", "x30", "x31", "x32", "x33"]
it_1 = TriangleListIterator(triangle_lst)
test1 = [x for x in it_1]
assert test1 == linear_lst, f"Incorrect result - {test1}"

# Test 2
it_2 = iter(TriangleListIterator(triangle_lst))
test2 = [next(it_2) for _ in range(len(linear_lst))]
assert test2 == linear_lst, f"Incorrect result - {test2}"

# Test 3
square_lst = [
    ["x00", "x01", "x02", "x03"],
    ["x10", "x11", "x12", "x13"],
    ["x20", "x21", "x22", "x23"],
    ["x30", "x31", "x32", "x33"],
]
it_3 = TriangleListIterator(square_lst)
test3 = [x for x in it_3]
assert test3 == linear_lst, f"Incorrect result - {test3}"

# Test 4
incorrect_lst = [
    ["x00", "x01", "x02", "x03"],
    ["x10"],
    ["x20", "x21"],
    ["x30", "x31", "x32", "x33"],
]
it_4, flag = TriangleListIterator(incorrect_lst), False
try:
    test4 = [x for x in it_4]
except IndexError:
    flag = True
finally:
    assert flag, "Waited IndexError"

# Test 5
triangle_lst = [
    ["x00"],
    ["x10", "x11"],
    ["x20", "x21", "x22"],
    ["x30", "x31", "x32", "x33"],
]
it_5 = TriangleListIterator(triangle_lst)
t_5_1 = [x for x in it_5]
t_5_2 = [x for x in it_5]
print(t_5_1, t_5_2, sep="\n")
assert (
    t_5_1 == t_5_2 == linear_lst
), f"Incorrect result - {t_5_1}, {t_5_2}. Reinit attrs."
