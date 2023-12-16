"""A python program to showcase the usage of properties in a python class."""

class PropertyExample:

    def __init__(self, a):
        self.a = a


    @property
    def a(self):
        return self.__a


    # The attribute name and method name must be the same which is used to set the value for the attribute
    @a.setter
    def a(self, a):
        self.__a = a



class PropertyExample2:

    def __init__(self, a):
        self.set_a(a)


    def get_a(self):
        return self.__a


    def set_a(self, a):
        self.__a = a


    a = property(get_a, set_a)




if __name__=='__main__':
    p = PropertyExample(10)
    print('p.a: ', p.a)
    print('p.a = 20')
    p.a = 20
    print('p.a: ', p.a)

    print('*'*40)
    p2 = PropertyExample2(20)
    print('p2.a: ', p2.a)
    print('p2.a = 30')
    p2.a = 30
    print('p2.a: ', p2.a)
