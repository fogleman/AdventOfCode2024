from collections import *
from itertools import *
from math import *
import fileinput
import re

total = 0
grid = []
for line in fileinput.input():
    line = line.rstrip()
    grid.append(line)

w = len(grid[0])
h = len(grid)

def search(grid, x, y, path, deltas, pos, As):
    if not all(q == deltas[0] for q in deltas):
        return 0
    word = ''.join(path)
    if word == 'MAS':
        # print(pos)
        As[pos[-2]] += 1
        return 1
    if not 'MAS'.startswith(word):
        return 0
    if len(word) >= 3:
        return 0
    if x < 0 or y < 0 or x >= w or y >= h:
        return 0
    # print(path, pos, x, y)
    result = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 or dy == 0:
                continue
            if dx == 0 and dy == 0:
                continue
            deltas.append((dx, dy))
            path.append(grid[y][x])
            pos.append((x, y))
            result += search(grid, x + dx, y + dy, path, deltas, pos, As)
            deltas.pop()
            path.pop()
            pos.pop()
    return result

As = defaultdict(int)
for y in range(h):
    for x in range(w):
        total += search(grid, x, y, [], [], [], As)

print(total)
print(sum(x == 2 for x in As.values()))
