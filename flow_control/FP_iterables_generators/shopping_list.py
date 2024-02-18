"""
This is an example of iterables and iterators in python.
"""

import re
import reprlib

# RE_INGREDIENT = re.compile(',+')


class ShoppingList:
    '''This shopping list is an iterable because of __getitem__'''
    def __init__(self, ingredient_str):
        self.ingredient_str = ingredient_str
        self.ingredients = re.split(', ', ingredient_str)

    def __getitem__(self, index):
        return self.ingredients[index]

    def __len__(self):
        return len(self.ingredients)

    def __repr__(self):
        return f"ShoppingList({reprlib.repr(self.ingredient_str)})"




if __name__=='__main__':
    # sl is an iterable
    sl = ShoppingList('bananas, ice-cream, potatoes, spring onion')
    print('shopping list: ', sl)
    for item in sl:
        print(item)

    it = iter(sl)
    print('iterator of the shopping list: ', it)
    try:
        for i in range(6):
            print(next(it))
    except Exception as e:
        print(e)
    
    print('list of used up iterator: ', list(it))
    print('list of new iterator: ', list(iter(sl)))

