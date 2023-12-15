"""A python program showing abstract classes through inheritance"""

class Animal:
    """Abstract base class without abc"""

    # abstract method
    def move(self):
        pass


class Human(Animal):

    # Implementing empty move() method from parent class
    def move(self):
        print('A human walks on two legs.')


class Dog(Animal):

    # Implementing empty move() method from parent class
    def move(self):
        print('A dog walks on four legs.')


class Bird(Animal):

    # Implementing empty move() method from parent class
    def move(self):
        print('A bird flies.')



if __name__=='__main__':
    try:
        print('Trying to instantiate a base class Animal() with an empty move() method:')
        a = Animal()
        a.move()
    except Exception as e:
        print('Trying to instantiate a base class Animal() with an empty move() method resulted in error:\n', e)

    h = Human()
    h.move()

    d = Dog()
    d.move()

    b = Bird()
    b.move()
