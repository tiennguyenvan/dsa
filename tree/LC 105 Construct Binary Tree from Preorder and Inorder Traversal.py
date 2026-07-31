
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iMap = {}
        for i, v in enumerate(inorder):
            iMap[v] = i
        n = len(preorder)

        def build(pstart, istart, length):            
            if length <= 0: return None
            val = preorder[pstart]
            imid = iMap[val]
            node = TreeNode(val)
            leftStart = pstart + 1
            leftLen = imid - istart
            rightStart = leftStart + leftLen
            righIStart = imid + 1
            rightLen = istart + length - righIStart
            node.left = build(leftStart, istart, leftLen)
            node.right = build(rightStart, righIStart, rightLen)
            return node

        return build(0, 0, n)
