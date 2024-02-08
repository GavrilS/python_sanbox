"""
This is an example of the partial implementation of a protocol, in this case the sequence protocol.
Sequence: __getitem__, __contains__, __iter__, __len__ ...
"""

class Foo:
    '''
    Partially implement the sequence protocol with just __getitem__ and look at what is availabel with just that.
    '''
    def __getitem__(self, pos):
        return range(30)[pos]



if __name__=='__main__':
    f = Foo()
    print('f[1]: ', f[1])
    print('20 in f: ', 20 in f)
    print('40 in f: ', 40 in f)
    for i in f: print(i)
