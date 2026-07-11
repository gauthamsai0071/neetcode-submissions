# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good=0;maxsofar=float("-inf")
        def dfs(curr, maxsofar):
            nonlocal good
            if not curr:
                return
            if curr.val>=maxsofar:
                good+=1
                maxsofar=max(maxsofar, curr.val)
            return dfs(curr.left, maxsofar) or dfs(curr.right, maxsofar)
        dfs(root, maxsofar)
        return good
