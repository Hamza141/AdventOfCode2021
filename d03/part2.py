def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d03\\input.txt')


def most_common(line_set):
    common = ''
    for index in range(len(lines[0])):
        count = 0
        for l in line_set:
            if l[index] == '1':
                count += 1
        if count >= len(line_set) / 2:
            common += '1'
        else:
            common += '0'

    return common


line_set = set(lines)
generator = ''
bit = 0
while len(line_set) > 1:
    common = most_common(line_set)

    for l in lines:
        if l in line_set and l[bit] != common[bit]:
            line_set.remove(l)
    bit += 1

generator = line_set.pop()
print(generator)


def least_common(line_set):
    common = ''
    for index in range(len(lines[0])):
        count = 0
        for l in line_set:
            if l[index] == '0':
                count += 1
        if count <= len(line_set) / 2:
            common += '0'
        else:
            common += '1'

    return common


line_set = set(lines)
scrubber = ''
bit = 0
while len(line_set) > 1:
    common = least_common(line_set)

    for l in lines:
        if l in line_set and l[bit] != common[bit]:
            line_set.remove(l)
    bit += 1

scrubber = line_set.pop()
print(scrubber)

print(int(generator, 2) * int(scrubber, 2))
