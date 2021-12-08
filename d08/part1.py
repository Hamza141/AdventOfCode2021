from collections import defaultdict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d08\\input.txt')

count = 0
for l in lines:
    l = l.split(' | ')
    words = l[1].split(' ')
    for w in words:
        length = len(w)
        if length == 3 or length == 2 or length == 4 or length == 7:
            count += 1

print(count)
