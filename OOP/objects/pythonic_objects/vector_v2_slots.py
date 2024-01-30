"""
The only difference here is the __slots__ attribute. By defining __slots__ you tell the interpreter these are
all the instance attributes in this class. Python then stores them in a tuple like structure instead of using
a hash table for the __dict__ attribute, which makes the code run faster. __slots__ are good when we have a
class that will a have a large number of instances active at the same time.
"""
from array import array
import math

class Vector:
    ## Only new thing to _v2_slots:
    __slots__ = ('__x', '__y')

    typecode = 'd' # class attribute used to convert Vector to/from bytes

    def __init__(self, x, y):
        # converting x and y to floats in the constructor to catch errors
        ##!!!! making the properties read only implemented in v2 !!!!##
        self.__x = float(x)
        self.__y = float(y)

    ##!!!! New in v2 !!!!##
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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

    ##!!!! New in v2 !!!!##
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

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
    v2 = Vector(3.1, 4.4)
    print('hash(v1): ', hash(v1))
    print('hash(v2): ', hash(v2))
    print('set([v1, v2]): ', set([v1, v2]))
    print('*'*40)
    # Example of name mangling: when you name an instance variable with 2 leading _ - __x, python will 
    # store the name in the instance __dict__ prefixed with the name of the class with a leading _
    # This feature is a safety device, not a security one: like a switch cover, it protects you from
    # accidental access, but cannot stop intentional behaviour
    try:
        print('v1.__dict__: ', v1.__dict__)
        print('v2.__dict__: ', v2.__dict__)
    except Exception as e:
        print(e)
    
    print('v1.__slots__: ', v1.__slots__)
    print('v2.__slots__: ', v2.__slots__)
    print('v1: ', v1)
    print('v2: ', v2)
