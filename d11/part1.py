def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d11\\input.txt')

grid = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        grid[i][j] = int(lines[i][j])


flashes = 0
for _ in range(100):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            grid[i][j] += 1

    flash = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
    left = True
    while left:
        left = False
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if grid[i][j] > 9 and not flash[i][j]:
                    flash[i][j] = True
                    if i - 1 >= 0:
                        grid[i-1][j] += 1
                    if i + 1 < 10:
                        grid[i+1][j] += 1
                    if j - 1 >= 0:
                        grid[i][j-1] += 1
                    if j + 1 < 10:
                        grid[i][j+1] += 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        grid[i-1][j-1] += 1
                    if i + 1 < 10 and j + 1 < 10:
                        grid[i+1][j+1] += 1
                    if j - 1 >= 0 and i + 1 < 10:
                        grid[i + 1][j-1] += 1
                    if j + 1 < 10 and i - 1 >= 0:
                        grid[i-1][j+1] += 1
            for i in range(len(lines)):
                for j in range(len(lines[0])):
                    if grid[i][j] > 9 and not flash[i][j]:
                        left = True
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if grid[i][j] > 9:
                flashes += 1
                grid[i][j] = 0

print(flashes)
