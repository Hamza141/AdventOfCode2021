def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d10\\input.txt')


def scores(c):
    if c == ')':
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137


points = 0
for line in lines:
    stack = []
    for c in line:
        if c == '[' or c == '(' or c == '{' or c == '<':
            stack.append(c)
        else:
            d = stack[-1]
            if d == '[' and c != ']':
                points += scores(c)
                break

            elif d == '(' and c != ')':
                points += scores(c)
                break

            elif d == '{' and c != '}':
                points += scores(c)
                break

            elif d == '<' and c != '>':
                points += scores(c)
                break
            else:
                stack.pop()

print(points)
