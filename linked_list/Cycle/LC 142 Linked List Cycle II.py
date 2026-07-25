class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while True:
            fast = fast.next if fast else None
            fast = fast.next if fast else None
            slow = slow.next if slow else None
            slow_met_fast = slow == fast
            if slow_met_fast:
                break

        while True:
            head = head.next if head else None
            slow = slow.next if slow else None
            slow_met_head = slow == head
            if slow_met_head:
                break

        return head