"""
Python program for showing basic usage of coroutines.
"""
from argparse import ArgumentParser

VALID_TEST_CASES = [
    'single',
    'continuous_coro'
]

name = 'Initial'

def print_matching_name(sub_name):
    print(f"Searching for names containing: {sub_name}")
    try:
        while True:
            name = yield
            if sub_name in name:
                print(name)
                # break
    except GeneratorExit:
        print('Closing coroutine!')


def single():
    global name
    sub_name = input('Give me a name to look for: ')
    coro = print_matching_name(sub_name)
    coro.__next__()

    try:
        name = 'Achilles'
        coro.send(name)
        name = 'Heracles'
        coro.send(name)
        name = 'Perseus'
        coro.send(name)
        coro.close()
    except Exception as e:
        print('Reached the end of the coroutine: ', str(e))
        print('Finished on name: ', name)


def continuous_coro():
    global name
    sub_name = input('Give me a name to look for: ')

    while True:
        try:
            coro = print_matching_name(sub_name)
            coro.__next__()
            name = input('Give me a name to test: ')
            if name == 'exit':
                return
            coro.send(name)
            coro.close()
        except Exception as e:
            print('Found the name we were looking for! ', str(e))


if __name__=='__main__':
    parser = ArgumentParser(description='Testing coroutines')
    parser.add_argument('--test_case', default='single', choices=VALID_TEST_CASES)
    args = parser.parse_args()
    test_case = args.test_case

    eval(test_case)()
    print('After test case the final name value is: ', name)
