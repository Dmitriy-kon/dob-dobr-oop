data = [
    "Python; Балакирев С.М.; 2020",
    "Python ООП; Балакирев С.М.; 2021",
    "Python ООП; Балакирев С.М.; 2022",
    "Python; Балакирев С.М.; 2021",
]


class BookStudy:
    def __init__(self, name, author, year) -> None:
        self.__name = name
        self.__author = author
        self.__year = year
    
    @property
    def name(self):
        return self.__name
    
    @property
    def author(self):
        return self.__author
    
    @property
    def year(self):
        return self.__year
    
    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)
    
    def __hash__(self) -> int:
        return hash((self.name.lower(), self.author.lower()))
    
    def __repr__(self) -> str:
        return f"BookStudy({self.name}, {self.author}, {self.year})"

lst_bs = []
lst_bs2 = [BookStudy(*i.split("; ")) for i in data]
for i in data:
    name, author, year = i.split("; ")
    obj = BookStudy(name, author, int(year))
    lst_bs.append(obj)

# unique_books  = len(set(lst_bs))
print(lst_bs2)