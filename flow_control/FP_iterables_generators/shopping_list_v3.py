"""
This is an example of iterables, iterators and generators in python.
"""

import re
import reprlib

# RE_INGREDIENT = re.compile(',+')


class ShoppingList:
    '''This is a shopping list with a generator function.'''
    def __init__(self, ingredient_str):
        self.ingredient_str = ingredient_str
        self.ingredients = re.split(', ', ingredient_str)

    def __repr__(self):
        return f"ShoppingList({reprlib.repr(self.ingredient_str)})"

    def __iter__(self):
        for ingredient in self.ingredients:
            yield ingredient
        return




if __name__=='__main__':
    shopping_list = ShoppingList('banana, red onion, garlic, beans, almonds, yogurt')
    print('shopping_list: ', shopping_list)
    it = iter(shopping_list)
    for i in it:
        print(i)
    print('list of used up iterator: ', list(it))
    print('list of new iterator: ', list(iter(shopping_list)))
