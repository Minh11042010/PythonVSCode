n = int(input())
if n == 0:
    s = "0"
else:
    s = ""
    tmp = n
    while tmp > 0:
        s = str(tmp % 2) + s
        tmp = tmp // 2
print(s)
