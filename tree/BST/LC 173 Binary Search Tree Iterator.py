# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        cur = root
        ret = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
                continue
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        ret.reverse()
        self.ret = ret

    def next(self) -> int:
        return self.ret.pop()
        

    def hasNext(self) -> bool:
        return len(self.ret) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Follow up:
# Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?