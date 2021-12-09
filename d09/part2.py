def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d09\\input.txt')

board = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
lows = set()

for i in range(len(lines)):
    for j in range(len(lines[0])):
        board[i][j] = int(lines[i][j])

for i in range(len(lines)):
    for j in range(len(lines[0])):
        point = board[i][j]
        if point == 9:
            continue
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
            lows.add((i, j))

visited = set()


def dfs(visited, board, node):
    if node in visited:
        return 0
    i, j = node
    point = board[i][j]
    if point == 9:
        return 0
    visited.add(node)
    count = 1
    if i + 1 < len(lines) and board[i + 1][j] > point:
        count += dfs(visited, board, (i + 1, j))
    if j + 1 < len(lines[0]) and board[i][j + 1] > point:
        count += dfs(visited, board, (i, j + 1))
    if i - 1 >= 0 and board[i - 1][j] > point:
        count += dfs(visited, board, (i - 1, j))
    if j - 1 >= 0 and board[i][j - 1] > point:
        count += dfs(visited, board, (i, j - 1))
    return count


counts = []
for low in lows:
    counts.append(dfs(visited, board, low))

counts.sort()
ans = 1
for c in counts[-3:]:
    ans *= c
print(ans)
