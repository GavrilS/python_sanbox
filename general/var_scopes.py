a = 5

def f1(b):
    print('a: ', a)
    print('b: ', b)


def f2(b):
    print('a: ', a)
    print('b: ', b)
    a = 3 # initial print of a will fail because a is assignet in the scope of the func as a local var as well


def f3(b):
    print('a: ', a)
    print('b: ', b)
    b = 5
    print('final b: ', b)


def f4(b):
    global a # this lets the interpreter know we are using the global a, not the local one created later
    print('a: ', a)
    print('b: ', b)
    a = 3


if __name__=='__main__':
    print('f1(3)')
    f1(3)
    print('*'*40)
    print('f2(8)')
    try:
        f2(8)
    except Exception as e:
        print(e)
    
    print('*'*40)
    print('f3(9)')
    try:
        f3(9)
    except Exception as e:
        print(e)

    print('*'*40)
    print('f4(9)')
    try:
        f4(9)
    except Exception as e:
        print(e)
