# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left -> right -> root                
        stack = []
        visited = []
        ret = []
        last = None
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
                continue
            peek = stack[-1]
            if peek.right and peek.right != last:
                cur = peek.right                
                continue
            last = stack.pop()
            ret.append(last.val)

        return ret
            
            

        
