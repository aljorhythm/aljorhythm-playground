# Vertical Order Traversal of a Binary Tree

from arr_bin_tree import TreeNode
from typing import List

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def helper(root, d, x=0, y=0):
            if not root:
                return
            if x not in d:
                d[x] = []
            d[x].append((x, -y, root.val))
            helper(root.left, d, x - 1, y - 1,)
            helper(root.right, d, x + 1, y - 1)
        d = {}
        helper(root, d)
        sorted_keys = sorted(d.keys())
        ans = []
        for key in sorted_keys:
            values = d[key]
            values.sort()
            ans.append(list(v[2] for v in values))
        return ans

root = TreeNode.from_arr([0, None, 1])
ans = Solution().verticalTraversal(root)
print(ans)
assert ans == [[0], [1]]

root = TreeNode.from_arr([1,2,3,4,5,6,7])
ans = Solution().verticalTraversal(root)
print(ans)
assert ans == [[4],[2],[1,5,6],[3],[7]]

root = TreeNode.from_arr([3,9,20,None,None,15,7])
ans = Solution().verticalTraversal(root)
print(ans)

# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]`                                            