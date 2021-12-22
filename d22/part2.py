import collections
import math
import re
import heapq
import sys
from collections import defaultdict
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


d = dirname(dirname(abspath(__file__)))

lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

on = collections.Counter()

for l in lines:
    l = l.split()
    coords = l[1].split(',')
    x = coords[0].split('=')[1].split('..')
    y = coords[1].split('=')[1].split('..')
    z = coords[2].split('=')[1].split('..')
    x_min = int(x[0])
    x_max = int(x[1])
    y_min = int(y[0])
    y_max = int(y[1])
    z_min = int(z[0])
    z_max = int(z[1])
    new_on = collections.Counter()
    for cube, value in on.items():
        n_x_min = max(x_min, cube[0])
        n_x_max = min(x_max, cube[1])
        n_y_min = max(y_min, cube[2])
        n_y_max = min(y_max, cube[3])
        n_z_min = max(z_min, cube[4])
        n_z_max = min(z_max, cube[5])
        if n_x_min <= n_x_max and n_y_min <= n_y_max and n_z_min <= n_z_max:
            new_on[(n_x_min, n_x_max, n_y_min, n_y_max, n_z_min, n_z_max)] -= value
    if l[0] == 'on':
        new_on[(x_min, x_max, y_min, y_max, z_min, z_max)] += 1
    on.update(new_on)

ans = 0
for (x_min, x_max, y_min, y_max, z_min, z_max), value in on.items():
    ans += ((x_max - x_min + 1) * (y_max - y_min + 1)
            * (z_max - z_min + 1) * value)
print(ans)
