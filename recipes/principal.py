from recipe import Recipe
from type import Type

dessert = Type("Dessert", "Sweet")
recipe1 = Recipe("Cake", dessert)
recipe1.set_ingredients()