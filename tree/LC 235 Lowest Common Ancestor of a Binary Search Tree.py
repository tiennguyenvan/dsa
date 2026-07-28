# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root        
        while cur:
            if cur == p or cur == q:
                return cur
            if p.val < cur.val < q.val or p.val > cur.val > q.val:
                return cur            
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
                continue
            cur = cur.left

        return None