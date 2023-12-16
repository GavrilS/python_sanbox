"""A python program to showcase the usage of getter/setters in python."""

class Example:

    def __init__(self, a):
       self. __set_a(a)

    
    # getter method to get the value of the property
    def get_a(self):
        return self.__a


    # setter method to set the value of the property
    def __set_a(self, a):
        self.__a = a


class Example2:

    def __init__(self, b):
        self._set_b(b)

    
    def get_b(self):
        return self._b

    
    def _set_b(self, b):
        self._b = b


if __name__=='__main__':
    print('Example 1 - double underscore(_) for setter and property')
    e = Example(10)
    print('e.get_a: ', e.get_a)
    print('e.get_a(): ', e.get_a())
    try:
        print('e.__set_a(8) ')
        e.__set_a(8)
        print('e.get_a(): ', e.get_a())
    except Exception as exc:
        print('Could not set a new value for e.__a: ', exc)
    
    print('*'*40)
    e2 = Example2(20)
    print('e2.get_b(): ', e2.get_b())
    try:
        print('e2._set_b(8) ')
        e2._set_b(8)
        print('e2.get_b(): ', e2.get_b())
    except Exception as exc:
        print('Could not set a new value for e2._a: ', exc)

    print('*'*40)
