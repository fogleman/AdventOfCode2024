from functools import *
import fileinput

rules = {}
updates = []
for line in fileinput.input():
    if '|' in line:
        a, b = map(int, line.split('|'))
        rules[(a, b)] = -1
        rules[(b, a)] = 1
    elif ',' in line:
        updates.append(tuple(map(int, line.split(','))))

mid = lambda x: x[len(x) // 2]
fix = lambda x: tuple(sorted(x,
    key=cmp_to_key(lambda a, b: rules.get((a, b), 0))))

print(sum(mid(x) for x in updates if x == fix(x)))
print(sum(mid(fix(x)) for x in updates if x != fix(x)))
