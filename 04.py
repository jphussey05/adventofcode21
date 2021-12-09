from utils import get_input_file


def create_boards(contents):
    
    boards = []
    tmp = []
    while contents:
        line = contents.pop(0)
        if not line:
            continue
        
        line = list(map(int, line.split()))
        tmp.append(line)
        if len(tmp) == 5:
            boards.append(tmp)
            tmp = list()
        
    return boards


def print_boards(boards, single=False):

    if single:
        for row in boards:
            print(row)
    else:            
        for board in boards:
            for line in board:
                print(line)
            
            print()


def update_boards(boards, num):
    new_boards = list()

    for board in boards:
        tmp = list()
        for line in board:
            new_line = [-0.1 if x == num else x for x in line]
            tmp.append(new_line)
        new_boards.append(tmp)

    return new_boards


def sum_board(board):
    total = 0
    for row in board:
        unmarkeds = [num for num in row if num >= 0]
        total += sum(unmarkeds)
    
    return total





def check_boards(boards):
    
    board_drops = []
    last_board = True if len(boards) == 1 else False
    print(f'There are {len(boards)} boards during this check')
    for idx, board in enumerate(boards):
        # check columns
        cols = [[x[i] for x in board] for i in range(len(board))]
        for col in cols:
            if sum(col) == -0.5:
                print(f'Found a bingo column in board {idx}!')
                print_boards(board, single=True)

                if last_board:
                    return sum_board(board)
                else:
                    board_drops.append(idx)

        for row in board:
            if sum(row) == -0.5:
                print(f'Found a bingo row in board {idx}!')
                print_boards(board, single=True)

                if last_board:
                    return sum_board(board)
                else:
                    board_drops.append(idx)

    return board_drops if board_drops else None


if __name__ == '__main__':

 
    contents = get_input_file('04.txt')

    draws = list(map(int, contents.pop(0).split(',')))
    
    boards = create_boards(contents)

    # print_boards(boards)

    for num in draws:
        boards = update_boards(boards, num)
        result = check_boards(boards)

        if type(result) == int:
            print(f'Result was {result} * {num} = {result * num}')
            break
        else:
            if result is not None:
                print(f'Dropping board with index {result}')
                for drop in sorted(set(result), reverse=True):
                    boards.pop(drop)
        
