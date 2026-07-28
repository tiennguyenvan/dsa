# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([root])
        cur_lvl = 0
        ret_lvl = 1
        ret_max = root.val
        while q:
            cur_lvl += 1
            l = len(q)
            lvl = []
            for _ in range(l):
                node = q.popleft()
                lvl.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)                
            lvl_sum = sum(lvl)
            if lvl_sum > ret_max:
                ret_max = lvl_sum
                ret_lvl = cur_lvl
        return ret_lvl