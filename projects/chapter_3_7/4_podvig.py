lst_in = [
    "Балакирев; 34; 2048",
    "Mediel; 27; 0",
    "Влад; 18; 9012",
    "Nina P; 33; 0",
]


class Player:
    def __init__(self, name, old, score) -> None:
        self.__name = name
        self.__old = int(old)
        self.__score = int(score)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, value):
        self.__old = value
        
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value

    def __bool__(self):
        return self.score > 0
    def __repr__(self) -> str:
        return f"Player({self.name}, {self.old}, {self.score})"


players = [Player(*i.split("; ")) for i in lst_in]
players_filtered = list(filter(bool, players))

print(players)
print(players_filtered)
