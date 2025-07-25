n = int(input())

sum = 0
for i in range(1, n + 1):
    k = float(input())
    sum = sum + k

p = sum / n
if p >= 9.0:
    xep_loai = "Xuat sac"
elif p >= 8.0:
    xep_loai = "Gioi"
elif p >= 6.5:
    xep_loai = "Kha"
elif p >= 5.0:
    xep_loai = "Trung binh"
else:
    xep_loai = "Yeu"
print(f"Diem TB: {p:.2f}, Xep loat: {xep_loai}")
