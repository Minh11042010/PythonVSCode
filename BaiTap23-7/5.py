import math
def check(n):
    d = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d += 1
            if i != n / i:
                d += 1
    if d == 2:
        return True
    else :
        return False
n = int(input())
print(n, f"là số nguyên tố" if check(n) else f"không là số nguyên tố")