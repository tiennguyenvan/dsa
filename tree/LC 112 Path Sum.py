# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        cur = root
        pre = None
        stack = []
        def isLeave(node):
            return not node.left and not node.right
        while cur or stack:
            if cur:
                stack.append(cur)
                total += cur.val
                if total == targetSum and isLeave(cur):
                    return True
                cur = cur.left
                continue
            peek = stack[-1]
            if peek.right and peek.right != pre:
                cur = peek.right
                continue
            pre = stack.pop()
            total -= pre.val
            
        return False