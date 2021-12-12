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
    if l[0] != 'start' and l[1] != 'end':
        graph[l[1]].append(l[0])

def dfs(graph, point, seen_so_far):
    if point == 'end':
        return [point]
    if str(point).islower() and point in seen_so_far.split(','):
        return []
    paths = set()
    for p in graph[point]:
        for path in dfs(graph, p, seen_so_far + ',' + point):
            paths.add(point + ',' + path)
    return paths

count = 0
paths = set()
for point in graph['start']:
    for path in dfs(graph, point, 'start'):
        paths.add('start' + ',' + path)
    


# print(paths)
print(len(paths))