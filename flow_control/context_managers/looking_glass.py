"""
Context managers implement the __enter__ and __exit__ dunder methods. They exist to control the 'with' 
statement, which simplifies the try/except statement to perform an operation and do something after it. In 
this case the enter method sets up the context when 'with' is invoked and the exit method clears the 
resources when we leave the 'with' statement.
__enter__ -> takes only self as an argument
__exit__ -> takes self, exc_type - the exception class, exc_value - the exception instance, traceback - 
a traceback object
"""
class LookingGlass:

    def __enter__(self):
        import sys
        self.original_output = sys.stdout.write
        sys.stdout.write = self.reverse_output
        return 'JABBERWABBER'

    
    def reverse_output(self, text):
        self.original_output(text[::-1])

    
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_output
        if exc_type is ZeroDivisionError:
            print('Please do not devide by zero!')
            return True



if __name__=='__main__':
    with LookingGlass() as lg:
        print('We love learning!!!')
        print(lg)
    
    print('After the exit method is called on the context manager!')
    print(lg)
