"""
The presence of references to an object(the referent) is what keeps it alive in memory, but weak references
do not increase the reference count of an object. They are perfect for caches.

Weak references limitations: weak references can be made to custom made types as well as sets, but lists and
dicts cannot have weak references(unless they are subclassed) as well as int and tuple(in the case of int and 
tuple even if they are subclassed weak refenreces cannot be made).
"""
import weakref

a_set = {0, 1, 2}
print('a_set: ', a_set)
wref = weakref.ref(a_set)
print('wref: ', wref)
print('wref(): ', wref())
a_set = {3, 4, 5}
print('a_set: ', a_set)
print('wref(): ', wref())
print('wref() is None: ', wref() is None)
print('************-----------------**************')

class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


# weakref.WeakValueDicitionary() -> this is a dict of weak references, perfect for caches; in this case we are
# caching what cheeses we have in stock
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print('sorted(stock.keys()): ', sorted(stock.keys()))
print('del catalog')
del catalog
print('sorted(stock.keys()): ', sorted(stock.keys()))
del cheese # cheese is in this context a global variable(it is outside of any function) and the last Cheese
# it had a reference to is still not garbage collected, so to remove it we use del
print('sorted(stock.keys()): ', sorted(stock.keys()))
