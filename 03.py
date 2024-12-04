import fileinput
import re

pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
part1 = part2 = 0
enabled = 1

for line in fileinput.input():
    for match in re.finditer(pattern, line):
        if match[0] == "do()":
            enabled = 1
        elif match[0] == "don't()":
            enabled = 0
        else:
            product = int(match[1]) * int(match[2])
            part1 += product
            part2 += product * enabled

print(part1)
print(part2)
