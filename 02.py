from collections import *
from itertools import *
from math import *
import fileinput
import re

def check(values):
    deltas = [b-a for a, b in zip(values, values[1:])]
    safe = True
    if not (all([x < 0 for x in deltas]) or all([x > 0 for x in deltas])):
        safe = False
    if not all([abs(x) >= 1 and abs(x) <= 3 for x in deltas]):
        safe = False
    return safe

def check_all(values):
    if check(values):
        return True
    return any(check(values[:i] + values[i+1:]) for i in range(len(values)))

total = 0
for line in fileinput.input():
    line = line.rstrip()
    values = list(map(int, line.split()))
    safe = check_all(values)
    if safe:
        total += 1
print(total)
