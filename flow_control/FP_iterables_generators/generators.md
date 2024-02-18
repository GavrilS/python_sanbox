# Generators:
* Every generator is an iterator. They fully implement the iterator interface. But while an iterator retrieves items from a collection, a generator can produce them out of 'thin air'. Generators are iterators that produce the values of the expresions passed to yield.

** Generator functions:
    - Any python function that has the yield keyword in its body is a generator function. This is a function which, when called returns a generator object; in other words it is a generator factory.
    - When we call next() on a generator object, execution advances to the next yield keyword in the function's body. When there are no more yield statements to go over and the function body returns, the enclosing generator raises StopIteration in accordance with the Iterator protocol.

*** Simple generator functions can be replaced by generator expressions. A generator expression is akin to a lazy version of list comprehension: it does not eagerly build a list, but returns a generator that will lazily produce the items on demand.

**** When a generator function needs to return values from another generator it can be achieved with nested for loops, but there is new syntax to accomplish the same thing. The new syntax is with 'yield from <var>'.

## Iterable reducing functions - functions that take an iterable and return a single result. These functions are also known as 'reducing', 'folding' or 'accumulating':

Module || Function || Description

(built-in) || all(it) || Returns True if all items in it are truthy, otherwise False; all([])
returns True

(built-in) || any(it) || Returns True if any item in it is truthy, otherwise False; any([])
returns False

(built-in) || max(it, [key=,] [default=]) || Returns the maximum value of the items in it; a key is an ordering function, as in sorted; default is returned if the iterable is empty

(built-in) || min(it, [key=,] [default=]) || Returns the minimum value of the items in it, key is an ordering function, as in sorted; default is returned if the iterable is empty

functools || reduce(func, it, [initial]) || Returns the result of applying func to the first pair of items, then to that result and the third item and so on; if given, initial forms the initial pair with the first item

(built-in) || sum(it, start=0) || The sum of all items in it, with the optional start value added (use
math.fsum for better precision when adding floats)
