# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        v2i = {}
        for i,v in enumerate(inorder):
            v2i[v] = i
        p = -1
        def build(l,r):
            if l >= r:
                return
            nonlocal p
            p+=1
            root = TreeNode(preorder[p])
            m = v2i[root.val]
            root.left = build(l, m)
            root.right = build(m+1, r)
            return root
        return build(0, len(preorder))


        # v2i = {}
        # for i,v in enumerate(inorder):
        #     v2i[v] = i
        # n = len(preorder)        
        # def build(s,l,r):            
        #     if l >= r:  
        #         return None
        #     v = preorder[s]
        #     root = TreeNode(v)
        #     m = v2i[v]          
        #     ls = s+1
        #     rs = s+1+m-l  
        #     root.left = build(ls, l, m)                        
        #     root.right = build(rs, m+1, r)            
        #     return root
        # return build(0, 0, n)



        # if not preorder or not inorder:
        #     return None
        # root = TreeNode(preorder[0])
        # index = inorder.index(root.val)
        # root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        # root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        # return root
        