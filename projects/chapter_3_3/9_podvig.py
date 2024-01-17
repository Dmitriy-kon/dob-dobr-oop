class Ingridient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        self.recipes = list(args)

    def add_ingredient(self, ing):
        self.recipes.append(ing)

    def remove_ingredient(self, ing):
        self.recipes.remove(ing)

    def get_ingredients(self):
        return tuple(self.recipes)

    def __len__(self):
        return len(self.recipes)
