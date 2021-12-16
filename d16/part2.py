import heapq
import sys
from collections import defaultdict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d16\\input.txt')


def parse_literal(binary):
    i = 0
    end = False
    literal_vals = ''
    while not end:
        if binary[i] == '0':
            end = True
        literal_val = binary[i+1:i+5]
        literal_vals += literal_val
        i += 5
    return int(literal_vals, 2), i


binary = ''
for c in lines[0]:
    binary += format(int(c, 16), '04b')


def calculate(packet_type_ID, subpacket_values):
    if packet_type_ID == 0:
        return sum(subpacket_values)

    if packet_type_ID == 1:
        ans = 1
        for i in subpacket_values:
            ans *= i
        return ans

    if packet_type_ID == 2:
        return min(subpacket_values)

    if packet_type_ID == 3:
        return max(subpacket_values)

    if packet_type_ID == 5:
        return 1 if subpacket_values[0] > subpacket_values[1] else 0

    if packet_type_ID == 6:
        return 1 if subpacket_values[0] < subpacket_values[1] else 0

    if packet_type_ID == 7:
        return 1 if subpacket_values[0] == subpacket_values[1] else 0


def parse_packet(binary):
    packet_version = binary[:3]
    packet_type_ID = binary[3:6]
    bits_read = 6
    if packet_type_ID == '100':
        ans, subpacket_bits_read = parse_literal(binary[bits_read:])
        bits_read += subpacket_bits_read
    else:
        length_type_ID = binary[6]
        bits_read += 1
        subpacket_values = []
        if length_type_ID == '0':
            bits_read += 15
            total_length = binary[8: bits_read]
            start = 0
            bits_left = int(total_length, 2)
            while bits_left > 0:
                subpacket_ans, subpacket_bits_read = parse_packet(
                    binary[bits_read:bits_read + bits_left])
                start += subpacket_bits_read
                subpacket_values.append(subpacket_ans)
                bits_read += subpacket_bits_read
                bits_left -= subpacket_bits_read
            return calculate(int(packet_type_ID, 2), subpacket_values), bits_read
        elif length_type_ID == '1':
            bits_read += 11
            number_of_subpackets = binary[8: bits_read]
            for _ in range(int(number_of_subpackets, 2)):
                subpacket_ans, subpacket_bits_read = parse_packet(
                    binary[bits_read:])
                subpacket_values.append(subpacket_ans)
                bits_read += subpacket_bits_read
            return calculate(int(packet_type_ID, 2), subpacket_values), bits_read

    return ans, bits_read


ans = parse_packet(binary)[0]
print(ans)
