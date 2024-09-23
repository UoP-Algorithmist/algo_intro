from math import floor


# TODO: Fix error
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [float('inf')] * (n1 + 1)
    R = [float('inf')] * (n2 + 1)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p, r, 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    print('unsorted', L, R)


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


unsorted = [9, 2, 6, 1, 0, 4]
merge_sort(unsorted, 1, len(unsorted))
print('sorted: ', unsorted)

# Insertion sort
# def insertion_sort(arr):
#     if len(arr) == 1:
#         return arr[0]
#     key = arr[1]
#     res = []
#     for i in range(1, len(arr)):
#         l = arr[i - 1]
#         if i < len(arr) - 1:
#             key = arr[i + 1]
#             if l < key:
#                 print(l)
#
#
# insertion_sort([5, 2, 4, 6, 1, 3])
