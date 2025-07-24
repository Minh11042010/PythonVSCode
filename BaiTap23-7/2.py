import math

n = int(input())
t = 0
while n > 0:
    t = t * 10 + n % 10
    n = n // 10
print(t)
