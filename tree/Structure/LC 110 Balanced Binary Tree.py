# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balancedTreeHeight(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0     
        leftHeight = self.balancedTreeHeight(root.left)
        rightHeight = self.balancedTreeHeight(root.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        return self.balancedTreeHeight(root) != -1
        