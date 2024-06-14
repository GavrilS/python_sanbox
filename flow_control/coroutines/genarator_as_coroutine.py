
def simple_coroutine():
    print('Coroutine started!')
    x = yield # yield None if the coroutine is designed just to receive data from the client(like now)
    print('Coroutine received: ', x)



if __name__=='__main__':
    my_coro = simple_coroutine()
    print(my_coro)
    next(my_coro) # the first call is next() so the generator can reach the yield where we can send data
    my_coro.send(42) # with send() we can send a value to the coroutine
    