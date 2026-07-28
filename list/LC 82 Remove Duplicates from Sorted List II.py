# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(None, head) 
        pre = root
        cur = head
        while cur:            
            if cur.next and cur.next.val == cur.val:
                val = cur.val 
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
                continue
            pre = cur
            cur = cur.next

            
        return root.next