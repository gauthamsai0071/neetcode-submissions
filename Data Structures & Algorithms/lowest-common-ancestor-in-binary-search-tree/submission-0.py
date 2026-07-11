# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        basing on root
        if curr > max(p,q)
        curr = curr.left
        if curr< 
        '''

        curr=root
        while curr:
            print(curr.val,p.val,q.val)
            if curr.val<p.val and curr.val<q.val:
                curr=curr.right
            elif curr.val>p.val and curr.val>q.val:
                curr=curr.left
            else:
                return curr
        
        
