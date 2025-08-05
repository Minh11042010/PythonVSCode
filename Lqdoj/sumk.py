n, k = map(int, input().split())
lst = list(map(int, input().split()))
prefix = lst
prefix.insert(0, 0)
for i in range(1, len(prefix)):
    prefix[i] = prefix[i] + prefix[i - 1]
# print(*prefix)

maxx = -1
prefix[-1] = 0
for i in range(k - 1, n):
    maxx = max(maxx, prefix[i] - prefix[i - k])
print(maxx)
