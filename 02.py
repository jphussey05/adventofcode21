from utils import get_input_file


def solver1(contents):

    x = 0
    y = 0

    for move in contents:
        direction = move[0]
        magnitude = int(move[1])

        if direction == 'forward':
            x += magnitude
        elif direction == 'down':
            y += magnitude
        elif direction == 'up':
            y -= magnitude
        else:
            print(f'Received a bad direction!')
            exit()
    
    return x * y


def solver2(contents):

    a = 0
    x = 0
    y = 0

    for move in contents:
        direction = move[0]
        magnitude = int(move[1])

        if direction == 'forward':
            x += magnitude
            y += (a * magnitude)
        elif direction == 'down':
            a += magnitude
        elif direction == 'up':
            a -= magnitude
        else:
            print(f'Received a bad direction!')
            exit()
    
    return x * y

if __name__ == '__main__':
    contents = [tuple(line.split()) for line in get_input_file('02.txt')]

    ans1 = solver1(contents)
    ans2 = solver2(contents)

    print(f'Part 1: {ans1}')
    print(f'Part 2: {ans2}')