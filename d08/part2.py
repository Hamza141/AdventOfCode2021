from itertools import permutations


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d08\\input.txt')

seqs = {0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg'}

total = 0
txt = 'abcdefg'
perms = [''.join(p) for p in permutations(txt)]
for line in lines:
    l = str(line).replace(' |', '')
    words = [''.join(sorted(w)) for w in l.split(' ')]
    sorted_words = sorted(words, key=len, reverse=True)
    for p in perms:
        translation = txt.maketrans(txt, p)
        possible = {''.join(sorted(v.translate(translation)))
                            : k for k, v in seqs.items()}
        found = True
        for w in sorted_words:
            if w not in possible.keys():
                found = False
                break
        if not found:
            continue
        l = line.split(' | ')[1]
        words = [''.join(sorted(w)) for w in l.split(' ')]
        number = ''
        for w in words:
            number += str(possible[w])
        total += int(number)

print(total)
