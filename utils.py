def get_input_file(filename):
    with open(filename) as fin:
        return [line.strip() for line in fin.readlines()]