"""
Testing different scenarios of operator overloading.
"""

class Test:

    def __init__(self, components):
        self._components = components

    def __str__(self): 
        return f"Class Test: {self._components}"
    
    def __add__(self, other):
        try:
            new_components = self._components + other
            return Test(new_components)
        except TypeError:
            raise NotImplemented

    def __radd__(self, other):
        return self + other



class Assistant:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Class Assistant: {tuple((self.a, self.b))}"

    def __add__(self, other):
        try:
            updated_a = self.a + str(other)
            updated_b = self.b + str(other)
            return Assistant(updated_a, updated_b)
        except TypeError:
            raise NotImplemented

    def __radd__(self, other):
        """This allows us to perform the addition of this class in case the object from it is provided as
        the second argument to a + operation."""
        return self + other


class Assistant2:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Class Assistant: {tuple((self.a, self.b))}"

    def __add__(self, other):
        try:
            updated_a = self.a + str(other)
            updated_b = self.b + str(other)
            return Assistant(updated_a, updated_b)
        except TypeError:
            raise NotImplemented

    # Without __radd__ implemented it will fail if the first operand of a + operation fails its __add__ method 
    # def __radd__(self, other):
    #     return self + other




if __name__=='__main__':
    assistant = Assistant('foo', 'bar')
    tester = Test([1, 2, 3])
    assistant2 = Assistant2('foo', 'bar')

    print('assistant: ', assistant )
    print('assistant2: ', assistant2 )
    print('tester: ', tester)

    res = tester + assistant
    print('res: ', res)

    res2 = tester + assistant2
    print('res2: ', res2)
