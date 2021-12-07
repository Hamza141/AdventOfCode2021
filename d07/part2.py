from collections import defaultdict
import sys


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d07\\input.txt')

crabs = [int(c) for c in lines[0].split(',')]

counts = defaultdict(int)

for c in crabs:
    counts[c] += 1


def new_cost(move):
    if move == 0:
        return 0
    return sum(range(move+1))


min_fuel = sys.maxsize
for i in range(max(counts.keys())):
    new_fuel = 0
    for j in counts.keys():
        c = counts[j]
        new_fuel += (new_cost(abs(i-j)) * c)
    if new_fuel < min_fuel:
        min_fuel = new_fuel


print(min_fuel)
