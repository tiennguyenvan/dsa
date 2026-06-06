# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        valToIdx = {}
        for i,v in enumerate(postorder):
            valToIdx[v] = i
        ptr = -1
        n = len(preorder)
        def build(left, right):
            if left > right:
                return None
            nonlocal ptr
            ptr += 1
            # print(padStr, ptr, [left,right])
            root = TreeNode(preorder[ptr])
            leftVal = preorder[ptr+1] if ptr < n - 1 else None
            leftRight = valToIdx[leftVal] if leftVal != None else left-1
            rightRight = right - 1
            root.left = build(left, min(leftRight, rightRight))
            root.right = build(leftRight + 1, rightRight)
            return root
        
        return build(0, n-1)