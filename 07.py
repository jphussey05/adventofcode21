from utils import get_input_file
import numpy as np


if __name__ == '__main__':

    positions = [int(num) for num in get_input_file('07-test.txt')[0].split(',')]

    fuel = 0
    tgt = np.mean(positions)

    for pos in positions:
        steps = abs(pos-tgt)
        fuel += (steps * (steps + 1)) / 2



    print(np.ceil(fuel))
    