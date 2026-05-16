# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root: 
            return ret
        stack = [root]
        back = []

        while stack or back:
            if stack:
                last = stack.pop()
                if last.left:
                    stack.append(last.left)
                    back.append(last)
                    continue
                ret.append(last.val)
                if last.right:
                    stack.append(last.right)
                continue
            last = back.pop()
            ret.append(last.val)
            if last.right:
                stack.append(last.right)                

        return ret