from utils import get_input_file
import numpy as np
from pprint import pprint

if __name__ == '__main__':

    positions = [int(num) for num in get_input_file('07.txt')[0].split(',')]

    
    lower = min(positions)
    upper = max(positions)
    fuel_costs = {}

    for tgt in range(lower, upper+1):
        fuel = 0
        for pos in positions:
            steps = abs(pos-tgt)
            fuel += (steps * (steps + 1)) / 2
        
        fuel_costs[tgt] = fuel

    pprint(fuel_costs[sorted(fuel_costs, key=lambda x: fuel_costs[x])[0]])
    