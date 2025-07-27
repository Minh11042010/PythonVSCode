def check(n):
    k = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1
