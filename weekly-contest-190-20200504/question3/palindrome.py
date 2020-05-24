import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isPseudo(self, s):
        numberCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for item in s:
            numberCounts[item] = numberCounts[item] + 1
        odds = 0
        for c in numberCounts:
            if c % 2 == 1:
                odds = odds + 1
            if odds > 1:
                return False
        return True

    def count(self, node, accum=[], count=0):
        if node == None:
            return count

        # childLeftIndex = (index + 1) * 2 - 1
        # childRightIndex = (index + 1) * 2
        accum = accum + [node.val]

        # if (childLeftIndex >= len(self.root) or self.root[childLeftIndex] == None) and (childRightIndex >= len(self.root) or self.root[childRightIndex] == None):
        if node.left is None and node.right is None:
            return count + (1 if self.isPseudo(accum) else 0)

        count = self.count(node.left, accum, count)
        return self.count(node.right, accum, count)

    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.count(root)
        
class Solution(object):
    
    def isPseudo(self, s):
        numberCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for item in s:
            numberCounts[item] = numberCounts[item] + 1
        odds = 0
        for c in numberCounts:
            if c % 2 == 1:
                odds = odds + 1
            if odds > 1:
                return False
        return True

    def count(self, index, accum=[], count=0):
        if index >= len(self.root) or self.root[index] == None:
            return count

        childLeftIndex = (index + 1) * 2 - 1
        childRightIndex = (index + 1) * 2
        accum = accum + [self.root[index]]

        if (childLeftIndex >= len(self.root) or self.root[childLeftIndex] == None) and (childRightIndex >= len(self.root) or self.root[childRightIndex] == None):
            return count + (1 if self.isPseudo(accum) else 0)

        count = self.count((index + 1) * 2 - 1, accum, count)
        return self.count((index + 1) * 2, accum, count)

    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.root = root
        return self.count(0)



inputs = [
    [2,3,1,3,1,None,1],
    [2,1,1,1,3,None,None,None,None,None,1]
]
outputs = [
    2, 1
]

results = []
for (i, o) in zip(inputs, outputs)[0:]:
    s = Solution()
    result = s.pseudoPalindromicPaths(i)
    print(result)
    print(result == o)
    results.append((result == o, result))

print("all")
print(results)
