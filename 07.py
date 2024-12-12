from itertools import *
import fileinput
import re

def test(numbers, operators):
    target, numbers = numbers[0], numbers[1:]
    for ops in product(operators, repeat=len(numbers)-1):
        value = numbers[0]
        for x, op in zip(numbers[1:], ops):
            if op == '+':
                value += x
            elif op == '*':
                value *= x
            else:
                value = int(str(value) + str(x))
        if value == target:
            return target
    return 0

part1 = part2 = 0
for line in fileinput.input():
    numbers = list(map(int, re.findall(r'\d+', line)))
    part1 += test(numbers, '+*')
    part2 += test(numbers, '+*|')
print(part1)
print(part2)
