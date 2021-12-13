from utils import get_input_file






if __name__ == '__main__':
    contents = get_input_file('13-test.txt')

    break_spot = contents.index('')

    folds = contents[break_spot+1:]
    marks = contents[:break_spot]

    rows = [int(x.split(',')[0]) for x in marks]
    cols = [int(x.split(',')[1]) for x in marks]
    row_num = max(rows)
    print(min(rows), max(rows))
    print(min(cols), max(cols))

    for fold in folds:
        print(fold)

    for mark in marks:
