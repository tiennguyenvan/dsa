class Node:
    def __init__(self, time: Meeting, left = None, right = None):
        self.time = time
        self.left = left
        self.right = right

class Meeting:
    def __init__(self,start,end):
        self.start = start
        self.end = end

class MyCalendar:

    def __init__(self):
        self.root = None
        
    def addMeeting(self, node, start, end) -> bool:
        if end <= node.time.start:
            if node.left:
                return self.addMeeting(node.left, start, end)
            node.left = Node(Meeting(start,end))
            return True
        if start >= node.time.end:
            if node.right:
                return self.addMeeting(node.right, start, end)
            node.right = Node(Meeting(start,end))
            return True
        return False

    def book(self, start: int, end: int) -> bool:
        
        if not self.root:
            self.root = Node(Meeting(start, end))
            return True
        return self.addMeeting(self.root, start, end)
        

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)