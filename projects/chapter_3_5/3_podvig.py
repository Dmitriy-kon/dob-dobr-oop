import functools
from math import sqrt


class TrackLine:
    def __init__(self, to_x, to_y, max_speed) -> None:
        self._to_x = to_x
        self._to_y = to_y
        self._max_speed = max_speed

    @property
    def x(self):
        return self._to_x

    @property
    def y(self):
        return self._to_y

    @property
    def max_speed(self):
        return self._max_speed


class Track:
    def __init__(self, start_x, start_y) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self._tracks = list()

    def add_track(self, tr: TrackLine):
        self._tracks.append(tr)

    def get_tracks(self):
        return self._tracks

    def __eq__(self, other) -> bool:
        return len(self) == len(other)

    def __lt__(self, other) -> bool:
        return len(self) < len(other)

    def __len__(self):
        len_1 = (
            (self.start_x - self._tracks[0].x) ** 2
            + (self.start_y - self._tracks[0].y) ** 2
        ) ** 0.5
        return int(
            len_1 + sum(self.__get_lenth(i) for i in range(1, len(self._tracks)))
        )

    def __get_lenth(self, i):
        return (
            (self._tracks[i - 1].x - self._tracks[i].x) ** 2
            + (self._tracks[i - 1].y - self._tracks[i].y) ** 2
        ) ** 0.5

    def __str__(self) -> str:
        return "".join(f"{i.to_x}, {i.to_y}" for i in self.get_tracks())
