from collections import defaultdict
from typing import DefaultDict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d14\\input.txt')

ans = lines[0]
rules = []

for l in lines[2:]:
    l = l.split(' -> ')
    rules.append((l[0], l[1]))
del l
del lines

for _ in range(10):
    current = ans
    index = 0
    for i in range(len(ans) - 1):
        c = ans[i]
        d = ans[i+1]
        for r in rules:
            if c == r[0][0] and d == r[0][1]:
                index += 1
                current = current[:index] + r[1] + current[index:]
        index += 1
    ans = current

occ = defaultdict(int)
for c in ans:
    occ[c] += 1

l = sorted(occ.values())

print(l[-1] - l[0])
