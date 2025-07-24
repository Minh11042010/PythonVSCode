import math

n = int(input())
lst = [1, 1]
a = 1
b = 1
for i in range(3, n + 1):
    a, b = b, a + b
    lst.append(b)
for i in range(n):
    print(lst[i], end=" ")
