from collections import *
from functools import *
from itertools import *
from math import *
import fileinput
import re

line = ''.join(line.rstrip() for line in fileinput.input())

value = []
id = 0
for i, c in enumerate(line):
    n = int(c)
    if i % 2 == 0:
        value.extend([id] * n)
        id += 1
    else:
        value.extend([-1] * n)


def shift(value):
    i = 0
    j = len(value) - 1
    while j > i:
        while value[j] < 0:
            j -= 1
        if value[i] < 0:
            value[i] = value[j]
            value[j] = -1
            i += 1
            j -= 1
        else:
            i += 1

def find(value, n):
    for i in range(len(value)-n):
        ok = True
        for j in range(i, i + n):
            if value[j] >= 0:
                ok = False
                break
        if ok:
            return i
    return -1

def shift(value):
    x = max(value)
    while x >= 0:
        n = value.count(x)
        i = value.index(x)
        j = find(value, n)
        if j >= 0 and j < i:
            value[j:j+n] = [x] * n
            value[i:i+n] = [-1] * n
        x -= 1

shift(value)
total = 0
for i, x in enumerate(value):
    if x < 0:
        continue
    total += i * x
print(total)
