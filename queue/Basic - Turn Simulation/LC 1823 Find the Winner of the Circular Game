class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [num for num in range(1,n+1)]
        print(circle)
        start = 0
        while len(circle) > 1:
            end = (start + k - 1) % len(circle)
            circle.pop(end)
            start = end
        return circle[0]