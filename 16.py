
from utils import get_input_file




def process_pkt(pkt):
    # recursive processing of packets
    #
    version = int(pkt[:3], base=2)
    type_id = int(pkt[3:6], base=2)
    pkt_len = 6
    print(f'-------------------------\nReceived {len(pkt)}: {pkt}')
    print(f'Version: {version}, Type: {type_id}')

    if type_id == 4:
        # for a literal packet, read until the leading packet is a zero
        print(f'Base Case: A literal packet!')
        nib_cnt = 1
        idx = 6
        while pkt[idx] == '1':
            nib_cnt += 1
            idx += 5
        
        # we just trash leading zeros so don't have to worry about them here
        value = ''
        for start in list(range(6, 6 + nib_cnt * 5, 5)):
            value += pkt[start+1:start+5]
            pkt_len += 5
        
        print(f'Raw value of packet was: {int(value, base=2)}')
        print(f'packet was {pkt_len} bits long')
        return int(value, base=2), pkt_len
    else:
        print(f'Recursive Case: An operator packet!')
        len_type = pkt[6]
        print(f'Length Type ID: {len_type}')
        if len_type == '1':
            # type 1 means we track the # of packets
            num_packets = int(pkt[7:18], base=2)
            print(f'The number of sub-packets is {num_packets}')
            
            # initialize version total (for part 1 only)
            sub_packet_total = version
            # init total operator packet length 
            op_packet_length = 18
            sub_pkt_len = 0
            sub_pkts = list()

            # modify the pkt we pass down the stacks
            pkt = pkt[18:]
            while num_packets > 0:
                # we need to spawn 3 packet cleans

                print(f'{num_packets} packets remaining')
                print(f'Passing {pkt} down...')
                
                sub_pkt_value, sub_pkt_len = process_pkt(pkt)
                print(f'Sub packet value was {sub_pkt_value}, length used {sub_pkt_len}')
                pkt = pkt[sub_pkt_len:]
                print(f'Total Bits remaining are: {len(pkt)}')

                op_packet_length += sub_pkt_len
                print(f'Total bits for this operator parent packet: {op_packet_length}')
                sub_pkts.append(sub_pkt_value)
                num_packets -= 1
            
        elif len_type == '0':
            num_bits = int(pkt[7:22], base=2)
            print(f'The number of bits for sub-packets is {num_bits}')
            sub_packet_total = version
            op_packet_length = 22
            sub_pkt_len = 0
            sub_pkts = list()
            pkt = pkt[22:]
            while num_bits > 0:
                # we need to spawn packets until we've consumed all bits

                print(f'{num_bits} bits remaining')
                print(f'Passing {pkt} down...')
                
                sub_pkt_value, sub_pkt_len = process_pkt(pkt)
                print(f'Sub packet value was {sub_pkt_value}, length used {sub_pkt_len}')
                pkt = pkt[sub_pkt_len:]
                print(f'Total Bits remaining are: {len(pkt)}')

                op_packet_length += sub_pkt_len
                print(f'Total bits for this operator parent packet: {op_packet_length}')
                sub_pkts.append(sub_pkt_value)
                num_bits -= sub_pkt_len
        

        # check the type and do the things here for returning values?

        # operator packets no longer need to return any version information

        print(f'Returning type id {type_id} of {sub_pkts}')
        print(f'Op_packet length: {op_packet_length}')
        if type_id == 0:
            return sum(sub_pkts), op_packet_length
        elif type_id == 1:
            product = 1
            for pkt in sub_pkts:
                product *= pkt
            return product, op_packet_length
        elif type_id == 2:
            return min(sub_pkts), op_packet_length
        elif type_id == 3:
            return max(sub_pkts), op_packet_length
        elif type_id == 5:
            if sub_pkts[0] > sub_pkts[1]:
                return 1, op_packet_length
            else:
                return 0, op_packet_length        
        elif type_id == 6:
            if sub_pkts[0] < sub_pkts[1]:
                return 1, op_packet_length
            else:
                return 0, op_packet_length        
        elif type_id == 7:
            if sub_pkts[0] == sub_pkts[1]:
                return 1, op_packet_length
            else:
                return 0, op_packet_length

        # return sub_packet_total, op_packet_length



#   100|010|1|00000000001|001|010|1|00000000001|101|010|0|000000000001011|110|100|01111|000
#    v4 op  1    1 pkt    v1   op 1    1 pkt     v5 op  0        11        v6 lit  15    ignore

# 111|011|1|00000000011|010|100|00001|100|100|00010|001|100|00011|00000
#  v7  op 1   3 pkt      v2 lit  val1  v4 lit  val2  v1 lit  val3


if __name__ == '__main__':
    contents = get_input_file('16.txt')[0].strip()

    
    binary = (bin(int(contents, base=16))[2:]).zfill(len(contents) * 4)
    
    print(contents, binary)

    value = process_pkt(binary)

    print(f'The value is {value[0]}')



#TODO I think my method is stripping leading zeros
# 100 000 0 000001011010110 | 000110011100010010000