n = int(input())
lst = list(map(int, input().split()))
maxx = lst[0]
for i in range(1, len(lst)):
    maxx = max(maxx, lst[i])
print(maxx)
for i in range(len(lst)):
    if lst[i] == maxx:
        print(i + 1)
        break
