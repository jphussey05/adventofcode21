from utils import get_input_file


def check_height(row_idx, col_idx, contents):
    # check up (row - 1)
    up = contents[row_idx - 1][col_idx] if row_idx > 0 else 99
    # check down (row + 1)
    down = contents[row_idx + 1][col_idx] if row_idx < len(contents) -1 else 99
    # check left (col - 1)
    left = contents[row_idx][col_idx - 1] if col_idx > 0 else 99
    # check right ( col + 1)
    right = contents[row_idx][col_idx + 1] if col_idx < len(contents[row_idx]) - 1  else 99
    
    return True if contents[row_idx][col_idx] < min([up, down, left, right]) else False

if __name__ == '__main__':
    contents = [list(map(int, list(row))) for row in get_input_file('09-test.txt')]


    sum_risk = 0

    for row_idx, row in enumerate(contents):
        for col_idx, col in enumerate(row):

            if check_height(row_idx, col_idx, contents):
                sum_risk += contents[row_idx][col_idx] + 1

    
    print(f'Done, total risk is {sum_risk}')
            