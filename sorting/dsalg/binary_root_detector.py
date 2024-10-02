def find_root(edges):
    parents = set()
    children = set()

    for parent, child in edges:
        parents.add(parent)
        children.add(child)

    tree_root = parents - children
    return tree_root.pop() if tree_root else None


edges_set = {(1, 2), (1, 3), (2, 4), (2, 5)}
root = find_root(edges_set)
print(f"Root: {root}")
