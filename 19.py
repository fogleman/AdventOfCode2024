from collections import *
from functools import *
from itertools import *
from math import *
import fileinput
import re
# import networkx as nx
# import numpy as np

def ints(s):
    return list(map(int, re.findall(r'-?\d+', s)))

# grid = [line.rstrip() for line in fileinput.input()]
# w, h = len(grid[0]), len(grid)
# get = lambda x, y: '.' if x < 0 or y < 0 or x >= w or y >= h else grid[y][x]

data = ''.join(fileinput.input())

patterns, rest = data.split('\n\n')

patterns = patterns.split(', ')

def possible(design, path, memo):
    # print(design, path)
    result = 0
    key = design
    if key in memo:
        return memo[key]
    if not design:
        if path:
            memo[key] = 1
            return 1
    for p in patterns:
        if len(p) > len(design):
            continue
        if design.startswith(p):
            path.append(p)
            x = possible(design[len(p):], path, memo)
            if x:
                result += x
            path.pop()
    memo[key] = result
    return result

t = 0
for d in rest.split('\n'):
    t += possible(d, [], {})
print(t)
