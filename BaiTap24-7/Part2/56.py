def check(n):
    if n % 2 == 0:
        return 1
    else:
        return 0


n = int(input())
print("Chan" if check(n) == 1 else "Le")
