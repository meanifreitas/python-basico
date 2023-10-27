class Recipe:
    def __init__(self, title, type):
        self.title = title
        self.type = type
        self.ingredients = []
        self.how_to = ""

    def set_ingredients(self):
        while(True):
            ingredient = input("Write QUIT or the ingredient: ")
            if ingredient.upper() == "QUIT":
                break
            self.ingredients.append(ingredient.upper())