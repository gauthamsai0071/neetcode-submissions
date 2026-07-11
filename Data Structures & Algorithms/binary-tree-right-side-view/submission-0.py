# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels=[]
        def bfs():
            q=[root]
            while q:
                l=[]
                qlen=len(q)
                for i in range(qlen):
                    node=q.pop(0)
                    if node:
                        l.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                if l:
                    levels.append(l)
        ans=[]
        bfs()
        for i in levels:
            ans.append(i[-1])
        return ans