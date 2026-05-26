# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def isLeave(node):
            return not node.left and not node.right
        
        ret = 0
        total = 0 
        cur = root
        pre = None
        stack = []
        while cur or stack:
            if cur:
                total = total * 10 + cur.val
                # print('cur', cur.val, total)
                if isLeave(cur):
                    # print('    add to ret', total)
                    ret += total                    
                stack.append(cur)
                cur = cur.left
                continue
            peek = stack[-1]
            if peek.right and peek.right != pre:
                cur = peek.right
                continue
            pre = stack.pop()
            # print('pre: total&pre', total, pre.val)
            total = total - pre.val
            # print('    total - pre', total)
            total = total // 10   
            # print('    total//10', total)
        return ret