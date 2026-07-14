# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        we explore the subtree if the sum_so_far is increasing, 
        if curr.val + curr.left.val > sum_so_far:
            dfs(curr.left)
        same for right

        if curr.val> sm_so_far:
            sum_so_far=curr.val
        '''
        sumsofar = 0
        maxsum=root.val
        def dfs(curr):
            nonlocal maxsum
            if not curr:
                return 0
            
            leftsum=max(0,dfs(curr.left))
            rightsum=max(0,dfs(curr.right))
            print(curr.val,leftsum,rightsum)
            maxsum=max(maxsum, curr.val+leftsum+rightsum)
            return curr.val + max(leftsum, rightsum)
        dfs(root)
        return maxsum
            