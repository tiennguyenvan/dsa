# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        last = head
        while last:
            length += 1
            last = last.next
        if n > length:
            return head
        root = ListNode(None, head)
        pre = root         
        for i in range(length-n):
            pre = pre.next
        pre.next = pre.next.next
        return root.next
