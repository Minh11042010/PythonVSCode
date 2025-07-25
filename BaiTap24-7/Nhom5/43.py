a, b = map(float, input().split())
if a != 0:
    x = -b / a
    print(f"x = {x}")
elif b == 0:
    print("Vo so nghiem")
else:
    print("Vo nghiem")
