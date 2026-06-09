# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        cur = root
        stack = []
        ret = []
        while cur or stack:
            if cur:
                ret.append(str(cur.val))
                stack.append(cur)
                cur = cur.left
                continue
            ret.append('')
            cur = stack.pop()
            cur = cur.right
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        stack = []
        vals = data.split(',')
        while vals:
            val = vals.pop()
            if val == '':
                stack.append(None)
                continue
            left = stack.pop()
            right = stack.pop() if stack else None
            root = TreeNode(int(val), left, right)
            stack.append(root)
            
        return stack[0]

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))