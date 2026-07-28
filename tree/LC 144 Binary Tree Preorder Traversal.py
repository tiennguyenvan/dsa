# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # root -> left -> right
        cur = root
        stack = []
        ret = []
        while cur or stack:            
            if cur:
                ret.append(cur.val)
                stack.append(cur)
                cur = cur.left
                continue
            cur = stack.pop()
            cur = cur.right
        return ret