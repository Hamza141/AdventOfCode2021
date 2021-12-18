import math
import re
import heapq
import sys
from collections import defaultdict
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


d = dirname(dirname(abspath(__file__)))

lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))


def find_depth(match, current):
    current_depth = 0
    n = len(current)

    for i in range(n):
        if current[i] == '[':
            current_depth += 1

        elif current[i] == ']':
            if current_depth > 0:
                current_depth -= 1
            else:
                print("ERROR")
                return False

        if i >= match[0] and i < match[1] and current_depth >= 5:
            return True

    return False


def check_nested_pairs(current):
    new_current = list(current)
    pattern = re.compile('[0-9]+(,[0-9]+)*')
    matches = [m.span() for m in re.finditer(pattern, current)]
    for i, match in enumerate(matches):
        if len(match) != 2:
            continue
        too_deep = find_depth(match, current)
        if too_deep:
            pair = current[match[0]:match[1]]
            comma = str(pair).index(',')
            pair_first_num = int(pair[:comma])
            pair_second_num = int(pair[comma+1:])

            next_match = []
            next_pair = []
            if i + 1 < len(matches):
                next_match = matches[i+1]
                next_pair = current[next_match[0]:next_match[1]]
                if ',' in next_pair:
                    comma = str(next_pair).index(',')
                    next_new_num = int(next_pair[:comma]) + pair_second_num
                    next_new_pair = str(next_new_num) + \
                        ',' + next_pair[comma + 1:]
                else:
                    # just one num
                    next_new_pair = int(next_pair) + pair_second_num
                new_current[next_match[0]:next_match[1]] = str(next_new_pair)

            new_current[match[0]-1:match[1]+1] = '0'

            prev_match = []
            prev_pair = []
            if i > 0:
                prev_match = matches[i-1]
                prev_pair = current[prev_match[0]:prev_match[1]]
                if ',' in prev_pair:
                    comma = str(prev_pair).index(',')
                    prev_new_num = int(prev_pair[comma+1:]) + pair_first_num
                    prev_new_pair = prev_pair[:comma] + ',' + str(prev_new_num)
                else:
                    # just one num
                    prev_new_pair = int(prev_pair) + pair_first_num
                new_current[prev_match[0]:prev_match[1]] = str(prev_new_pair)

            return ''.join(new_current)
    return current


def check_ten(current):
    new_current = list(current)
    pattern = re.compile('[0-9]+(,[0-9]+)*')
    matches = [m.span() for m in re.finditer(pattern, current)]
    for match in matches:
        pair = current[match[0]:match[1]]
        nums = pair.split(',')
        for i, n in enumerate(nums):
            n = int(n)
            if n >= 10:
                new_pair = '[' + str(math.floor(n/2)) + \
                    ',' + str(math.ceil(n/2)) + ']'
                if len(nums) > 1:
                    comma = str(pair).index(',')
                    if i == 0:
                        new_current[match[0]:match[0] + comma] = new_pair
                    else:
                        new_current[match[0] + comma:match[1]] = ',' + new_pair

                else:
                    new_current[match[0]:match[1]] = new_pair
                return ''.join(new_current)
    return current


def checks(current):
    while True:
        new_current = check_nested_pairs(current)
        if current == new_current:
            new_current = check_ten(current)
        if current != new_current:
            current = new_current
            continue
        else:
            return current


index = 1
current = lines[0]
while index != len(lines):
    current = '[' + current + ',' + lines[index] + ']'
    current = checks(current)
    index += 1
current = checks(current)
print(current)


def magnitude(current):
    n = len(current)
    stack = []
    current_num = ''
    i = 0

    while i < n:
        current_char = current[i]
        if str(current_char).isdigit():
            while str(current_char).isdigit():
                current_num += current[i]
                i += 1
                current_char = current[i]
            stack.append(int(current_num))
            current_num = ''
        if current_char == ']':
            stack.append(2 * stack.pop() + 3 * stack.pop())

        i += 1

    return stack.pop()


print(magnitude(current))
