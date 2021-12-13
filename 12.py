from utils import get_input_file

from collections import defaultdict, Counter

def print_graph(graph):
    for k, v in graph.items():
        print(f'{k}: {v}')


def get_no_gos(cur_path):
    # cannot go back to start
    # cannot go back to any lowercase cave in the current path
    no_gos = set([node for node in cur_path if node.islower()])
    
    return no_gos


def get_no_gos2(cur_path):

    no_gos = set(['start'])
    node_cnt = Counter(cur_path)
    # print(node_cnt)
    for node, cnt in node_cnt.items():
        # is it a small cave, not start or end, that is already in here 2x?
        if node.islower() and node != 'start' and cnt > 1:
            no_gos.update([node for node in cur_path if node.islower()])
            break


    return no_gos

if __name__ == '__main__':
    contents = get_input_file('12.txt')

    graph = defaultdict(list)

    for line in contents:
        start, stop = line.split('-')
        graph[stop].append(start)

        graph[start].append(stop)
    
    print_graph(graph)

    open_paths = []
    final_paths = []

    # create initial paths originating from start
    for v in graph['start']:
        open_paths.append(['start', v])


    while open_paths:
        cur_path = open_paths.pop()
        last_node = cur_path[-1]
        # print(f'Current path is {cur_path}, last node is {last_node}')
        connections = set(graph[last_node])
        # print(f'{last_node} connects to {connections}')
        no_gos = get_no_gos2(cur_path)
        # print(f'These nodes cannot be readded {no_gos}')
        next_steps = connections.difference(no_gos)
        # print(f'The valid next nodes are then {next_steps}')

        for node in next_steps:
            tmp_path = list(cur_path)
            tmp_path.append(node)
            # print(f'New path is {tmp_path}')
            if node == 'end':
                final_paths.append(tmp_path)
            else:
                open_paths.append(tmp_path)
        
        print(f'Open paths remaining: {len(open_paths)}')

    print(f'There are {len(final_paths)} final paths')