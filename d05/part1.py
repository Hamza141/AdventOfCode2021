from typing import DefaultDict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d05\\input.txt')

floor = [[0 for _ in range(1000)] for _ in range(1000)]

for l in lines:
    l = l.split(' -> ')
    x1 = int(l[0].split(',')[0])
    y1 = int(l[0].split(',')[1])
    x2 = int(l[1].split(',')[0])
    y2 = int(l[1].split(',')[1])
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            floor[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            floor[i][y1] += 1

count = 0
for i in range(len(floor)):
    for j in range(len(floor[0])):
        if floor[i][j] > 1:
            count += 1

print(count)
