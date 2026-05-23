# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node
        pre = None
        cur = root
        while cur:            
            pre = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        if pre.val > val:
            pre.left = new_node
        else:
            pre.right = new_node

        return root