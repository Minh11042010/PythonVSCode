thang, nam = map(int, input().split())

if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
else:  # Thang 2
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
        so_ngay = 29
    else:
        so_ngay = 28

    print(so_ngay)
