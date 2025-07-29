a, b, c = map(int, input().split())
if a + b > c and b + c > a and c + a > b:
    if a == b or b == c or c == a:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
