from array import array
import math

class Vector:
    typecode = 'd' # class attribute used to convert Vector to/from bytes

    def __init__(self, x, y):
        # converting x and y to floats in the constructor to catch errors
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        # this is what makes the Vector iterable; implemented by using a generator expression to yield the 
        # components one after the other
        return (i for i in (self.x, self.y))

    def __repr__(self):
        # returns the representation of the object; since Vector is iterable *self fieds its components to format
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self) #

    def __str__(self):
        return str(tuple(self)) #

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self))) 

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
