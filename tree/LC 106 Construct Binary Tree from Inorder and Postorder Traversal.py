# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# inorder = [9,3,15,20,7], 
# postorder = [9,15,7,20,3] -> [3,20,7,15,9]
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        v2i = {}
        for i,v in enumerate(inorder):
            v2i[v] = i
        n = len(postorder)
        p = n
        def build(l,r):
            if l >= r:
                return None
            nonlocal p
            p -= 1
            root = TreeNode(postorder[p])
            m = v2i[root.val]
            root.right = build(m+1,r)
            root.left = build(l,m)
            return root
        return build(0,n)
            