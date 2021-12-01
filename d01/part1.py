def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2021\\d01\\input.txt')

prev = 0
c = 0
for index, i in enumerate(lines):
    i = i.strip()
    i = int(i)
    if i > prev and index > 0:
        c += 1
    prev = i

print(c)
