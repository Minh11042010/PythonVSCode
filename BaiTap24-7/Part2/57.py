def giai_thua(n):
    tich = 1
    for i in range(1, n + 1):
        tich = tich * i
    return tich


n = int(input())
print(giai_thua(n))
