from utils import get_input_file



def parse_fold(fold):
    _, _, flip = fold.split()
    xory, num = flip.split('=')
    
    return xory, int(num)


def fold_paper(xory, num, marks):
    print(f'Folding along {xory} = {num}')
    new_marks = set()

    if xory == 'x':
        for mark in marks:
            # above the fold, do not change, just add
            if mark[0] < num:
                print(f'Mark {mark} is above the fold')
                new_marks.add(mark)
            # below fold, subtract 2xdistance to fold from x
            elif mark[0] > num:
                
                dist = mark[0] - num
                
                tmp_mark = (mark[0] - 2 * dist, mark[1])
                print(f'Mark {mark} is below fold by {dist} unit(s), becomes {tmp_mark}')
                new_marks.add(tmp_mark)
            else:
                pass # the fold line doesn't go forward
    elif xory == 'y':
        for mark in marks:
            if mark[1] < num:
                print(f'Mark {mark} is left of fold')
                new_marks.add(mark)
            elif mark[1] > num:
                dist = mark[1] - num

                tmp_mark = mark[0], mark[1] - dist * 2
                print(f'Mark {mark} is right of fold by {dist} unit(s), becomes {tmp_mark}')
                new_marks.add(tmp_mark)
            else:
                pass  # fold was on this point
    
    return new_marks



def output_marks(marks):
    max_row = max([mark[0] for mark in marks])
    max_col = max([mark[1] for mark in marks])
    
    
    mark_map = [[' '] * (max_row + 1) for _ in range(max_col + 1)]
    print(f'Max col is {max_col} and map has {len(mark_map[0])} columns')


    for mark in marks:
        print(f'Plotting {mark}')
        mark_map[mark[1]][mark[0]] = '#'

    for row in mark_map:
        print(''.join(row))


if __name__ == '__main__':
    contents = get_input_file('13.txt')

    break_spot = contents.index('')

    folds = contents[break_spot+1:]
    marks = set(tuple(map(int, line.split(','))) for line in contents[:break_spot])

    print(f'Initial Marks:')
    print(marks)

    for fold in folds:


        xory, num = parse_fold(fold)

        marks = fold_paper(xory, num, marks)

        

                    
    print(f'Final Marks: {len(marks)}')
    # print(marks)

    output_marks(marks)
