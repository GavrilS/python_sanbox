

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)


def check_factorial(n):
    result = factorial(n)
    print('result: ', result)
    print('factorial.__doc__: ', factorial.__doc__)
    print('type(factorial): ', type(factorial))
    print('*'*40)
    fact = factorial
    print('fact(10): ', fact(10))
    print('map of factorial: ', map(factorial, range(11)))
    print(list(map(fact, range(11))))


if __name__=='__main__':
    check_factorial(5)
