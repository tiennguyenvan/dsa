# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ret = 0
        q = deque([root])
        while root and q:
            lq = len(q)
            for _ in range(lq):
                node = q.popleft()
                if (not node.left) and (not node.right):
                    return ret+1
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ret+=1
        return ret