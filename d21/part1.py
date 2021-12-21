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

roll = 1
player1 = 0
player2 = 0
player1_pos = int(lines[0][-1])
player2_pos = int(lines[1][-1])
current = '1'
while player1 < 1000 and player2 < 1000:
    current_roll = 0
    if roll >= 990:
        a = 2
    for i in range(3):
        current_roll += roll
        roll += 1
    if current == '1':
        player1_pos = ((player1_pos + current_roll) % 10)
        if player1_pos == 0:
            player1_pos = 10
        player1 += player1_pos
        current = '2'
    else:
        player2_pos = ((player2_pos + current_roll) % 10)
        if player2_pos == 0:
            player2_pos = 10
        player2 += player2_pos
        current = '1'
print(min(player1, player2) * (roll - 1))
