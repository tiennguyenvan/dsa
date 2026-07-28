# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        cur_lvl = 0
        q = deque()
        q.append(root)
        ret = []
        while q:
            lvl = []
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                lvl.append(node.val)                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)                                            
            if cur_lvl % 2:
                lvl.reverse()
            ret.append(lvl)
            cur_lvl += 1
        return ret