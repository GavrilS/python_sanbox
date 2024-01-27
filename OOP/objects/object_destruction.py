"""
The del keyword does not delete objects, but names. That means it removes the name from the references to an 
object. When there are no more connections to an object or if the object becomes unreachable it can be 
garbage collected.
"""
import weakref

s1 = {1, 2, 3}
s2 = s1

def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
print('ender.alive: ', ender.alive)
print('del s1')
del s1
print('ender.alive: ', ender.alive)
print('s2 = "spam"')
s2 = 'spam'
print('ender.alive: ', ender.alive)
