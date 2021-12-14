from collections import defaultdict
import copy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d14\\input.txt')

rules = {}
for l in lines[2:]:
    l = l.split(' -> ')
    rules[l[0]] = l[1]

pairs = defaultdict(int)
for i in range(len(lines[0]) - 1):
    pairs[lines[0][i:i+2]] += 1


for step in range(40):
    new_pairs = defaultdict(int)
    for pair, count in pairs.items():
        if pair in rules:
            c = rules[pair]
            new_pairs[pair[0] + c] += count
            new_pairs[c + pair[1]] += count
        else:
            new_pairs[pair] = count
    pairs = copy.deepcopy(new_pairs)


occ = defaultdict(int)
for pair in pairs:
    for c in pair:
        occ[c] += pairs[pair]
occ[lines[0][0]] += 1
occ[lines[0][-1]] += 1

l = sorted(occ.values())

print((l[-1] - l[0]) // 2)
