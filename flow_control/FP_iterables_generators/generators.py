# This is a simple example of the behavior of a generator function
def gen_123():
    yield 1
    yield 2
    yield 3


if __name__=='__main__':
    print('gen_123(): ', gen_123())
    for i in gen_123():
        print(i)

    g = gen_123()
    for i in range(10):
        try:
            print(next(g))
        except Exception as e:
            print(e)
            break
