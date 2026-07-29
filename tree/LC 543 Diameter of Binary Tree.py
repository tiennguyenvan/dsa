# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeStats:
    def __init__(self, h, d):
        self.h = h
        self.d = d

class Solution:
    def _getTreeStats(self, node) -> TreeStats:
        if not node:
            return TreeStats(0,0)

        leftStats = self._getTreeStats(node.left)
        rightStats = self._getTreeStats(node.right)
        return TreeStats(
            max(leftStats.h, rightStats.h) + 1, 
            max(leftStats.d, rightStats.d, leftStats.h + rightStats.h)
        )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        rootStats = self._getTreeStats(root)

        return rootStats.d
        