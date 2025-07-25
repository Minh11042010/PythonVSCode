def check(n):
    k = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            k += 1
            if i != n / i:
                k += 1
    if k == 2:
        return 1
    else:
        return 0


n = int(input())
print("La so nguyen to" if check(n) == 1 else "Khong phai so nguyen to")
