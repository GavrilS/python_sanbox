"""Python program showing abstract properties"""
from abc import ABC, abstractproperty


class Animal(ABC):
    """Abstract class"""

    @abstractproperty
    def num_legs(self):
        return "Different types of animals have a different number of legs!"


class Dog(Animal):

    @property
    def num_legs(self):
        return "A dog has four legs."


class Human(Animal):

    @property
    def num_legs(self):
        return "A human has two legs."


if __name__=='__main__':
    try:
        print('Trying to get number of legs of Animal()')
        a = Animal()
        print(a.num_legs)
    except Exception as e:
        print('Trying to get number of legs of Animal() resulted in error:\n', e)
    
    d = Dog()
    print(d.num_legs)

    h = Human()
    print(h.num_legs)
