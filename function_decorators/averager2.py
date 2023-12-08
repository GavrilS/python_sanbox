"""This is an implementation of the Averager() functionality from ./averager.py using higher order functions.
"""

def make_averager():
    series = [] # this is closure; a local var in make_averager() which is kept by averager after the func returns

    def averager(new_value):
        series.append(new_value) # this is a free variable(defined outside the scope of the function)
        total = sum(series)
        return total/len(series)

    return averager


if __name__=='__main__':
    avg = make_averager()
    print('avg(10): ', avg(10))
    print('avg(11): ', avg(11))
    print('avg(12): ', avg(12))

    print('*'*40)
    print('avg.__code__: ', avg.__code__) # the __code__ attribute that represents the compiled body of the func
    print('avg.__code__.co_varnames: ', avg.__code__.co_varnames)
    print('avg.__code__.co_freevars: ', avg.__code__.co_freevars)
    print('avg.__closure__[0]: ', avg.__closure__[0])
    print('avg.__closure__[0].cell_contents: ', avg.__closure__[0].cell_contents)
