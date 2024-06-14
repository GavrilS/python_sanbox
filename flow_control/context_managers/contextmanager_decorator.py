"""
Use the @contextmanager decorator to reduce the boilerplate of creating a class that implements the 
__enter__ / __exit__ methods. Instead here you create a generator with a single 'yield' statement. The 
part before the 'yield' is taking the role of the __enter__ method and the part after it is substituting 
the __exit__ method.
"""
import contextlib # Utilities for with-statement contexts

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    yield 'JABBERWABBER'

    sys.stdout.write = original_write


if __name__=='__main__':
    with looking_glass() as lg:
        print('We love learning!!!')
        print(lg)
    
    print('After the exit method is called on the context manager!')
    print(lg)
