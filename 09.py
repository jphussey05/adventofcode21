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
    
    return (row_idx, col_idx) if contents[row_idx][col_idx] < min([up, down, left, right]) else None



def check_neighbors(point, contents):
    row_idx, col_idx = point
    tgt_val = contents[row_idx][col_idx]
    valids = list()

    if tgt_val == 9:
        print(f'Target value is 9, which is not allowed, returning nothing...')
        return valids
    print(f'Checking neighbors of {row_idx}, {col_idx}')
    print(f'Points value is {contents[row_idx][col_idx]}, looking for {tgt_val}')
    # check up (row - 1)
    if row_idx > 0:
        up = contents[row_idx - 1][col_idx]
        if up >= tgt_val and up != 9:
            valids.append((row_idx-1, col_idx))
            print(f'Up point was good {contents[row_idx - 1][col_idx]}')
            print(f'Valids are now: {valids}')
    # check down (row + 1)
    if row_idx < len(contents) - 1:
        down = contents[row_idx + 1][col_idx]
        if down >= tgt_val and down != 9:
            valids.append((row_idx + 1, col_idx))
            print(f'Down point was good {contents[row_idx + 1][col_idx]}')
            print(f'Valids are now: {valids}')
    # check left (col - 1)
    if col_idx > 0:
        left = contents[row_idx][col_idx - 1]
        if left >= tgt_val and left != 9:
            valids.append((row_idx, col_idx-1))
            print(f'Left point was good {contents[row_idx][col_idx - 1]}')
            print(f'Valids are now: {valids}')
    # check right ( col + 1)
    if col_idx < len(contents[row_idx]) - 1:
        right = contents[row_idx][col_idx + 1]
        if right >= tgt_val and right != 9:
        
            valids.append((row_idx, col_idx + 1))
            print(f'Right point was good {contents[row_idx][col_idx + 1]}')
            print(f'Valids are now: {valids}')
        
    
    return valids



if __name__ == '__main__':
    contents = [list(map(int, list(row))) for row in get_input_file('09.txt')]


    sum_risk = 0
    basins = {}


    for row_idx, row in enumerate(contents):
        for col_idx, col in enumerate(row):

            low_point = check_height(row_idx, col_idx, contents)
            if low_point:
                sum_risk += contents[row_idx][col_idx] + 1
                basins[low_point] = set([low_point])
                
    
    print(f'Done, total risk is {sum_risk}, found {len(basins)} basins\n')
    
    for basin in basins:
        print(f'Starting at basin {basin}')
        to_check = [basin]
        print(f'------------')
        print(f'Looking at neighbors of {basin}')
        while to_check:

            basin_neighbors = set(check_neighbors(to_check[0], contents))
            print(f'Received {basin_neighbors} back from check')
            news = basin_neighbors.difference(basins[basin])
            print(f'These are new: {news}')
            basins[basin].update(news)
            print(f'Basin now looks like: {basins[basin]}')
            for bn in basin_neighbors:
                if bn not in basins[basin]:
                    basins[basin].append(bn)
                
            to_check.extend(news)
            to_check.pop(0)
       

        print(f'Exhausted all options for basin {basin}')
        print(f'Points are {basins[basin]}')


    biggest_three = sorted(basins, key=lambda k: len(basins[k]), reverse=True)[:3]
    print(f'Biggest three are {biggest_three}')
    score = 1
    for bt in biggest_three:
        score *= len(basins[bt])

    print(f'Score is {score}')
    # for each point in a basin
    # check its neighbors
    # if the neighbor is +1 from the point
    # add it to the list to check
    # otherwise move on?