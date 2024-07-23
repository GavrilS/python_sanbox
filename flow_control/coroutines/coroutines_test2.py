"""
A python program to test multiple coroutines.
"""
import random
from datetime import datetime, timedelta
from argparse import ArgumentParser
import time

EXCEED_RUNTIME = 'Runtime exceeded!'
TARGET_REACHED = 'Target number reached!'


def get_runtime(start, break_time):
    try:
        while True:
            now = yield
            time_elapsed = now - start
            print('Time Elapsed: ', time_elapsed)
            print('Time Elapsed Seconds: ', time_elapsed.seconds)
            if time_elapsed.seconds > break_time:
                print('Runtime exceeded!')
                raise Exception(EXCEED_RUNTIME)
            time.sleep(1)
    except GeneratorExit:
        print('Get Runtime routine closing!')

    
def get_random_number(target):
    try:
        while True:
            test = yield
            print('Test number: ', test)
            if test == target:
                print(TARGET_REACHED)
                print(target)
                raise Exception(TARGET_REACHED)
    except GeneratorExit:
        print('Get Random Number routine closing!')



if __name__=='__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--target', default=10)
    parser.add_argument('--start_number', default=0)
    parser.add_argument('--end_number', default=11)
    parser.add_argument('--break_time', default=30)

    args = parser.parse_args()

    target = args.target
    start_range = args.start_number
    end_number = args.end_number
    break_time = int(args.break_time)

    print('*'*80)
    print('Test argumets:')
    print('Target number: ', target)
    print('Start range: ', start_range)
    print('End range: ', end_number)
    print('Time Limit for the test: ', break_time)
    print('*'*80)

    if target >= end_number or target < start_range:
        print('Wrong end range; the target needs to be between the start and end ranges!')
        exit()

    start_time = datetime.now()
    runtime_routine = get_runtime(start_time, break_time)
    runtime_routine.__next__()
    random_number_routine = get_random_number(target)
    random_number_routine.__next__()
    try:
        while True:
            test = random.randint(start_range, end_number)
            random_number_routine.send(test)
            now = datetime.now()
            runtime_routine.send(now)
    except Exception as e:
        print('Final exception is \n', str(e))
        runtime_routine.close()
        random_number_routine.close()
