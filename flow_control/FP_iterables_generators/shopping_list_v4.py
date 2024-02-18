"""
This is a lazy implementation of the ShoppingList __iter__ method using generators
"""

import re
import reprlib


class ShoppingList:
    def __init__(self, ingredient_str):
        self.ingredient_str = ingredient_str
        # self.ingredients = re.split(', ', ingredient_str)

    def __repr__(self):
        return f"ShoppingList({reprlib.repr(self.ingredient_str)})"

    def __iter__(self):
        for ingredient in re.split(', ', self.ingredient_str):
            yield ingredient


if __name__=='__main__':
    shopping_list = ShoppingList('banana, red onion, garlic, beans, almonds, yogurt')
    print('shopping_list: ', shopping_list)
    it = iter(shopping_list)
    for i in it:
        print(i)
    print('list of used up iterator: ', list(it))
    print('list of new iterator: ', list(iter(shopping_list)))
