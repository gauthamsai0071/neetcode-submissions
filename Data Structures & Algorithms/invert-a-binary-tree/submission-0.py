# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
                        1 <-head
            head.left->2  3 <-head.right
                    4  5 6 7
        '''
        head=root
        def dfs(head):
            if not head:
                return
            head.left, head.right=head.right,head.left
            dfs(head.left)
            dfs(head.right)
        dfs(head)
        return root



