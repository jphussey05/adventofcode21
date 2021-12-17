from collections import defaultdict
from queue import PriorityQueue
from utils import get_input_file
from pprint import pprint
import networkx as nx


def build_graph(contents):
    print(f'Building Graph')
    width = len(contents[0])
    height = len(contents)

    print(f'Graph is {width} wide by {height} high')
    graph = defaultdict(dict)

    edges = []

    # need to build edges in all directions
    for ridx, row in enumerate(contents):
        for cidx, val in enumerate(row):
            # right only if cidx is not width - 1
            if cidx != width - 1:
                edges.append([(ridx, cidx), (ridx, cidx + 1)])
            # left only if cidx is not zero
            if cidx > 0:
                edges.append([(ridx, cidx), (ridx, cidx - 1)])
            # up
            if ridx > 0:
                edges.append([(ridx, cidx), (ridx - 1, cidx)])
            # down
            if ridx != height - 1:
                edges.append([(ridx, cidx), (ridx + 1, cidx)])


    for edge in edges:
        # creates a dictionary entrace for a vertex
        # adds a connected vertex to sub dict with a weight as the value
        # e.g., (1, 0): {(0, 0): '1', (1, 1): '3', (2, 0): '2'},
        graph[edge[0]][edge[1]] = int(contents[edge[1][0]][edge[1][1]])
        graph[edge[1]][edge[0]] = int(contents[edge[0][0]][edge[0][1]])
    # pprint(graph)

    print(f'Graph Built!')

    return graph


def dijkstra(graph):
    print(f'Starting SPF')
    visited = []

    # initialize distances to infinity and start to 0
    D = {vertex:float('inf') for vertex in graph.keys()}
    D[(0,0)] = 0
    # print('dist', D)
    
    # create a queue and put start in it
    pq = PriorityQueue()
    pq.put((0, (0,0)))
    # print('queue', pq.queue)

    while not pq.empty():
        print(f'Length of queue is {pq.qsize()})')
        dist, cur_vertex = pq.get()
        # print(f'visiting vertex {cur_vertex}, dist is {dist}')
        visited.append(cur_vertex)

        neighbors = [neighbor for neighbor in graph[cur_vertex] if neighbor not in visited]
        for neighbor in neighbors:
            distance = graph[cur_vertex][neighbor]
            # print(f'{neighbor} is a neighbor at a cost of {distance}')
            
            
            old_cost = D[neighbor]
            new_cost = D[cur_vertex] + distance

            if new_cost < old_cost:
                pq.put((new_cost, neighbor))
                D[neighbor] = new_cost
            # print(f'Old cost to {neighbor} was {old_cost}\nNew cost to {neighbor} is {new_cost}')
            


    
    print(D)


def add_one_wrap(num):
    num = str(int(num) + 1)
    return num if num != '10' else '1'
    

def get_new_block(block):
    # print(block)
    new_block = []
    for row in block:
        tmp = list(map(add_one_wrap, row))
        new_block.append(''.join(tmp))

    return new_block


def expand_map(contents):
    new_map = list(contents)
    length = len(new_map)
    
    # print(new_map[-10:])
    # build new rows below
    for _ in range(4):
        new_map.extend(get_new_block(new_map[-length:]))
    
    print(f'After expanding down: {len(new_map)}')
    # expand each row
    new_block = list(new_map)
    for _ in range(4):
        new_block = get_new_block([line[-length:] for line in new_map])
        for idx, new_row in enumerate(new_block):
            new_map[idx] += str(new_row)
        

    # pprint(new_map)
    return new_map

    
def build_graph_nx(graph):
    G = nx.DiGraph()

    for vert, neighbors in graph.items():
        
        for neighbor, weight in neighbors.items():
            # print(f'Neighbor {neighbor} with weight {weight}')
            
            G.add_edge(vert, neighbor, weight=weight)
    
    return G
    
if __name__ == '__main__':
    contents = get_input_file('15.txt')

    
    contents = expand_map(contents)
    graph = build_graph(contents)
    graph_nx = build_graph_nx(graph)

    sp = nx.dijkstra_path(graph_nx, (0,0), (499,499))
    print(sp)

    cost = 0
    for idx, node in enumerate(sp[:-1]):
        cost += graph[node][sp[idx+1]]

    print(cost)

    exit()

    spf = dijkstra(graph)