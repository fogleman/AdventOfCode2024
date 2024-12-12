from functools import *
import fileinput

@cache
def blink(x, d):
    d -= 1
    if d < 0:
        return 1
    s = str(x)
    n = len(s)
    if x == 0:
        return blink(1, d)
    elif n % 2 == 0:
        return blink(int(s[:n//2]), d) + blink(int(s[n//2:]), d)
    else:
        return blink(x * 2024, d)

numbers = list(map(int, next(fileinput.input()).split()))
print(sum(blink(x, 25) for x in numbers))
print(sum(blink(x, 75) for x in numbers))
