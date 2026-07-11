# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if not curr1 or not curr2:
                return False
            
            if curr1.val!=curr2.val:
                return False
            
            return dfs(curr1.left, curr2.left) and dfs(curr1.right, curr2.right)
        
        head1=root; head2=subRoot
        def sub(node,subnode):
            if not node:
                return False
            if dfs(node, subnode):
                return True
            return sub(node.left, subnode) or sub(node.right, subnode)
        
        return sub(head1,head2)
