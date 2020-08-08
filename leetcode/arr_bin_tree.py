# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_arr(arr):
        root = None
        i = 0
        while i < len(arr):
            if arr[i] is not None:
                arr[i] = TreeNode(arr[i])
                if i != 0:
                    parent_i = (i - 1) // 2
                    parent = arr[parent_i]
                    if i % 2 == 1:
                        parent.left = arr[i]
                    else:
                        parent.right = arr[i]
                else:
                    root = arr[i]
            i += 1
        return root

def dfs(root, depth = 0):
    if root:
        print("\t" * depth + str(root.val))
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)

if __name__ == "__main__":
    root = TreeNode.from_arr([9,8,7,6,5,4])
    dfs(root)