
from utils import get_input_file











# first three bits is packet version
# next three bits is type ID
# These two numbers are binary 










if __name__ == '__main__':
    contents = get_input_file('16-test.txt')

    
    binary = str(bin(int(contents[0].strip(), base=16)))[2:]
    
    print(contents, binary)
    pkt_len = 6
    version = int(binary[:3], base=2)
    type_id = int(binary[3:6], base=2)

    print(version, type_id)
    if type_id == 4:
        nib_cnt = 1
        idx = 6
        while True:
            if binary[idx] == '1':
                nib_cnt += 1
                idx += 5
            else:
                break
        
        # adds in the padded zeros at the end as packet has to be multiple of 4
        pkt_len = (pkt_len + nib_cnt * 5) + (4 - (pkt_len + nib_cnt *5)) % 4
        print(f'Num of nibbles is {nib_cnt}, pkt length is {pkt_len}')
        value = ''
        for start in list(range(6, 6 + nib_cnt * 5, 5)):
            value += binary[start+1:start+5]
        
        print(int(value, base=2))
    else:
        pass

