# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ret = 0
        while root and q:
            ql = len(q)
            for _ in range(ql):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ret+=1
        return ret