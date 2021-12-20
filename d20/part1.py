from grid import *
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

algo = lines[0]

img = lines[2:]

grid = Grid.make_grid(len(img), len(img[0]), default='.')

for i in range(len(img)):
    for j in range(len(img[0])):
        grid[i][j] = img[i][j]

outside = '.'
border_len = 2
for step in range(2):
    grid = grid.add_border(outside, border_len)
    new_grid = Grid.make_grid(grid.m, grid.n, default='.')
    for i in range(grid.n):
        for j in range(grid.m):
            pixels = grid.get_neighbors(
                i, j, coords=False, include_self=True, outside_bounds=outside)
            trans = str.maketrans(".#", "01")
            bits = ''.join(pixels).translate(trans)
            decimal = int(bits, 2)
            val = algo[decimal]
            new_grid[i][j] = val
    outside = algo[int((outside*9).translate(trans), 2)]
    grid = new_grid.copy()

print(grid.get_counter()['#'])
