def check(n):
    k = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            k += 1
            if i != n / i:
                k = k + 1
    if k == 2:
        return 1
    else:
        return 0


n = int(input())
for i in range(1, n + 1):
    if check(i) == 1:
        print(i, end=" ")
