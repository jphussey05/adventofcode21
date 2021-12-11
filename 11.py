from utils import get_input_file
import numpy as np



def reset_octopus(octopus_map):
    octopus_map[np.where(octopus_map > 9)] = 0
    return octopus_map

def inc_neighbors(octopus_map, cur_flasher):

    ridx, cidx = cur_flasher
    
    if ridx > 0:                                    # can increment up
        octopus_map[ridx - 1][cidx] += 1
        
        if cidx < len(octopus_map[0]) - 1:          # can increment up and right
             octopus_map[ridx - 1][cidx + 1] += 1
        if cidx > 0:                                # can increment up and left
            octopus_map[ridx - 1][cidx - 1] += 1
        
    if ridx < len(octopus_map) - 1:                 # can increment down
        octopus_map[ridx + 1][cidx] += 1
        
        if cidx < len(octopus_map[0]) - 1:          # can increment down and right
            octopus_map[ridx + 1][cidx + 1] += 1
        if cidx > 0:                                # can increment down and left
            octopus_map[ridx + 1][cidx - 1] += 1
    
    if cidx > 0:                                    # can increment left
        octopus_map[ridx][cidx - 1] += 1
    
    if cidx < len(octopus_map[0]) - 1:              # can increment right
        octopus_map[ridx][cidx + 1] += 1


    return octopus_map

if __name__ == '__main__':
    contents = get_input_file('11.txt')
    flash_total = 0

    octopus_map = np.asarray([list(map(int, list(line))) for line in contents], dtype=np.dtype('u1'))
    print(octopus_map)
    # do 100 steps
    for x in range(1,10000000):
        print(f'****************\nRND {x}  Starts')
        flashers = set()
        # increment all by 1
        octopus_map += 1
        # check for those above 9 and add to flashers
        new_flashers = set(zip(np.where(octopus_map > 9)[0], np.where(octopus_map > 9)[1]))
        
        

        while new_flashers:
            # get element of the new flashers
            cur_flasher = new_flashers.pop()
            
            # if it's already been flashed, continue
            if cur_flasher in flashers:
                continue
            # else add to our list of flashers and process it
            else:
                flashers.add(cur_flasher)
                # increment it's neighbors
                octopus_map = inc_neighbors(octopus_map, cur_flasher)
                flashed_neighbors = set(zip(np.where(octopus_map > 9)[0], np.where(octopus_map > 9)[1]))
                new_flashers.update(flashed_neighbors)
                new_flashers = new_flashers.difference(flashers)
            # print(octopus_map)
        
        octopus_map = reset_octopus(octopus_map)
        # print(octopus_map)
        flash_total += len(flashers)
        print(f'RND {x}  Total Flashes: {len(flashers)}')
        if len(flashers) == 100:
            print(f'RND {x} has all 100 flash!')
            break


        # rest all flashers to 0
    print(f'****************\nFinal flash count: {flash_total}')
    
        







'''
import numpy as np
a = np.asarray([[1,2],[3,4]])
'''
