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
