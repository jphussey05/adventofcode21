from utils import get_input_file
from collections import Counter
import numpy as np



if __name__ == '__main__':
    lines = [list(map(int, line.replace(' -> ', ',').split(','))) for line in get_input_file('05-test.txt')]

    