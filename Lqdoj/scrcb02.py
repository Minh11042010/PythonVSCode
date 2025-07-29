a = int(input())
b = int(input())
a = (a // 3 + (a % 3 != 0)) * 3
b = (b // 3) * 3
print((b - a) // 3 + 1)
