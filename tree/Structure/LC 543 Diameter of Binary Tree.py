# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(root):
            nonlocal ret
            if not root: return 0
            leftH = dfs(root.left)
            rightH = dfs(root.right)
            ret = max(ret, leftH+rightH)
            return max(leftH,rightH)+1

        dfs(root)

        return ret