from collections import *
from functools import *
from itertools import *
from math import *
import fileinput
import re

grid = [line.rstrip() for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

all_nodes = defaultdict(set)
for y in range(h):
    for x in range(w):
        c = grid[y][x]
        if c == '.':
            continue
        all_nodes[c].add((x, y))

seen = set()
for c, nodes in all_nodes.items():
    for i, a in enumerate(nodes):
        for j, b in enumerate(nodes):
            if i == j:
                continue
            ax, ay = a
            bx, by = b
            dx, dy = bx - ax, by - ay
            k = 0
            while True:
                done = True
                x0, y0 = ax - dx * k, ay - dy * k
                x1, y1 = bx + dx * k, by + dy * k
                if not (x0 < 0 or y0 < 0 or x0 >= w or y0 >= h):
                    seen.add((x0, y0))
                    done = False
                if not (x1 < 0 or y1 < 0 or x1 >= w or y1 >= h):
                    seen.add((x1, y1))
                    done = False
                k += 1
                if done:
                    break
print(len(seen))
