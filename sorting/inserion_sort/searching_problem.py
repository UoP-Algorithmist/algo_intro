"""
Input a sequence of n  numbers A = {a1,a2,...,an}
An index i such that v = A[i] or the special value NIL if v does not appear in A
Write pseudocode for linear search
linear_search(A, v)
    for i = 0 to A.length
        if A[i] == v
            return i
    return NIL
"""


def linear_search(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None


print("Not found: {}".format(linear_search([1, 2, 3, 4, 5], 43)))
print("Found: {}".format(linear_search([1, 2, 3, 4, 5], 3)))
