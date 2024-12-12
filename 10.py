from collections import *
from functools import *
from itertools import *
from math import *
import fileinput
import re

grid = [tuple(map(int, line.rstrip())) for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def search(x, y, e, seen):
    if x < 0 or y < 0 or x >= w or y >= h:
        return 0
    H = grid[y][x]
    if e != H:
        return 0
    if H == 9:
        seen.add((x, y))
        return 1
    result = 0
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        result += search(nx, ny, e + 1, seen)
    return result

total = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == 0:
            seen = set()
            score = search(x, y, 0, seen)
            total += score#len(seen)
print(total)