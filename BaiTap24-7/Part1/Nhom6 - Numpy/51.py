a, b, c = map(float, input().split())

if a == 0:
    if b == 0:
        if c == 0:
            print("Vo so nghiem")
        else:
            print("Vo nghiem")
    else:
        x = -c / b
        print(f"Phuong trinh co nghiem la: {x}")
else:
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        print(f"Phuong trinh co 2 nghiem la x1 = {x1} va x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phuong trinh co nghiem kep: x = {x}")
    else:
        print("Phuong trinh vo nghiem")
