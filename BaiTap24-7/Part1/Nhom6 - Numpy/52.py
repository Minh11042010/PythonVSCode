a, b, c, d, e, f = map(float, input().split())
D = a * e - b * d
Dx = c * e - b * f
Dy = a * f - c * d

if D != 0:
    x = Dx / D
    y = Dy / D
    print(f"He phuong trinh co nghiem duy nhat la x = {x}, y = {y}")
elif Dx == 0 and Dy == 0:
    print("He phuong trinh co vo so nghiem")
else:
    print("He phuong trinh vo nghiem")
