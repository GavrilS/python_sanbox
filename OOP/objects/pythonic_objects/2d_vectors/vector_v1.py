from array import array
import math

class Vector:
    typecode = 'd' # class attribute used to convert Vector to/from bytes

    def __init__(self, x, y):
        # converting x and y to floats in the constructor to catch errors
        self.x = float(x)
        self.y = float(y)

    ##!!!! New in the v1 version !!!!##
    @classmethod # class method decorator: defines a method that operates on the class and not on instances
    def frombytes(cls, octets): # no self argument, instead the class itself is passed as cls
        typecode = chr(octets[0]) # read the typecode from the first byte
        memv = memoryview(octets[1:]).cast(typecode) # create a memoryview from the octets binary sequence and cast it with typecode
        return cls(*memv) # unpack the memoryview resulting from the casting into the arguments needed by the constructor

    def __iter__(self):
        # this is what makes the Vector iterable; implemented by using a generator expression to yield the 
        # components one after the other
        return (i for i in (self.x, self.y))

    def __repr__(self):
        # returns the representation of the object; since Vector is iterable *self feeds its components to format
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        # from iterable type, it is easy to build a tuple for display as an ordered pair
        return str(tuple(self))

    def __bytes__(self):
        # to generate bytes we convert the typecode to bytes and concatenate bytes converted from an array
        # built by iterating over the instance
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self))) 

    def __eq__(self, other):
        # to quickly compare all components, we build tuples out of the operands; has issues: it will return 
        # True when comparing Vector(3, 4) == [3, 4]
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # we are using abs(self) to compute the magnituted, then convert it to bool, so 0.0 is False, non 0 is True
        return bool(abs(self))

    ## New in v1 ##
    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self) # use the format built-in to apply fmt_spec to each vector component
        return '({}, {})'.format(*components) # return the formatted strings


if __name__=='__main__':
    v1 = Vector(3, 4)
    print(f"v1.x - {v1.x}, v1.y - {v1.y}")
    x, y = v1
    print(f"{x}, {y}")
    print('v1: ', v1)
    v1_clone = eval(repr(v1))
    print('v1_clone: ', v1_clone)
    print('v1 == v1_clone: ', v1 == v1_clone)
    print('v1: ', v1)
    octets = bytes(v1)
    print('octets: ', octets)
    print('abs(v1): ', abs(v1))
    print(f"bool(v1) - {bool(v1)}, bool(Vector(0, 0) - {bool(Vector(0,0))})")
    print('format(v1): ', format(v1))
    print("format(v1, '.2f'): ", format(v1, '.2f'))
    print("format(v1, '.3f'): ", format(v1, '.3f'))
