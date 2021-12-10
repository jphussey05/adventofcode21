from pprint import pprint
from utils import get_input_file


def get_uniques(inputs):
    sorted_inputs = sorted(inputs.split(), key=len)
    uniques = sorted_inputs[:3]
    uniques.append(sorted_inputs[-1])
    return uniques


def get_nine(inputs, four):
    for inp in inputs.split():
        if len(inp) == 6:
            if set(four).intersection(set(inp)) == set(four):
                return inp


def get_three(inputs, seven):
    for inp in inputs.split():
        if len(inp) == 5:
            if set(seven).intersection(set(inp)) == set(seven):
                return inp


def get_five(inputs, nine, three):
    for inp in inputs.split():
        if len(inp) == 5 and inp != three:
            if set(nine).intersection(set(inp)) == set(inp):
                return inp

def get_two(inputs, five, two):
    for inp in inputs.split():
        if len(inp) == 5 and inp not in [two, five]:
            return inp


def get_six(inputs, five, nine):
    for inp in inputs.split():
        if len(inp) == 6 and inp != nine:
            if set(five).intersection(set(inp)) == set(five):
                return inp   


def get_zero(inputs, nine, six):
    for inp in inputs.split():
        if len(inp) == 6 and inp not in [nine, six]:
            return inp


def print_decoded(decoded):
    for num, code in enumerate(decoded):
        print(f'{num} = {code}')


if __name__ == '__main__':



    contents = get_input_file('08.txt')
    entries = [x.split(' | ') for x in contents]
    output_val_list = []

    inputs = [x[0] for x in entries]
    outputs = [x[1] for x in entries]

    for idx in range(len(inputs)):
        print(f'Starting: {inputs[idx]}')
        decoded = ['---'] * 10
        
        
        decoded[1], decoded[7], decoded[4], decoded[8] = get_uniques(inputs[idx])
        decoded[9] = get_nine(inputs[idx], decoded[4])
        decoded[3] = get_three(inputs[idx], decoded[7])
        decoded[5] = get_five(inputs[idx], decoded[9], decoded[3])
        decoded[2] = get_two(inputs[idx], decoded[5], decoded[3])
        decoded[6] = get_six(inputs[idx], decoded[5], decoded[9])
        decoded[0] = get_zero(inputs[idx], decoded[9], decoded[6])
        
        print_decoded(decoded)
        decoded_sets = list(map(set, decoded))

        output_val = ''
        for out in outputs[idx].split():
            out_set = set(out)
            output_val += str(decoded_sets.index(out_set))

        output_val_list.append(int(output_val))
        print(output_val_list)
        print(sum(output_val_list))

