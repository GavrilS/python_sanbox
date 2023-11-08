"""
Implement the __missing__ method on a custom subclass of the dict class
"""

class StrDictKey(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)

        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__=='__main__':
    d = StrDictKey([('2', 'two'), ('4', "four")])
    print("d['2']: ", d['2'])
    print('d[2]: ', d[2])
    print('d[4]: ', d[4])
    print('d[1]: ', d[1])
