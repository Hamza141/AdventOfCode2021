import heapq
import sys
from collections import defaultdict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d17\\input.txt')
xs = lines[0].split()[2][:-1]
ys = lines[0].split()[3]
x_min = int(xs.split('..')[0][2:])
x_max = int(xs.split('..')[1])
y_min = int(ys.split('..')[0][2:])
y_max = int(ys.split('..')[1])


def step(x, y, x_vel, y_vel):
    x += x_vel
    y += y_vel
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
    y_vel -= 1
    return x, y, x_vel, y_vel


ans = -sys.maxsize - 1
for i in range(0, x_max + 1):
    for j in range(y_min, abs(y_min)):
        x, y = 0, 0
        x_vel = i
        y_vel = j
        highest_y = y

        while x < x_max and y > y_min:
            x, y, x_vel, y_vel = step(x, y, x_vel, y_vel)

            if y > highest_y:
                highest_y = y
            if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
                if highest_y > ans:
                    ans = highest_y

print(ans)
