"""
This is an example of iterables and iterators in python.
"""

import re
import reprlib

# RE_INGREDIENT = re.compile(',+')


class ShoppingList:
    '''This is a shopping list with iterator and this is the classic iterator design pattern.'''
    def __init__(self, ingredient_str):
        self.ingredient_str = ingredient_str
        self.ingredients = re.split(', ', ingredient_str)

    def __repr__(self):
        return f"ShoppingList({reprlib.repr(self.ingredient_str)})"

    def __iter__(self):
        return ShoppingListIterator(self.ingredients)


class ShoppingListIterator:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.index = 0

    def __next__(self):
        try:
            ingredient = self.ingredients[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return ingredient

    def __iter__(self):
        return self



if __name__=='__main__':
    shopping_list = ShoppingList('banana, red onion, garlic, beans, almonds, yogurt')
    print('shopping_list: ', shopping_list)
    it = iter(shopping_list)
    for i in it:
        print(i)
    print('list of used up iterator: ', list(it))
    print('list of new iterator: ', list(iter(shopping_list)))
