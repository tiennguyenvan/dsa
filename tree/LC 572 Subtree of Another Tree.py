# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeSignature(seft, root):
        vals = []
        cur = root
        stack = []
        pre = None
        while cur or stack:
            if cur:
                stack.append(cur)                                                
                cur = cur.left
                continue
            peek = stack[-1]
            if peek.right and peek.right != pre:
                cur = peek.right
                continue
            pre = stack.pop()
            vals.append('('+str(pre.val)+')')
            if not pre.left:
                vals.append('l')
            if not pre.right:
                vals.append('r')            
        return '.'.join(vals)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subTreeSign = self.treeSignature(subRoot)
        rootTreeSign = self.treeSignature(root)
        # print(subTreeSign)
        # print(rootTreeSign)
        return subTreeSign in rootTreeSign
        # return self.treeSignature(subRoot) in self.treeSignature(root)
        