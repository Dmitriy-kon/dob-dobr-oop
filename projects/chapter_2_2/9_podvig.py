class LineTo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *paths) -> None:
        self.paths = list((LineTo(0, 0),) + paths)

    def get_path(self):
        if self.paths:
            return self.paths[1:]
        return []
    
    def get_length(self):
        g = ((self.paths[i - 1], self.paths[i]) for i in range(1, len(self.paths)))
        return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g))
    
    def add_line(self, line):
        self.paths.append(line)
        