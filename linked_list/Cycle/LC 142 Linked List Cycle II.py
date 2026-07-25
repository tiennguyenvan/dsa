class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while True:
            fast = fast.next if fast else None
            fast = fast.next if fast else None
            slow = slow.next if slow else None
            
            if slow == fast:
                break

        while slow != head:
            head = head.next if head else None
            slow = slow.next if slow else None            

        return head