def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b, c = map(int, input().split())
print(gcd(a, gcd(b, c)))
