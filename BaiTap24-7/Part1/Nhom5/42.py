km = float(input())
if km <= 1:
    tien = km * 15000
elif km <= 5:
    tien = 15000 + (km - 1) * 12000
else:
    tien = 15000 + 4 * 12000 + (km - 5) * 10000
print(int(tien))
