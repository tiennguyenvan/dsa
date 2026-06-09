# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        cur = root
        stack = []
        ret = []
        while cur or stack:
            ret.append(str(cur.val) if cur else '')
            if cur:
                stack.append(cur)
                cur = cur.left
                continue
            cur = stack.pop()
            cur = cur.right      
        return ','.join(ret)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        vals = data.split(',')        
        stack = []
        while vals:
            v = vals.pop()
            if v == '':
                stack.append(None)
                continue
            node = TreeNode(int(v))
            node.left = stack.pop() if stack else None
            node.right= stack.pop() if stack else None
            stack.append(node)
        
        return stack[0]
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans