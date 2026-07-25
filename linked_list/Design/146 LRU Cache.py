class LRUNode:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None
        self.key = None

class LRUCache:

    def __init__(self, capacity: int):   
        self.cap = capacity  
        self.size = 0   
        self.head = LRUNode()
        self.tail = LRUNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}

    def updateList(self, key: int) -> None:
        cur = self.dict[key]
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        head_next = self.head.next
        self.head.next = cur
        cur.prev = self.head
        cur.next = head_next
        head_next.prev = cur

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.updateList(key)
        return self.dict[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].val = value
            self.updateList(key)
            return
        if self.size == self.cap:
            remove_node = self.tail.prev
            remove_key = self.tail.prev.key
            remove_node.prev.next = self.tail
            self.tail.prev = remove_node.prev
            self.size -= 1
            del self.dict[remove_key]
    
        new_node = LRUNode(value)
        new_node.key = key
        self.head.next.prev = new_node
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node

        self.dict[key] = new_node
        self.size += 1

        



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)