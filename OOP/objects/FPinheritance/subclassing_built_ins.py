"""
An example of why it is a bad idea to subclass built-in types in python.
"""

class TestDict(dict):

    def __getitem__(self, item):
        return 42


if __name__=='__main__':
    td = TestDict(a='foo',b='boo')
    print('td: ', td)
    print('td["a"]: ', td['a'])
    print('td["b"]: ', td['b'])
    reg_dict = dict(td)
    print('reg_dict: ', reg_dict)
    print('reg_dict[a]: ', reg_dict['a'])
    print('reg_dict[b]: ', reg_dict['b'])
    reg_dict2 = {}
    reg_dict2.update(td)
    print('reg_dict2: ', reg_dict2)
    print(reg_dict2['a'])
    print(reg_dict2['b'])
