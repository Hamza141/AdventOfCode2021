from collections import defaultdict
from os import fsdecode


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d06\\input.txt')

fishies = [int(f) for f in lines[0].split(',')]
fish = defaultdict(int)
for f in fishies:
    fish[f] += 1

for day in range(80):
    growth = fish[0]
    for f in range(1, 9):
        fish[f - 1] = fish[f]
    fish[8] = growth
    fish[6] += growth

print(sum(fish.values()))
