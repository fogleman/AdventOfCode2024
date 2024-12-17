import fileinput
import networkx as nx

grid = ''.join(fileinput.input()).split('\n')

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
G = nx.DiGraph()
S = E = None

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == 'S':
            S = (x, y, (1, 0))
        if c == 'E':
            E = (x, y)
        for d in D:
            ax, ay = x + d[0], y + d[1]
            if c == '#' or grid[ay][ax] == '#':
                continue
            to = (ax, ay) if grid[ay][ax] == 'E' else (ax, ay, d)
            for e in D:
                w = 1 if e == d else 1001
                G.add_edge((x, y, e), to, weight=w)

path = nx.shortest_path(G, S, E, 'weight')
print(nx.path_weight(G, path, 'weight'))

paths = nx.all_shortest_paths(G, S, E, 'weight')
print(len(set((p[0], p[1]) for path in paths for p in path)))
