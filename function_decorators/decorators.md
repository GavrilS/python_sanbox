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
