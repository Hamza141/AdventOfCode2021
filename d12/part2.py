from collections import defaultdict
from typing import DefaultDict


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile('E:\\Projects\\AdventOfCode2021\\d12\\input.txt')

graph = DefaultDict(list)

for l in lines:
    l = l.split('-')
    graph[l[0]].append(l[1])
    graph[l[1]].append(l[0])


def dfs(graph, point, seen_so_far):
    if point == 'start':
        return []
    if point == 'end':
        return [point]
    if seen_so_far == 'start,b,A,b,A':
        a = 1

    if str(point).islower():
        splits = seen_so_far.split(',')
        lower_count = defaultdict(int)
        for s in splits:
            if s.islower():
                lower_count[s] += 1
        lower_count[point] += 1
        if lower_count[point] > 2:
            return []

        for c in lower_count.keys():
            if c == point:
                continue
            if lower_count[c] > 1 and lower_count[point] > 1:
                return []

    paths = set()
    for p in graph[point]:
        for path in dfs(graph, p, seen_so_far + ',' + point):
            paths.add(point + ',' + path)
    return paths


paths = set()
for point in graph['start']:
    seen = set()
    for path in dfs(graph, point, 'start'):
        seen.add('start')
        paths.add('start' + ',' + path)
        seen.clear()


# for p in sorted(list(paths)):
#     print(p)
print(len(paths))
