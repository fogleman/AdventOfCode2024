from collections import *
from functools import *
from itertools import *
from math import *
import fileinput
# import networkx as nx
# import numpy as np
import re
import time

w = 101
h = 103
# w = 11
# h = 7
points = []
for line in fileinput.input():
    x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
    points.append((x, y, vx, vy))

def step(points):
    result = []
    for x, y, vx, vy in points:
        x += vx
        y += vy
        if x < 0:
            x += w
        if y < 0:
            y += h
        if x >= w:
            x -= w
        if y >= h:
            y -= h
        result.append((x, y, vx, vy))
    return result

def count(points):
    q0 = q1 = q2 = q3 = 0
    X = w // 2
    Y = h // 2
    for x, y, vx, vy in points:
        if x < X and y < Y:
            q0 += 1
        if x < X and y > Y:
            q1 += 1
        if x > X and y < Y:
            q2 += 1
        if x > X and y > Y:
            q3 += 1
    return q0*q1*q2*q3

def display(i, points):
    seen = set((x, y) for x, y, vx, vy in points)
    rows = []
    for y in range(h):
        row = []
        for x in range(w):
            if (x, y) in seen:
                row.append('*')
            else:
                row.append(' ')
        rows.append(''.join(row))
    print(i)
    print('\n'.join(rows))
    print()
# 342,387,445,488,589
seen = set()
hi = 0
for i in range(100000):
    if (i-589)%101==0:
        display(i, points)
        input()
    key = tuple((x, y) for x, y, vx, vy in points)
    if key in seen:
        break
    seen.add(key)
    points = step(points)
    # time.sleep(0)
print(i)
# print(count(points))
