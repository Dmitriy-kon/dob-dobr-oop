class Dimensions:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.check_dimensions()
    
    def check_dimensions(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
    
    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)
    
    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))
    
    def __repr__(self) -> str:
        return f"{hash(self)}"

s_inp = input() 

spam = s_inp.split("; ")
spam = [[int(j) if "." not in j else float(j) for j in i.split()] for i in spam]
lst_dims = sorted([Dimensions(*i) for i in spam], key=hash)
print(lst_dims)