from utils import get_input_file
from collections import Counter



if __name__ == '__main__':
    lines = [list(map(int, line.replace(' -> ', ',').split(','))) for line in get_input_file('05.txt')]

    points = Counter()


    for line in lines:
        a = line[0], line[1]
        b = line[2], line[3]
        print(a, b)

        # horizontal
        if a[1] == b[1]:
            y = a[1]
            start = min(a[0], b[0])
            end = max(a[0], b[0])

            for x in range(start, end+1):
                points[x,y] +=1 

            print(start, end)
        # vertical
        elif a[0] == b[0]:
            x = a[0]
            start = min(a[1], b[1])
            end = max(a[1], b[1])

            for y in range(start, end+1):
                points[x,y] += 1
            
            print(start, end)
        else:
            x_start = a[0] if a[0] < b[0] else b[0]
            y_start = a[1] if a[0] < b[0] else b[1]
            x_stop = b[0] if a[0] < b[0] else a[0] 
            y_stop = b[1] if a[0] < b[0] else a[1]

            y = y_start
            for x in range(x_start, x_stop+1):
                points[x,y] += 1
                y = y + 1 if y_start < y_stop else y - 1
            



    cnt = 0
    for k, v in points.items():
        if v >= 2:
            cnt += 1
        
    
    print(cnt)