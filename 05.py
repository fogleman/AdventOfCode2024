from functools import *
import fileinput
import re

rules = []
updates = []
for line in fileinput.input():
    numbers = tuple(map(int, re.findall(r'\d+', line)))
    if '|' in line:
        rules.append(numbers)
    elif ',' in line:
        updates.append(numbers)

fix = lambda x: tuple(sorted(x, key=cmp_to_key(
    lambda a, b: -1 if (a, b) in rules else 1 if (b, a) in rules else 0)))

print(sum(x[len(x) // 2] for x in updates if x == fix(x)))
print(sum([fix(x)[len(x) // 2] for x in updates if x != fix(x)]))
