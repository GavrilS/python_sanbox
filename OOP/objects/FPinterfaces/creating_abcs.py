"""
It is heavily recommended that we do not create an ABC. They are complex and there usually is no need
for us to define our own. Additionally, the existing set of ABCs contain mostly everything a regular user of
the language might require. A typical example of a use case for defining one would be if we are creating a 
framework and have a very specific use case.

This is an example of how to define one - from the book 'Fluent Python'. The ABC that is defined here is for 
displaying advertisements in random order, without repeating any before we go through all of the available
ones at least one time.
"""

import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        '''Add items from an iterable.'''

    @abc.abstractmethod
    def pick(self):
        '''Remove item at random returning it.
        This method should raise a LookupError when the instance is empty.'''

    def loaded(self):
        '''Return True if there is at least 1 item, False otherwise'''
        return bool(self.inspect())

    def inspect(self):
        '''Return a sorted tuple with the items currently inside.'''
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        self.load(items)
        return tuple(sorted(items))


class Fake(Tombola):
    '''Testing a fake tombola implementation.'''
    def pick(self):
        return 13



if __name__=='__main__':
    print('Fake: ', Fake)
    print('The class was created without problems, but we see an error when we try to instantiate it.')
    f = Fake()
    print('f: ', f)
