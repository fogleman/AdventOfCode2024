from collections import *
from itertools import *
from math import *
import fileinput
import re

first = []
second = []
for line in fileinput.input():
    line = line.rstrip()
    numbers = list(map(int, re.findall(r'\d+', line)))
    first.append(numbers[0])
    second.append(numbers[1])

first.sort()
second.sort()

print(sum(abs(a-b) for a, b in zip(first, second)))

print(sum(a*second.count(a) for a in first))
