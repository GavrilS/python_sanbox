# Generators:
* Every generator is an iterator. They fully implement the iterator interface. But while an iterator retrieves items from a collection, a generator can produce them out of 'thin air'. Generators are iterators that produce the values of the expresions passed to yield.

** Generator functions:
    - Any python function that has the yield keyword in its body is a generator function. This is a function which, when called returns a generator object; in other words it is a generator factory.
    - When we call next() on a generator object, execution advances to the next yield keyword in the function's body. When there are no more yield statements to go over and the function body returns, the enclosing generator raises StopIteration in accordance with the Iterator protocol.
