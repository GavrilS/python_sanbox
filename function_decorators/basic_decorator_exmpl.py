def deco(func):
    def inner():
        print('running inner()')
    
    return inner


@deco
def target():
    print('running target()')


def deco_test(func):
    print('This is deco test')
    return func


@deco_test
def test():
    print('running test()')


if __name__=='__main__':
    target()
    print('target: ', target)
    print('*'*40)

    test()
    print('test: ', test)
