a, b = map(int, (input().split()))
while b != 0:
    k = b
    b = a % b
    a = k
print(a)
