def get_min(A):
    low, index = A[0], 0
    for i in range(len(A)):
        if low > A[i]:
            low = A[i]
            index = i
    return low, index


def selection_sort(A: list):
    start = 0
    while start < len(A):
        sub = min(A[start:])
        p = get_min(A[start:])
        A[A.index(sub)] = A[start]
        A[start] = sub
        start += 1
    return A


print(selection_sort([1, 4, 2, 7, 8, 0, 8]))
