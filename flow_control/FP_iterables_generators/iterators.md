# Every collection in python is iterable and iterators are used internally to suport:
    - for loops
    - Collection type construction and extension
    - Looping over text files line by line
    - List, dict and set comprehensions
    - Tuple unpacking
    - Unpacking actual parameters with * in function calls

* Iterable types can be used as input for lists and other iterable types => list(iterable type)

** The iter() function:
    - Checks whether the object implements __iter__, and calls that to obtain an iterator.
    - If __iter__ is not implemented, but __getitem__ is implemented, python creates an iterator that attempts to fetch items in order, starting from index 0
    - If that fails, python raises TypeError, usually saying the object is not iterable. This is why every python sequence is iterable; they all implement __getitem__. The standard sequence usually implements __iter__ as well.
    - You can check if a type is iterable with abc.Iterable -> this only returns True if the __iter__ method is implemented.

*** Iterators in python aren't a matter of type but of protocol. Don't check the type! Use hasattr to check for both __iter__ and __next__ attributes instead -> that is exactly what the __subclasshook__ method in the abc.Iterator ABC does.
    - Iterators Definition: any object that implements the __next__ no argument method that returns the next item in a series or raises StopIteration when there are no more items. Python iterators also implement the __iter__ method which means they are iterable as well.

!!! Iterables should never act as iterators for themselves. In other words implement the __iter__ method for an iterable, but don't implement __next__. The __iter__ method should return an iterator of the iterable. Iterators should implement the __next__ method and also the __iter__ method, which means that iterators are also iterable. The __iter__ method of an iterator should just return self. -> CLASSIC ITERATOR PATTERN
