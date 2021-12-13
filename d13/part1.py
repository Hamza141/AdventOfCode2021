def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d13\\input.txt')

paper = [[0 for _ in range(2000)] for _ in range(2000)]
folds = []

for l in lines:
    if ',' in l:
        l = l.split(',')
        x = int(l[0])
        y = int(l[1])
        paper[y][x] = 1
    elif len(l) > 0:
        l = l.split()[-1].split('=')
        folds.append((l[0], int(l[1])))
        break

range_x = 2000
range_y = 2000
for fold in folds:
    if fold[0] == 'x':
        range_x = fold[1] * 2 + 1
    else:
        range_y = fold[1] * 2 + 1
    folding = (fold[1] * 2)
    for y in range(range_y):
        for x in range(range_x):
            if paper[y][x] == 1:
                paper[y][x] = 0
                new_x = x
                new_y = y
                if fold[0] == 'x' and x >= fold[1]:
                    new_x = folding - x
                elif fold[0] == 'y' and y >= fold[1]:
                    new_y = folding - y
                paper[new_y][new_x] = 1
    if fold[0] == 'x':
        range_x = fold[1] + 1
    else:
        range_y = fold[1] + 1

count = 0
for j in range(range_y):
    for i in range(range_x):
        if paper[j][i] == 1:
            count += 1
print(count)
