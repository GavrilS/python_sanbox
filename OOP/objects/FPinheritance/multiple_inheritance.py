"""
An example of how python handles multiple inheritance.
"""

class Grandpa:

    def get_generation(self):
        print('I am from the grandpa generation: ', self)


class ParentGen(Grandpa):

    def get_generation(self):
        print('I am from a middle generation: ', self)

    def call(self):
        print('I want you to come home now...')


class ParentYounger(Grandpa):

    def call(self):
        print('You can stay a bit later')

    def get_generation(self):
        print('I am from a relatively young generation...')


class Child(ParentYounger, ParentGen):

    def call(self):
        super().call()

    def get_generation(self):
        print('This is the younger generation...')
        super().get_generation()


class ChildOlder(ParentGen, ParentYounger):

    def call(self):
        super().call()

    def get_generation(self):
        print('This is the younger generation + 2...')
        super().get_generation()



if __name__=='__main__':
    ch = Child()
    print('Younger child:')
    ch.call()
    ch.get_generation()

    ch_older = ChildOlder()
    print('Older child:')
    ch_older.call()
    ch_older.get_generation()

    print('younger_child.__mro__: ', Child.__mro__)
    print('older_child.__mro__: ', ChildOlder.__mro__)
