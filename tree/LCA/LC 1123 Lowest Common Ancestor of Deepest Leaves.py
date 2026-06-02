# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def lcaWithDepth(depth, root):
            if not root:
                return (depth-1, root)
            left = lcaWithDepth(depth+1, root.left)
            right = lcaWithDepth(depth+1, root.right)
            if left[0] > right[0]:
                return left
            if left[0] < right[0]:
                return right
            return (left[0], root)
        lca = lcaWithDepth(1,root)
        return lca[1]