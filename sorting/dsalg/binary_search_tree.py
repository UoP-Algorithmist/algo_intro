def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


# recursive tree search
def tree_search(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


# Iterative tree search
def iterative_tree_search(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


"""
Both max and min finder in a tree runs at O (h) on tree of height h
"""


# tree minimum
def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


# Tree maximum
def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


# Recursion tree maximum version
def tree_max(x):
    if x.right is not None:
        tree_max(x.right)
    else:
        return x


# Tree successor
def tree_successor(x):
    if x.right is not None:
        return tree_successor(x.right)
    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y
