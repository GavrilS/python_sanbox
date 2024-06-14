"""
This program calculates the running average using a coroutine.
"""

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count



if __name__=='__main__':
    co_avg = averager()
    next(co_avg)
    print(co_avg.send(10))
    print(co_avg.send(10))
    print(co_avg.send(38))
    co_avg.close()
