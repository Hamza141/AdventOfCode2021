from typing import SupportsComplex


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d10\\input.txt')

scores = []
for line in lines:
    incomplete = True
    stack = []
    for c in line:
        if c == '[' or c == '(' or c == '{' or c == '<':
            stack.append(c)
        else:
            d = stack[-1]
            if d == '[' and c != ']':
                incomplete = False
                break

            elif d == '(' and c != ')':
                incomplete = False
                break

            elif d == '{' and c != '}':
                incomplete = False
                break

            elif d == '<' and c != '>':
                incomplete = False
                break

            else:
                stack.pop()

    if incomplete:
        points = 0
        while len(stack) > 0:
            c = stack.pop()
            points *= 5
            if c == '(':
                points += 1

            if c == '[':
                points += 2

            if c == '{':
                points += 3

            if c == '<':
                points += 4
        scores.append(points)

scores.sort()

print(scores[int(len(scores)/2)])
