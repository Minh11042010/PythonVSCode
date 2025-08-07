def josephus(n, k):
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result + 1


case_number = 1
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    survivor = josephus(n, k)
    print(f"Case {case_number}: {survivor}")
    case_number += 1
