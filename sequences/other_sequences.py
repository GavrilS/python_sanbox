"""
If the sequence will only contain numbers, it could be more efficient to use array.array instead of list.
Another fast and flexible way of saving data is with the pickle module(it handles almost all built in types).
Besides deque, other python standard library packages implement queues: queue, multiprocessing, asyncio, heapq
"""
from argparse import ArgumentParser
from array import array
from random import random
from collections import deque

parser = ArgumentParser(description='This is going to be used to specify which specific sequence type tests to run')

parser.add_argument('--seq_type', default='array', choices=['array', 'deque'])
args = parser.parse_args()
seq_type = args.seq_type


def large_array_operations():
    floats = array('d', (random() for i in range(10**7))) # d is to create an array of double precision floats
    # from any iterable object(an array of doubles)
    print('floats[-1]', floats[-1])
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()
    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()
    print('floats2[-1]', floats2[1])
    print('floats2 == floats: ', floats2==floats)


def memory_view_ops():
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print('len(memv): ', len(memv))
    print('memv[0]: ', memv[0])
    memv_oct = memv.cast('B')
    print('memv_oct = memv.cast(\'B\') -> ', memv_oct)
    print('memv_oct.tolist(): ', memv_oct.tolist())
    print('memv_oct[5]: ', memv_oct[5])
    memv_oct[5] = 4
    print('numbers: ', numbers)


def deque_ops():
    dq = deque(range(10), maxlen=10)
    print('dq: ', dq)
    dq.rotate(3)
    print('dq.rotate(3): ', dq)
    dq.rotate(-4)
    print('dq.rotate(-4): ', dq)
    dq.appendleft(-1)
    print('dq.appendleft(-1): ', dq)
    dq.extend([11, 22, 33])
    print('dq.extend([11, 22, 33]): ', dq)
    dq.extendleft([10, 20, 30, 40])
    print('dq.extendleft([10, 20, 30, 40]): ', dq)


if __name__=='__main__':
    if seq_type == 'array':
        large_array_operations()
        print('*'*40)
        memory_view_ops()
    elif seq_type == 'deque':
        deque_ops()
