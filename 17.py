from utils import get_input_file
from random import randint


def get_boundaries(parts):
    xparts = parts[2].split('..')
    yparts = parts[3].split('..')
    xmin = int(xparts[0][2:])
    xmax = int(xparts[1][:-1])
    ymin = int(yparts[0][2:])
    ymax = int(yparts[1])

    return xmin, xmax, ymin, ymax


def in_play(pos, xmax, ymin):
    x, y = pos
    return True if x <= xmax and y >= ymin else False


def in_target(pos, xmin, xmax, ymin, ymax):
    x, y = pos
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        return True
    else:
        return False


def adv_projectile(pos, xvel, yvel):
    x, y = pos
    x += xvel
    y += yvel

    if xvel > 0:
        xvel -= 1
    elif xvel < 0:
        xvel += 1
    
    yvel -= 1

    return (x, y), xvel, yvel


if __name__ == '__main__':
    parts = get_input_file('17.txt')[0].split()
    xmin, xmax, ymin, ymax = get_boundaries(parts)

    print(xmin, xmax, ymin, ymax)
    total_cnt = 0
    global_max = 0


    for xstart in range(0, xmax+1):
        for ystart in range(-1000, 1000):
            pos = 0,0
            local_max = 0
            xvel = xstart
            yvel = ystart
            # print(f'----------')
            # print(f'Beginning {xstart,ystart}')
            # print(f'----------')

            # if we're still in play
            while in_play(pos, xmax, ymin):
                if pos[1] > local_max:
                    # print(f'New Max Y of {pos[1]}')
                    local_max = pos[1]
                # check if current pos is a score
                # otherwise step
                # print(f'Still in play at {pos}, velocity is {xvel, yvel}')
                on_target = in_target(pos, xmin, xmax, ymin, ymax)
                # print(f"{pos} is{'' if on_target else ' not'} on target")
                if on_target:
                    total_cnt += 1
                    print(f'On target with {pos}, max was {local_max}')
                    global_max = max(local_max, global_max)
                    break
                pos, xvel, yvel = adv_projectile(pos, xvel, yvel)

            # print(f'{pos} was not in play')

    print(global_max, total_cnt)



