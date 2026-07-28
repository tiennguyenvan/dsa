# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        nodeSum = Counter()
        nodeSum[0] = 1
        cur = root
        stack = []
        pre = None
        ret = 0
        total = 0
        while cur or stack:
            if cur:
                stack.append(cur)
                total += cur.val
                # print('add NodeSum', nodeSum)
                if nodeSum[total-targetSum] > 0:
                    ret += nodeSum[total-targetSum]
                nodeSum[total] += 1
                cur = cur.left
                continue
            peek = stack[-1]
            if peek.right and peek.right != pre:
                cur = peek.right
                continue
            pre = stack.pop()
            nodeSum[total] -= 1
            # if nodeSum[total] == 0:
            #     del nodeSum[total]
            total -= pre.val
            # print('remove NodeSum', nodeSum)
        return ret