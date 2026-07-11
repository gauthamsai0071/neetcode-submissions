# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=0
        def dfs(curr):
            if not curr:
                return 0
            lefth= dfs(curr.left)
            righth= dfs(curr.right)
            nonlocal ans
            if abs(lefth-righth)>1:
                ans= 1
            return 1+max(lefth,righth)
        head=root
        dfs(head)
        return not bool(ans)