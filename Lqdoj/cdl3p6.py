def demuoc(n):
    d = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d += 1
            if i != n / i:
                d += 1
    return d


n = int(input())
print(demuoc(n))
