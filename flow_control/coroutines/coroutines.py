"""
Python program for showing basic usage of coroutines.
"""

name = 'Initial'

def print_matching_name(sub_name):
    print(f"Searching for names containing: {sub_name}")
    while True:
        name = yield
        if sub_name in name:
            print(name)
            break


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
    except Exception as e:
        print('Reached the end of the coroutine: ', str(e))
        print('Finished on name: ', name)


if __name__=='__main__':
    single()
    print('After single: ', name)
