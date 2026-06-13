# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        signatures = {}
        ret = []
        def sign(root):
            if not root:
                return '_'
            s = ','.join([str(root.val), sign(root.left), sign(root.right)])
            nonlocal signatures
            if s not in signatures:
                signatures[s] = []
            signatures[s].append(root)
            return s
        sign(root)
        # print(signatures)
        for sign in signatures:
            nodes = signatures[sign]
            # print(sign, len(nodes))
            if len(nodes) == 1:
                continue
            ret.append(nodes[0])
        return ret