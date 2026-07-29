# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
                continue
            
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret