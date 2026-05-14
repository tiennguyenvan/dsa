# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def val(p):
            return p.val if p else None
        def vals(p):
            arr = []
            while p:
                arr.append(p.val)
                p = p.next
            return arr
        # find mid point
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        # print(vals(slow))
        if not slow:
            return
        
        # reverse last half
        prev = slow
        mid = slow.next
        slow.next = None
        while mid:
            next = mid.next
            mid.next = prev
            prev = mid
            mid = next        
        # print(vals(prev))

        # reorder
        pHead = head
        pTail = prev
        while pTail:
            head_next = pHead.next
            tail_next = pTail.next
            pHead.next = pTail
            pTail.next = head_next
            pHead = head_next
            pTail = tail_next
            # print(val(pHead), val(pTail))
        pHead.next = None
        
        

