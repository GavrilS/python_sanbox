# Every collection in python is iterable and iterators are used internally to suport:
    - for loops
    - Collection type construction and extension
    - Looping over text files line by line
    - List, dict and set comprehensions
    - Tuple unpacking
    - Unpacking actual parameters with * in function calls

* Iterable types can be used as input for lists and other iterable types => list(iterable type)

** The iter() function:
    - Checks whether the object implements __iter__, and calls that to obtain an iterator
    - If __iter__ is not implemented, but __getitem__ is implemented, python creates an iterator that attempts to fetch items in order, starting from index 0
    - If that fails, python raises TypeError, usually saying the object is not iterable. This is why every python sequence is iterable; they all implement __getitem__. The standard sequence usually implements __iter__ as well.
    - You can check if a type is iterable with abc.Iterable -> this only returns True if the __iter__ method is implemented.

# Generators:
* Every generator is an iterator. They fully implement the iterator interface. But while an iterator retrieves items from a collection, a generator can produce them out of 'thin air'.
