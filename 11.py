import math
n = int(input())
a, b = 1, 2
t = 0
while a <= n:
    if a % 2 == 0:
        t += a
    a, b = b, a + b
print(t)