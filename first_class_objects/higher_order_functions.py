'''
A function that takes another function as argument or returns a function as a result is a higher order function.
'''


def sort_list():
    '''Sorting a list with the len/reverse function passed as argument to the sorted function.'''
    fruits = ['banana', 'apple', 'grapefruit', 'cherry', 'raspberry']
    print('sorted fruits by length: ', sorted(fruits, key=len))
    print('*'*40)
    print('reverse(testing): ', reverse('testing'))
    print('sorted fruits by reverse: ', sorted(fruits, key=reverse))


def reverse(word):
    return word[::-1]


def test_list_comprehension():
    result = [factorial(n) for n in range(6) if n % 2]
    print('list comprehension with factorial: ', result)


def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)


def anon_functions():
    fruits = ['banana', 'apple', 'grapefruit', 'cherry', 'raspberry']
    print('sorting fruits with lambda function: ', sorted(fruits, key=lambda word: word[::-1]))


if __name__=='__main__':
    sort_list()
    print('*'*40)
    test_list_comprehension()
    print('*'*40)
    anon_functions()
