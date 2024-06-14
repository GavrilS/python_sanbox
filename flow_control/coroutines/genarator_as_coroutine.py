
def simple_coroutine():
    print('Coroutine started!')
    x = yield # yield None if the coroutine is designed just to receive data from the client(like now)
    print('Coroutine received: ', x)


def simple_coroutine2(val):
    print('Coroutine started! val -> ', val)
    x = yield val
    print('-> Received x -> ', x)
    y = yield val + x
    print('-> Received y -> ', y)



if __name__=='__main__':
    try:
        my_coro = simple_coroutine()
        print(my_coro)
        next(my_coro) # the first call is next() so the generator can reach the yield where we can send data
        my_coro.send(42) # with send() we can send a value to the coroutine
    except Exception as e:
        print('my_coro error -> \n', str(e))
        print('----------------')

    my_coro2 = simple_coroutine2(5)
    from inspect import getgeneratorstate
    try:
        print(getgeneratorstate(my_coro2))
        next(my_coro2)
        print(getgeneratorstate(my_coro2))
        my_coro2.send(20)
        my_coro2.send(30)

    except Exception as e:
        print(getgeneratorstate(my_coro2))
        print('my_coro2 error ->\n', str(e))
        print('----------------')
