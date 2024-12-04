import fileinput
import re

def check(values):
    deltas = [b - a for a, b in zip(values, values[1:])]
    return all(x >= 1 and x <= 3 for x in deltas) or all(x >= -3 and x <= -1 for x in deltas)

part1 = part2 = 0
for line in fileinput.input():
    values = list(map(int, line.split()))
    part1 += check(values)
    part2 += check(values) or any(check(values[:i] + values[i+1:]) for i in range(len(values)))
print(part1)
print(part2)
