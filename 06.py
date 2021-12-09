from utils import get_input_file
import numpy as np


def advance(timers):
    print(f'Received {timers}')
    new = timers[1:]
    new.append(timers[0])
    new[6] += timers[0]

    print(f'New timers {timers}')

    return new

if __name__ == '__main__':

    fishes = list(map(int, get_input_file('06.txt')[0].split(',')))
    timers = [fishes.count(idx) for idx in range(9)]

    print(timers)

    print(fishes)

    for x in range(256):
        timers = advance(timers)

    print(f'Sum is {sum([cnt for cnt in timers])}')