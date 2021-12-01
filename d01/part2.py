def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('E:\\Projects\\AdventOfCode2021\\d01\\input.txt')

prev = 0
c = 0
s = 0
for index, i in enumerate(lines):
    i = i.strip()
    i = int(i)
    s += i
    if index > 2:
        s -= int(lines[index-3].strip())
        if s > prev:
            c += 1
            print(s)
    prev = s

print(c)
