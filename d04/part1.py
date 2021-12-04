from typing import DefaultDict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d04\\input.txt')

numbers = lines[0].split(',')

boards = []
b_marked = []

for line in range(2, len(lines), 6):
    board = [[0 for i in range(5)] for j in range(5)]
    marks = [[False for i in range(5)] for j in range(5)]
    for row in range(5):
        nums = lines[line+row].split()
        for col, num in enumerate(nums):
            board[row][int(col)] = int(num)
    boards.append(board)
    b_marked.append(marks)


def win(marks):
    for i in range(5):
        found = True
        for j in range(5):
            if marks[i][j] != True:
                found = False
                break
        if found:
            return True

    for j in range(5):
        found = True
        for i in range(5):
            if marks[i][j] != True:
                found = False
                break
        if found:
            return True


def mark(board, marks, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                marks[i][j] = True
                return


def unmarked_sum(board, marks):
    total = 0
    for i in range(5):
        for j in range(5):
            if not marks[i][j]:
                total += board[i][j]
    return total


for n in numbers:
    n = int(n)
    for index, board in enumerate(boards):
        mark(board, b_marked[index], n)
        if win(b_marked[index]):
            print(unmarked_sum(board, b_marked[index]) * n)
            exit(0)
