def check(n):
    k = 0
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1


n = int(input())
lst = list(map(int, input().split()))
prime = []
for i in lst:
    if check(i) == 1:
        prime.append(i)
maxx = -1
for i in prime:
    maxx = max(maxx, i)

print(maxx)
for i in range(len(lst)):
    if lst[i] == maxx:
        print(i + 1, end=" ")
