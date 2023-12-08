import time

def clock(func):
    def clocked(*args): # take a number of arguments to pass to the function passed to clock()
        t0 = time.perf_counter()
        # print('t0: ', t0)
        result = func(*args) # the closure for clocked encompasses the func free variable
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked
