import functools
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

player1 = 0
player2 = 0
player1_pos = int(lines[0][-1])
player2_pos = int(lines[1][-1])
current = '1'

@functools.cache
def recurse(current, player1, player2, player1_pos, player2_pos):
    player1_wins = 0
    player2_wins = 0

    for i in [1,2,3]:
        for j in [1,2,3]:
            for k in [1,2,3]:
                current_roll = i + j + k
                if current == '1':
                    new_player1_pos = ((player1_pos + current_roll) % 10)
                    if new_player1_pos == 0:
                        new_player1_pos = 10
                    new_player1 = new_player1_pos + player1
                    if new_player1 >= 21:
                        player1_wins += 1
                    else:
                        rec1_wins, rec2_wins = recurse('2', new_player1,
                            player2, new_player1_pos, player2_pos)
                        player1_wins += rec1_wins
                        player2_wins += rec2_wins
                else:
                    new_player2_pos = ((player2_pos + current_roll) % 10)
                    if new_player2_pos == 0:
                        new_player2_pos = 10
                    new_player2 = new_player2_pos + player2
                    if new_player2 >= 21:
                        player2_wins += 1
                    else:
                        rec1_wins, rec2_wins = recurse('1', player1,
                            new_player2, player1_pos, new_player2_pos)
                        player1_wins += rec1_wins
                        player2_wins += rec2_wins

    return (player1_wins, player2_wins)



print(max(recurse(current, player1, player2, player1_pos, player2_pos)))
