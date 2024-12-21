from functools import cache
from itertools import groupby
import fileinput
import networkx as nx

dirs = {(-1, 0): '<', (1, 0): '>', (0, -1): '^', (0, 1): 'v'}
numpad = ['789', '456', '123', ' 0A']
dirpad = [' ^A', '<v>']

def make_graph(pad):
    G = nx.DiGraph()
    w, h = len(pad[0]), len(pad)
    for y, row in enumerate(pad):
        for x, src in enumerate(row):
            for (dx, dy), d in dirs.items():
                ax, ay = x + dx, y + dy
                if ax < 0 or ay < 0 or ax >= w or ay >= h:
                    continue
                dst = pad[ay][ax]
                if src == ' ' or dst == ' ':
                    continue
                G.add_edge(src, dst, d=d)
    return G

N = make_graph(numpad)
D = make_graph(dirpad)

def get_paths(G, src, dst):
    for p in nx.all_shortest_paths(G, src, dst):
        p = ''.join(G[a][b]['d'] for a, b in zip(p, p[1:]))
        s = [k for k, g in groupby(p)]
        if len(s) == len(set(s)):
            yield p

def search(G, path, buf):
    if len(path) < 2:
        yield ''.join(buf)
        return
    for p in get_paths(G, path[0], path[1]):
        buf.append(p + 'A')
        yield from search(G, path[1:], buf)
        buf.pop()

def get_num(path):
    yield from search(N, 'A' + path, [])

def get_dir(path, depth):
    if depth == 0:
        yield from search(D, 'A' + path, [])
    else:
        for p in search(D, 'A' + path, []):
            yield from get_dir(p, depth - 1)

@cache
def expand(path, depth):
    if depth == 0:
        return len(path)
    t = 0
    for p in path.rstrip('A').split('A'):
        t += min(expand(x, depth - 1) for x in get_dir(p + 'A', 0))
    return t

t = 0
for line in fileinput.input():
    line = line.rstrip()
    x = int(line[:-1])
    n = min(expand(a, 25) for a in get_num(line))
    # print(n, x, n * x)
    t += n * x
print(t)
