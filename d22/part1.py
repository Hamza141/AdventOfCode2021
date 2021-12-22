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

on = set()

for l in lines:
    l = l.split()
    coords = l[1].split(',')
    x = coords[0].split('=')[1].split('..')
    y = coords[1].split('=')[1].split('..')
    z = coords[2].split('=')[1].split('..')
    if l[0] == 'on':
        for i in range(max(-50, int(x[0])), min(int(x[1])+1, 51)):
            for j in range(max(-50, int(y[0])), min(int(y[1])+1, 51)):
                for k in range(max(-50, int(z[0])), min(int(z[1])+1, 51)):
                    on.add((i, j, k))
    else:
        for i in range(max(-50, int(x[0])), min(int(x[1])+1, 51)):
            for j in range(max(-50, int(y[0])), min(int(y[1])+1, 51)):
                for k in range(max(-50, int(z[0])), min(int(z[1])+1, 51)):
                    key = (i, j, k)
                    if key in on:
                        on.remove((i, j, k))

print(len(on))
