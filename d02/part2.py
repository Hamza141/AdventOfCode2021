def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d02\\input.txt')

x = 0
y = 0
aim = 0
for l in lines:
    l = l.split()
    d = l[0]
    if d == 'forward':
        x += int(l[1])
        y += (int(l[1]) * aim)
    elif d == 'down':
        aim += int(l[1])
    elif d == 'up':
        aim -= int(l[1])

print(abs(x * y))
