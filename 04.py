import fileinput
import re

grid = [line.rstrip() for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

get = lambda x, y: '.' if x < 0 or y < 0 or x >= w or y >= h else grid[y][x]
gets = lambda x, y, d: ''.join(get(x + dx, y + dy) for dx, dy in d)

print(sum(gets(x, y, [(dx * i, dy * i) for i in range(4)]) == 'XMAS'
    for y in range(h) for x in range(w) for dy in [-1, 0, 1] for dx in [-1, 0, 1]))

print(sum(gets(x, y, [(-1, -1), (0, 0), (1, 1)]) in ['MAS', 'SAM'] and
    gets(x, y, [(-1, 1), (0, 0), (1, -1)]) in ['MAS', 'SAM']
        for y in range(h) for x in range(w)))
