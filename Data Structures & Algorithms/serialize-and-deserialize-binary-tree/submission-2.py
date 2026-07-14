# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
        convert to inorder + # + preorder
        '''
        inorderstr=''; preorderstr=''
        def inorder(curr):
            nonlocal inorderstr
            if not curr:
                return
            inorder(curr.left)
            inorderstr+=str(curr.val)+'-'
            inorder(curr.right)

        def preorder(curr):
            nonlocal preorderstr
            if not curr:
                return
            preorderstr+=str(curr.val)+'-'
            preorder(curr.left)
            preorder(curr.right)
        head=root
        inorder(head)
        preorder(head)
        return inorderstr+'#'+preorderstr


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        '''
        use the str # seperated by inorder and preorder respectively
        '''
        if not data:
            return None
        inorder=[];preorder=[]
        s=data.split('#')
        inorder = s[0].split('-')
        preorder = s[1].split('-')

        for i in range(len(inorder)):
            if inorder[i]!='':
                inorder[i]=int(inorder[i])
            else:
                del inorder[i]
        for i in range(len(preorder)):
            if preorder[i]!='':
                preorder[i]=int(preorder[i])
            else:
                del preorder[i]
        midseen={}
        def tree(preorder, inorder):
            nonlocal midseen
            if not preorder or not inorder:
                return None
            curr=TreeNode(preorder[0])
            mid=inorder.index(preorder[0])
            for i in range(len(inorder)):
                if inorder[i]==preorder[0]:
                    if preorder[i] in midseen and midseen[preorder[i]]!=i:
                        mid=i
                        midseen[preorder[i]]=i
                        break
                    else:
                        midseen[preorder[i]]=i
                    
            curr.left = tree(preorder[1:mid+1], inorder[:mid])
            curr.right = tree(preorder[mid+1:], inorder[mid+1:])
            return curr
        
        return tree(preorder, inorder)
