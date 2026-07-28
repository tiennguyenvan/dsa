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
            if cur:
                stack.append(cur)
                ret.append(str(cur.val))
                cur = cur.left
                continue
            cur = stack.pop()
            cur = cur.right    
        print(ret)  
        return ','.join(ret)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        i = 0        
        vals = list(map(int, data.split(',')))        
        n = len(vals)

        def build(low,hi):
            nonlocal i
            if i >= n:
                return None
            val = vals[i]
            if val < low or val > hi:
                return None                
            i+=1
            root = TreeNode(val)
            root.left = build(low,val)
            root.right = build(val,hi)

            return root
            
        return build(float("-inf"), float("inf"))
        # if not data:
        #     return None
        # vals = data.split(',')        
        # v = None
        # stack = []
        # while vals:
        #     v = vals.pop()
        #     if v == '':
        #         stack.append(None)
        #         continue
        #     node = TreeNode(int(v))
        #     node.left = stack.pop() if stack else None
        #     node.right= stack.pop() if stack else None
        #     stack.append(node)
        
        # return stack[0]
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans