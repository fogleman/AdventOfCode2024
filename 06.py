import fileinput

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid = [line.rstrip() for line in fileinput.input()]
w, h = len(grid[0]), len(grid)
get = lambda x, y: '' if x < 0 or y < 0 or x >= w or y >= h else grid[y][x]
step = lambda x, y, d: (x + DIRS[d][0], y + DIRS[d][1])
start = [(x, y, 0) for y in range(h) for x in range(w) if get(x, y) == '^'][0]

def search(p):
    x, y, d = start
    seen = set()
    while True:
        if get(x, y) == '':
            return len({(x, y) for x, y, d in seen})
        if (x, y, d) in seen or seen.add((x, y, d)):
            return 0
        n = step(x, y, d)
        while get(*n) == '#' or n == p:
            d = (d + 1) % 4
            n = step(x, y, d)
        x, y = n

print(search(None))
print(sum(search((x, y)) == 0 for y in range(h) for x in range(w)))
