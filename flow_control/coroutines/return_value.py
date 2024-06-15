from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:
            break
    
        total += term
        count += 1
        average = total/count
    return Result(count, average)



if __name__=='__main__':
    coro_avg = averager()
    next(coro_avg)
    print(coro_avg.send(12))
    print(coro_avg.send(18))
    print(coro_avg.send(7))
    print(coro_avg.send(14))
    try:
        print(coro_avg.send(None))
    except StopIteration as exc:
        print(exc.value)
