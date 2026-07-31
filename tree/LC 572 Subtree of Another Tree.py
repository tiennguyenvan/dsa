class Solution:
    def treeSignature(self, root):
        signature = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                left = '/' if cur.left else '['
                right = '\\' if cur.right else ']'
                signature.append(left + str(cur.val) + right)
                stack.append(cur)
                cur = cur.left
                continue
            cur = stack.pop()
            cur = cur.right
        return ''.join(signature)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print(self.treeSignature(subRoot), self.treeSignature(root))
        return self.treeSignature(subRoot) in self.treeSignature(root)