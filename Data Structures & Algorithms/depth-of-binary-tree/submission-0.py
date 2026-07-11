# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth=1
        def dfs(head, depth):
            nonlocal maxdepth
            if not head:
                maxdepth=max(depth,maxdepth)
                return
            dfs(head.left, depth+1)
            dfs(head.right, depth+1)
        head=root
        if not head:
            return 0
        if head.left:
            dfs(head.left,1)
        if head.right:
            dfs(head.right,1)
        return maxdepth