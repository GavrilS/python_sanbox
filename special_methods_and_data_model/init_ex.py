"""
The __init__ method is used to initialize instances of a class.
"""

class Square:

    def __init__(self, side_length):
        """
        To create a square it needs to know its side lenght.
        """
        self.side_length = side_length


square1 = Square(1)
print('square1 side length is: ', square1.side_length)
