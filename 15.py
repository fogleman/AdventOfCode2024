from collections import *
from functools import *
from itertools import *
from math import *
import fileinput
import re

DIRS = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1),
}

data = ''.join(fileinput.input())

data = data.replace('#', '##')
data = data.replace('O', '[]')
data = data.replace('.', '..')
data = data.replace('@', '@.')

grid, dirs = data.split('\n\n')
dirs = ''.join(dirs.split())
grid = [list(line.rstrip()) for line in grid.split('\n')]
w, h = len(grid[0]), len(grid)
get = lambda x, y: '#' if x < 0 or y < 0 or x >= w or y >= h else grid[y][x]
sx, sy = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == '@'][0]
grid[sy][sx] = '.'

def setc(x, y, c):
    grid[y][x] = c

def can_move(x, y, d):
    dx, dy = DIRS[d]
    x, y = x + dx, y + dy
    if get(x, y) == '#':
        return False
    elif get(x, y) == '.':
        return True
    elif dx:
        return can_move(x, y, d)
    elif get(x, y) == '[':
        return can_move(x, y, d) and can_move(x+1, y, d)
    elif get(x, y) == ']':
        return can_move(x, y, d) and can_move(x-1, y, d)
    else:
        raise

def do_move(x, y, d, C, seen, erase):
    # if (x, y) in seen:
    #     return
    # seen.add((x, y))
    dx, dy = DIRS[d]
    c = get(x, y)
    x, y = x + dx, y + dy
    if get(x, y) == '#':
        pass
    elif get(x, y) == '.':
        pass
    elif dx:
        do_move(x, y, d, c, seen, erase)
    elif get(x, y) == '[':
        do_move(x, y, d, c, seen, erase)
        do_move(x+1, y, d, '.', seen, erase)
        erase.add((x+1,y))
    elif get(x, y) == ']':
        do_move(x, y, d, c, seen, erase)
        do_move(x-1, y, d, '.', seen, erase)
        erase.add((x-1,y))
    else:
        raise
    # setc(x, y, C)
    seen[(x, y)] = c
    return x, y

def display(px, py):
    for y in range(h):
        for x in range(w):
            if (x, y) == (px, py):
                print('@', end='')
            else:
                print(get(x, y), end='')
        print()
    print()

def score():
    total = 0
    for y in range(h):
        for x in range(w):
            if get(x, y) == '[':
                total += y * 100 + x
    return total

x, y = sx, sy
for d in dirs:
    if can_move(x, y, d):
        seen = {}
        erase = set()
        x, y = do_move(x, y, d, '.', seen, erase)
        for (px, py), c in seen.items():
            setc(px, py, c)
        for (px, py) in erase:
            if (px, py) not in seen:
                setc(px, py, '.')
    # display(x, y)

print(score())
