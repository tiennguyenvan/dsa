# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def isLeave(node):
            return not node.left and not node.right
        
        cur = root
        stack = []
        pre = None
        ret = []
        vals = []
        while cur or stack:
            if cur:
                vals.append(cur.val)
                if isLeave(cur):
                    ret.append("->".join(map(str,vals)))
                stack.append(cur)
                cur = cur.left
                continue
            peek = stack[-1]
            if peek.right and peek.right != pre:
                cur = peek.right
                continue
            pre = stack.pop()
            vals.pop()
        return ret