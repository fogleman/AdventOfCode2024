import numpy as np
import fileinput
import re

def f(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    px += 10000000000000
    py += 10000000000000
    X = np.linalg.solve([[ax, bx], [ay, by]], [px, py])
    na, nb = [int(round(x)) for x in X]
    x = na * ax + nb * bx
    y = na * ay + nb * by
    if (x, y) == (px, py):
        return 3 * na + nb
    return 0

total = 0
for line in fileinput.input():
    values = list(map(int, re.findall(r'\d+', line)))
    if 'A' in line:
        A = values
    elif 'B' in line:
        B = values
    elif values:
        P = values
        total += f(A, B, P)
print(total)
