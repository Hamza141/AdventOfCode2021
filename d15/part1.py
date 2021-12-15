import heapq
import sys
from collections import defaultdict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d15\\input.txt')

board = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
dp = [[sys.maxsize for _ in range(len(lines[0]))] for _ in range(len(lines))]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        board[i][j] = int(lines[i][j])

seen = set()
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]
pq = [(0, 0, board[0][0])]
heapq.heapify(pq)
dp[0][0] = board[0][0]

while (len(pq) > 0):
    current = heapq.heappop(pq)

    i = current[1]
    j = current[2]
    if (i, j) in seen:
        continue
    seen.add((i, j))

    for k in range(4):
        new_i = i + dRow[k]
        new_j = j + dCol[k]

        if new_i < 0 or new_i >= len(board) or new_j < 0 or new_j >= len(board[0]) or (new_i, new_j) in seen:
            continue

        dp[new_i][new_j] = min(dp[new_i][new_j], dp[i]
                               [j] + board[new_i][new_j])
        heapq.heappush(pq, (dp[new_i][new_j], new_i, new_j))

print(dp[-1][-1] - dp[0][0])
