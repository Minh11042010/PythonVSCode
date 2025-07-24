def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

lst = list(map(int, input().split()))
bubble_sort(lst)
print(f"Số lớn thứ 2 là: {lst[3]}")