from typing import DefaultDict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d03\\input.txt')

gamma = ''
epsilon = ''
for index in range(len(lines[0])):
    count_one = 0
    for l in lines:
        if l[index] == '0':
            count_one += 1
    if count_one > len(lines) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
print(gamma, epsilon)
print(int(gamma, 2) * int(epsilon, 2))
