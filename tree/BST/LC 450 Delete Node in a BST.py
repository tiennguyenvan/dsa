# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        head = TreeNode(-float("inf"), root)
           
        def replaceChild(parent, child, new):
            if parent.left == child:
                parent.left = new
                return
            parent.right = new

        # find Node of key
        foundParent = head
        found = root
        while found and found.val != key:
            foundParent = found
            found = found.right if key > found.val else found.left
        # print(f"Found: ({v(foundParent)})->${v(found)}")

        if not found: return head.left
        if not found.right:
            replaceChild(foundParent, found, found.left)
            return head.left
        if not found.left:
            replaceChild(foundParent, found, found.right)
            return head.left

        # parent.left -> found.left, maxLeft.right -> found.right
        if foundParent.left == found:
            maxLeft = found.left
            while maxLeft.right:
                maxLeft = maxLeft.right
            foundParent.left = found.left
            maxLeft.right = found.right

        # parent.right -> found.right, minRight.left -> found.left
        else:
            minRight = found.right
            while minRight.left:
                minRight = minRight.left
            foundParent.right = found.right
            minRight.left = found.left        
        
        return head.left
