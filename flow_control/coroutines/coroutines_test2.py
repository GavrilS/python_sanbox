"""
A python program to test multiple coroutines.
"""
import random
from datetime import datetime, timedelta


def get_runtime(start, break_time):
    try:
        while True:
            now = yield
            time_elapsed = start - now
            print('Time Elapsed: ', time_elapsed)
            if time_elapsed > break_time:
                print('Runtime exceeded!')
                break
    except GeneratorExit:
        print('Get Runtime routine closing!')
