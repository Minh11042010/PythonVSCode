def tong(n):
    k = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            k += i
            if i != n / i:
                k += n / i
    return k - n


n = int(input())
print("La so hoan hao" if n == tong(n) else "Khong phai so hoan hao")
