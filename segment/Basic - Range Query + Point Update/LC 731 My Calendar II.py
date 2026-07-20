'''
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.
A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).
The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.
Implement the MyCalendarTwo class:
MyCalendarTwo() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Example 1:
Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]
'''
class MeetingGroup:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = count
        
class Node:
    def __int__(self, m: MeetingGroup):
        self.m = m
        self.left = None
        self.right = None
        
class MyCalendarTwo:

    def __init__(self):
        self.root = None

    def addMeeting(self, node, start, end):
        if end <= node.m.start:
            if node.left:
                return self.addMeeting(node.left, start, end)
            node.left = Node(MeetingGroup(start,end))
            return True

        if start >= node.m.end:
            if node.right:
                return self.addMeeting(node.right, start, end)
            node.right = Node(MeetingGroup(start,end))
            return True

        if node.count == 2:
            return False
        node.count += 1
        

        
        

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(MeetingGroup(start,end))
            return True
        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)