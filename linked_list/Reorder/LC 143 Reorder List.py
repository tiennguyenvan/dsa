# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        last = head
        mid = head

        while last:
            last = last.next
            if last:
                last = last.next
            else:
                break                
            mid = mid.next

        tail = None
        last = mid
        while last:
            nxt = last.next
            last.next = tail
            tail = last
            last = nxt
        
        cur_head = head
        cur_tail = tail
        while cur_tail.next:            
            next_head = cur_head.next
            next_tail = cur_tail.next
            cur_head.next = cur_tail
            cur_tail.next = next_head
            cur_head = next_head
            cur_tail = next_tail

        



        


        


        