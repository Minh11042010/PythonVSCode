a, b = map(int, input().split())
a_goc, b_goc = a, b
while b != 0:
    temp = b
    b = a % b
    a = temp
ucln = a
bcnn = (a_goc * b_goc) // ucln
print(f"UCLN: {ucln}, BCNN: {bcnn}")
