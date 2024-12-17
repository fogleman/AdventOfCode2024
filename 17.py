from collections import *
from functools import *
from itertools import *
from math import *
import fileinput
import re

def ints(s):
    return list(map(int, re.findall(r'-?\d+', s)))

for line in fileinput.input():
    if 'A' in line:
        A = int(line.split()[-1])
    if 'B' in line:
        B = int(line.split()[-1])
    if 'C' in line:
        C = int(line.split()[-1])
    if 'P' in line:
        program = ints(line)

ip = 0

def combo(x):
    if x == 0: return 0
    if x == 1: return 1
    if x == 2: return 2
    if x == 3: return 3
    if x == 4: return A
    if x == 5: return B
    if x == 6: return C
    return None

def step():
    global ip, A, B, C
    instr = program[ip]
    opcode = program[ip+1]
    ip += 2
    if instr == 0:
        A = A // (2 ** combo(opcode))
    if instr == 1:
        B = B ^ opcode
    if instr == 2:
        B = combo(opcode) % 8
    if instr == 3:
        if A != 0:
            ip = opcode
    if instr == 4:
        B = B ^ C
    if instr == 5:
        return combo(opcode) % 8
    if instr == 6:
        B = A // (2 ** combo(opcode))
    if instr == 7:
        C = A // (2 ** combo(opcode))

def run(a):
    global A, B, C, ip
    ip = 0
    A = a
    B = 0
    C = 0
    result = []
    while True:
        try:
            x = step()
        except Exception:
            break
        if x is not None:
            result.append(x)
    return result

# Program: 2,4,1,2,7,5,4,1,1,3,5,5,0,3,3,0
a = 35282534841844
prev = 0
while True:
    x = run(a)
    # if a % 1 == 0:
    if x[:6] == [2, 4, 1, 2, 7, 5]:
        print(a, len(x), a-prev, x)
        prev = a
    if x == program:
        print(a)
        break
    # if len(x) < 16:
    #     print(a)
    #     a *= 2
    a += 2097152
