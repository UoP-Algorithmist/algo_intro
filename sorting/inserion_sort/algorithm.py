def insertion_sort(arr):
    index = 0
    while index < len(arr) - 1:
        if index < 0:
            index = 0
        if arr[index + 1] < arr[index]:
            cur_value = arr[index]
            arr[index] = arr[index + 1]
            arr[index + 1] = cur_value
            index -= 1
        else:
            index += 1
    return arr


# print(insertion_sort([5, 2, 4, 6, 1, 3]))


# Insertion sort
def insertion_sort_v2(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into sorted sequence A[1..j-1]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


print(insertion_sort_v2([5, 2, 4, 6, 1, 3]))
