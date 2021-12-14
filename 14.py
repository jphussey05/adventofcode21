from utils import get_input_file
from pprint import pprint
from collections import Counter
def build_map(rules):

    pair_rules = {}    
    for rule in rules:
        pair, result = rule.split(' -> ')
        pair_rules[pair] = pair[0] + result, result + pair[1]

    return pair_rules


def count_chars(pair_cnt):
    final_count = Counter()
    for pair, cnt in pair_cnt.items():
        final_count[pair[0]] += cnt / 2
        final_count[pair[1]] += cnt / 2

    return final_count

if __name__ == '__main__':
    contents = get_input_file('14.txt')

    init_chain = contents[0]
    pair_rules = build_map(contents[2:])

    # break current chain into pairs
    init_pairs = [init_chain[i] + init_chain[i+1] for i in range(len(init_chain) - 1)]
    cur_pair_cnt = Counter(init_pairs)
    print(f'Initial pairs in the chain are:')
    pprint(cur_pair_cnt)

    # translate current pairs into next step pairs (add both)
    print(f'The pair rules are:')
    pprint(pair_rules)


    for x in range(40):

        tmp = Counter()
        for pair, cnt in cur_pair_cnt.items():
            tmp[pair_rules[pair][0]] += cnt
            tmp[pair_rules[pair][1]] += cnt
        
        print(f'End of round {x+1}')
        print(f'{sum(tmp.values())} new pairs are:')
        pprint(tmp)
        cur_pair_cnt = tmp

        print(count_chars(cur_pair_cnt))
