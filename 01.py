import fileinput
import re

rows = [tuple(map(int, re.findall(r'\d+', line)))
    for line in fileinput.input()]

A = list(sorted(x[0] for x in rows))
B = list(sorted(x[1] for x in rows))

print(sum(abs(a - b) for a, b in zip(A, B)))
print(sum(a * B.count(a) for a in A))
