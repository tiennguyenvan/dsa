# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_v2: # learned from the accepted one
    def dfs(self, root: Optional[TreeNode], lower: float, upper: float) -> bool:
        if not root:
            return True
        if not (lower < root.val < upper):
            return False
        return (
            self.dfs(root.left, lower, root.val) 
            and self.dfs(root.right, root.val, upper)
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))
        

class Solution_v1: # this has the same Time Complexity, totally acceptable
    def minMax(self, root: Optional[TreeNode]) -> (int,int):
        minVal = root.val
        maxVal = root.val        
        if root.left:
            leftMin, leftMax = self.minMax(root.left)
            if leftMax >= minVal or leftMax == -float("inf"):
                return (float("inf"),-float("inf"))            
            minVal = leftMin
        if root.right:
            rightMin, rightMax = self.minMax(root.right)
            if rightMin <= maxVal or rightMin == float("inf"):
                return (float("inf"),-float("inf"))
            maxVal = rightMax
        
        return (minVal, maxVal)

        return (0,0)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True        
        left,right = self.minMax(root)
        if root.left and left >= root.val:
            return False
        if root.right and right <= root.val:
            return False
        return True
        