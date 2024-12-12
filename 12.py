import fileinput

grid = [line.rstrip() for line in fileinput.input()]
w, h = len(grid[0]), len(grid)
get = lambda x, y: '.' if x < 0 or y < 0 or x >= w or y >= h else grid[y][x]

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def score(x, y, c, seen):
    if (x, y) in seen or get(x, y) != c:
        return 0, 0
    seen.add((x, y))
    a, p = 1, 0
    for dx, dy in DIRS:
        if get(x + dx, y + dy) != c:
            p += 1
            if (dx,dy) == (0,1) and get(x+1, y) == c and get(x+1,y+1)!=c:
                p -= 1
            if (dx,dy) == (0,-1) and get(x+1, y) == c and get(x+1,y-1)!=c:
                p -= 1
            if (dx,dy) == (1,0) and get(x, y+1) == c and get(x+1,y+1)!=c:
                p -= 1
            if (dx,dy) == (-1,0) and get(x, y+1) == c and get(x-1,y+1)!=c:
                p -= 1
        else:
            result = score(x + dx, y + dy, c, seen)
            a += result[0]
            p += result[1]
    return a, p

total = 0
seen = set()
for y in range(h):
    for x in range(w):
        c = get(x, y)
        a, p = score(x, y, c, seen)
        total += a * p
print(total)
