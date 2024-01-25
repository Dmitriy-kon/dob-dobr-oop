class Track:
    def __init__(self, start_x, start_y) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self._track = []

    def add_point(self, x, y, speed):
        self._track.append([(x, y), speed])

    def __check_index(self, indx):
        if not 0 <= indx <= len(self) - 1:
            raise IndexError("некорректный индекс")

    def __getitem__(self, index):
        self.__check_index(index)
        return self._track[index]

    def __setitem__(self, index, value):
        self.__check_index(index)
        self._track[index][1] = value

    def __len__(self):
        return len(self._track)

    def get_points(self):
        return self._track


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError