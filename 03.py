from collections import *
from itertools import *
from math import *
import fileinput
import re

total = 0
do = True
for line in fileinput.input():
    line = line.rstrip()
    for item in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)", line):
        if item.group(0) == 'do()':
            do = True
        elif item.group(0) == "don't()":
            do = False
        else:
            if do:
                total += int(item.group(1))*int(item.group(2))
print(total)
