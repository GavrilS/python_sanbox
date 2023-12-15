"""This is a program to show how abstract classes work in python.
"""
from abc import ABC, abstractmethod


class Polygon(ABC):
    """Abstract base class"""

    @abstractmethod
    def side_number(self):
        """Abstract method to be implemented in inheriting classes"""
        pass


class Triangle(Polygon):

    # Overriding abstract method of base class
    def side_number(self):
        print('A triangle has 3 sides.')


class Square(Polygon):

    # Overriding abstract method of base class
    def side_number(self):
        print('A square has 4 sides.')


class Hexagon(Polygon):

    # Overriding abstract method of base class
    def side_number(self):
        print('A hexagon has 6 sides.')



if __name__=='__main__':
    try:
        print('Trying to instantiate an ABC base class Polygon():')
        p = Polygon()
        p.side_number()
    except Exception as e:
        print('Trying to instantiate abstract class Polygon() resulted in an error:\n', e)

    t = Triangle()
    t.side_number()

    s = Square()
    s.side_number()

    h = Hexagon()
    h.side_number()
