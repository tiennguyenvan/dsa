# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        stack = []
        cur = root
        last = None
        total = 0

        while cur or stack:
            if cur:
                stack.append(cur)
                total += cur.val
                cur = cur.left
                continue
                
            peek = stack[-1]
            if total == targetSum and not peek.right and not peek.left:
                ret.append([node.val for node in stack])

            if peek.right and peek.right != last:
                cur = peek.right
                continue

            last = stack.pop()
            total -= last.val

            
        return ret
