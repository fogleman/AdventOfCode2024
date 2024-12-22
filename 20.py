from collections import Counter
from functools import cache
import fileinput
import networkx as nx

grid = ''.join(fileinput.input()).split('\n')[:-1]
w, h = len(grid[0]), len(grid)
get = lambda x, y: '#' if x < 0 or y < 0 or x >= w or y >= h else grid[y][x]

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
G = nx.DiGraph()
S = E = None

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == 'S':
            S = (x, y)
        if c == 'E':
            E = (x, y)
        for d in D:
            ax, ay = x + d[0], y + d[1]
            if c == '#' or grid[ay][ax] == '#':
                continue
            G.add_edge((x, y), (ax, ay))

@cache
def cost(p):
    path = nx.shortest_path(G, p, E)
    return len(path) - 1

X = cost(S)
path = nx.shortest_path(G, S, E)
counter = Counter()
for i, p in enumerate(path):
    x, y = p
    for dx in range(-20, 21):
        for dy in range(-20, 21):
            m = abs(dx) + abs(dy)
            if m > 20:
                continue
            q = (x + dx, y + dy)
            if get(*q) == '#':
                continue
            c = i + m + cost(q)
            if c <= X - 100:
                # print(c)
                counter[X-c] += 1

# for k, v in reversed(counter.items()):
#     print(k, v)
print(sum(counter.values()))

# print(cost(S))
# path = nx.shortest_path(G, S, E)
# print(len(path) - 1)
# print(nx.path_weight(G, path, 'weight'))

# paths = nx.all_shortest_paths(G, S, E, 'weight')
# print(len(set((p[0], p[1]) for path in paths for p in path)))
