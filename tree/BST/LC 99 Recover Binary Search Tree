# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """        
        pre = None
        node1 = None
        node2 = None
        cur = root
        stack = []
        
        def swapNodeVal(n1,n2):
            if not n1 or not n2:
                return
            n1.val, n2.val = n2.val, n1.val        

        while cur or stack:
            if cur:                   
                stack.append(cur)
                cur = cur.left
                continue
            cur = stack.pop()
            if pre and pre.val > cur.val:
                if not node1:
                    node1 = pre
                    node2 = cur
                    # print('found node 1', pre.val)
                else:
                    node2 = cur
                    # print('found node 2', cur.val)
                    break
            pre = cur            
            # print(cur.val)            
            cur = cur.right
        swapNodeVal(node1, node2)
        
        return root