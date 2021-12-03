from utils import get_input_file
from collections import Counter





def part1(contents):

    gamma = ''
    epsilon = ''

    while(len(contents[0]) > 0):
        temp = Counter([number.pop(0) for number in contents])
        
        if temp['0'] > temp['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    

    g_int = int(gamma, 2)
    e_int = int(epsilon, 2)

    return(g_int * e_int)


def part2(contents):
    o2 = list(contents)
    co2 = list(contents)

    for i in range(len(contents[0])):
        o2_tmp = Counter([number[i] for number in o2])
        if o2_tmp['0'] > o2_tmp['1']:
            o2 = [val for val in o2 if val[i] == '0'] if len(o2) > 1 else o2
        elif o2_tmp['1'] > o2_tmp['0']:
            o2 = [val for val in o2 if val[i] == '1'] if len(o2) > 1 else o2
        else:
            #they are same
            o2 = [val for val in o2 if val[i] == '1'] if len(o2) > 1 else o2
        
    for i in range(len(contents[0])):
        co2_tmp = Counter([number[i] for number in co2])
        if co2_tmp['0'] > co2_tmp['1']:
            co2 = [val for val in co2 if val[i] == '1'] if len(co2) > 1 else co2
        elif co2_tmp['1'] > co2_tmp['0']:
            co2 = [val for val in co2 if val[i] == '0'] if len(co2) > 1 else co2
        else:
            co2 = [val for val in co2 if val[i] == '0'] if len(co2) > 1 else co2

    o2_int = int(''.join(o2[0]), 2)
    co2_int = int(''.join(co2[0]), 2)

    print(o2_int, co2_int)

    return o2_int * co2_int


if __name__ == "__main__":
    test = False

    contents = [number for number in get_input_file('03.txt' if not test else '03-test.txt')]

    # p1 = part1(list(contents))
    p2 = part2(contents)
    print(p2)