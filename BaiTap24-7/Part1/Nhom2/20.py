n = int(input())
lst = [0, 1]
a = 0
b = 1
for i in range(3, n + 1):
    a, b = b, a + b
    lst.append(b)
for i in range(n):
    print(lst[i], end=" ")
