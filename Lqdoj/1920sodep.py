ch = input()
while int(ch) >= 10:
    num = 0
    for i in range(len(ch)):
        num += int(ch[i])
    ch = str(num)
print(ch)
