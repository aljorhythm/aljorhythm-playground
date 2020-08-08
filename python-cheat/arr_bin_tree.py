tree = [i for i in range(20)]
print(tree)
parent_idx = [(i - 1) // 2 for i in tree]
print(parent_idx)
parents = [(tree[i], tree[parent]) if parent >= 0 else None for i, parent in enumerate(parent_idx)]
print(parents)
children_idx = [(i, i * 2 + 1, i * 2 + 2) for i in tree]
print("children")
print(children_idx)