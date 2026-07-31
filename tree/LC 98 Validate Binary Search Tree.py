# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Info:
    def __init__(self, isBST, minVal = None, maxVal = None):
        self.isBST = isBST
        self.min = minVal
        self.max = maxVal
        # print(isBST, minVal, maxVal)

class Solution:
    def nodeInfo(self, node: Optional[TreeNode]) -> List[int]:
        minVal = -float('inf')
        maxVal = float('inf')

        if not node:
            return None            
        l = self.nodeInfo(node.left)        
        r = self.nodeInfo(node.right)

        if not l: l = Info(True, maxVal, minVal)
        if not r: r = Info(True, maxVal, minVal)                

        return Info(
            (l.isBST and r.isBST and l.max < node.val < r.min),
            min(l.min, node.val),
            max(r.max, node.val)
        )     
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        rootBstStat = self.nodeInfo(root)
        return rootBstStat.isBST