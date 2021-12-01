from typing import Mapping
from utils import get_input_file


def solver(contents, size):
    windows = [contents[i:i+size] for i in range(len(contents)+1-size)]
    sums = list(map(sum, windows))

    cnt = 0
    for i in range(1, len(sums)):
        if sums[i] > sums[i-1]:
            cnt += 1

    return cnt

if __name__ == '__main__':
    contents = list(map(int, get_input_file('01.txt')))
    
    p1 = solver(contents, 1)

    p2 = solver(contents, 3)
    print(f'Part 1 = {p1}')
    print(f'Part 2 = {p2}')