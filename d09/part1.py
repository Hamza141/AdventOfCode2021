def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d09\\input.txt')

board = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        board[i][j] = int(lines[i][j])

count = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        point = board[i][j]
        low = True
        if i + 1 < len(lines) and board[i + 1][j] <= point:
            low = False
        elif j + 1 < len(lines[0]) and board[i][j + 1] <= point:
            low = False
        elif i - 1 >= 0 and board[i - 1][j] <= point:
            low = False
        elif j - 1 >= 0 and board[i][j - 1] <= point:
            low = False
        if low:
            count += point + 1

print(count)
