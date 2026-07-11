# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        rng=[-float("inf"), float("inf")]
        def dfs(curr,rng):
            leftr=rng[0]
            rightr=rng[1]
            if not curr:
                return True
            if not(curr.val<rightr and curr.val>leftr):
                return False
            return dfs(curr.left,[leftr,curr.val]) and dfs(curr.right, [curr.val, rightr])
        return dfs(root, [-float("inf"), float("inf")])