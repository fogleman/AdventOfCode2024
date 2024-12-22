from collections import *
from functools import *
from itertools import *
from math import *
import fileinput
import re
import networkx as nx
# import numpy as np

def ints(s):
    return list(map(int, re.findall(r'-?\d+', s)))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# grid = [line.rstrip() for line in fileinput.input()]
# w, h = len(grid[0]), len(grid)
# get = lambda x, y: '.' if x < 0 or y < 0 or x >= w or y >= h else grid[y][x]

data = ''.join(fileinput.input())

for i in range(2500, 5000):
    walls = set()
    for j, line in enumerate(data.split('\n')):
        if not line:
            continue
        x, y = ints(line)
        walls.add((x, y))
        if len(walls) == i:
            break

    N = 70
    S = (0, 0)
    E = (N, N)
    G = nx.DiGraph()
    for y in range(N+1):
        for x in range(N+1):
            for dx, dy in dirs:
                mx, ny = x + dx, y + dy
                if mx < 0 or ny < 0 or mx > N or ny > N:
                    continue
                if (x, y) in walls or (mx, ny) in walls:
                    continue
                G.add_edge((x, y), (mx, ny))
                # print(x, y, mx, ny)

    print(i, data.split('\n')[i-1])
    print(i, nx.shortest_path_length(G, S, E))

    # for y in range(N+1):
    #     for x in range(N+1):
    #         if (x, y) in walls:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
