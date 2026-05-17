# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ret = []
        fromLeft = True
        while root and q:        
            lq = len(q)
            lvl = []
            for _ in range(lq):
                node = q.popleft()
                lvl.append(node.val)                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)                    
            if not fromLeft:
                lvl.reverse()
            ret.append(lvl)                                        
            fromLeft = not fromLeft    
        return ret

        