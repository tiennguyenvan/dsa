# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode(None, None)
        cur = root
        valToNode = {}        
        minVal = 10000
        for i, head in enumerate(lists):
            if not head:
                continue            
            if head.val not in valToNode:
                valToNode[head.val] = []
            valToNode[head.val].append(i)
            minVal = min(minVal, head.val)        
        while valToNode:            
            if minVal not in valToNode:
                minVal += 1
                continue
            while valToNode[minVal]:
                i = valToNode[minVal].pop()            
                node = lists[i]
                cur.next = node
                cur = cur.next
                lists[i] = lists[i].next
                val = lists[i].val if lists[i] else None
                if val == None:
                    continue
                if val not in valToNode:
                    valToNode[val] = []
                valToNode[val].append(i)
            del valToNode[minVal]
            minVal += 1
        
        return root.next