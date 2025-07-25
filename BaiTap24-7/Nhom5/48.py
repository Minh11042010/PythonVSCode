import random

so_can_doan = random.randint(1, 100)
dem = 0
while True:
    doan = int(input())
    dem = dem + 1
    if doan == so_can_doan:
        print(f"Correct! U guessed it right in {dem} times")
        break
    elif doan > so_can_doan:
        print("Lower")
    else:
        print("Higher")
