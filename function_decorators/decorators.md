A decorator is a callable that takes another function as argument (the decorated func‐
tion). The decorator may perform some processing with the decorated function, and
returns it or replaces it with another function or callable object.

Example:

@decorate
def target():
    print('running target()')


is the same as writing this:

def target():
    print('running target()')

target = decorate(target)


# Important decorator facts:
1. They can replace the decorated function with a different one
2. They are executed immediately when a module is loaded

# Usage(points to remember):
- A decorator is usually defined in one module and applied to functions in other modules
- Most decorators don't return the function passed as arguments; they usually define an inner function that is than returned


## !! Decorators in the standard library:
- Python has three built-in functions that are designed to decorate methods: property, classmethod and staticmethod

- functools.wraps - a helper for building well behaved decorators

- functools.lru_cache - a decorator that implements memoization, an optimization technique that works by saving the results of previous invocations of an expensive function, avoiding repeat computations on previously used arguments

- functools.singledispatch - it turns a simple function into a generic one: a group of functions to perform the same operation in different ways; in a way it substitutes for Java's method overloading


### Stacked decorators - decorators can be stacked; for example we can have @d1 and @d2 applied to a function and then the result will be the same as f = d1(d2(f))


#### Parameterized decorators - you can pass parameters to decorators
