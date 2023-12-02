

def my_args_sum(*args):
    result = 0
    # Iterate over the positional arguments passed to the function(the *args is a tuple)
    for x in args:
        result += x

    return result


def concatenate(**kwargs):
    result = ''
    # Iterate over the kwargs dictionary
    for item in kwargs.values():
        result += item + ' '
    
    return result


def test_kwargs(**kwargs):
    result = kwargs.get('test', 'test')
    result2 = kwargs.get('test2', 'test2')

    return result + ' ' + result2


if __name__=='__main__':
    print('my_args_sum(1, 2, 3): ', my_args_sum(1, 2, 3))
    print("concatenate(a='Python', b='Is', c='Great'): ", concatenate(a='Python', b='Is', c='Great!'))
    print("test_kwargs(test='One'): ", test_kwargs(test='One'))
    print("test_kwargs(test2='Two'): ", test_kwargs(test2='Two'))
    print("test_kwargs(test='One', test2='Two'): ", test_kwargs(test='One', test2='Two'))
