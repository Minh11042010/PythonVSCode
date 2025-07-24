n = int(input())
m = abs(n)
if m == 0:
    print(1)
else:
    d = 0
    while m > 0:
        d += 1
        m = m // 10
    print(d)
