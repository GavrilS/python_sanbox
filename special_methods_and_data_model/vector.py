from math import hypot

class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Called by the repr built-in to get the string representation of the object for inspection.
        Without it the object would be shown as <Vector object at 0x1023131>.
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self,y)

    def __bool__(self):
        """
        This method tells Vector instances what process to use to determine whether they are True or False.
        """
        return bool(abs(self))

    def __add__(self, other):
        """
        This method tells Vector instances how to handle the + operator.
        """
        x = self.x + other
        y = self.y + other
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        This method tells Vector instances how to handle the * operator.
        """
        return Vector(self.x, self.y)



if __name__=='__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print('v1 + v2: ', v1 + v2)

    v = Vector(3, 4)
    print('abs(v): ', abs(v))

    print('v * 3: ', v * 3)
    print('abs(v * 3): ', abs(v * 3))
