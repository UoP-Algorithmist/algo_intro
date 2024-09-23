# Searching target code
def linear_search(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None


print("Not found: {}".format(linear_search([1, 2, 3, 4, 5], 43)))
print("Found: {}".format(linear_search([1, 2, 3, 4, 5], 3)))
