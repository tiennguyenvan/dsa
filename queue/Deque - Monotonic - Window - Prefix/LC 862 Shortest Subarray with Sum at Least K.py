class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        minVal = min(nums)
        realNums = [val - minVal for val in nums]
        realK = k - minVal
        q = deque()
        total = 0
        l = len(nums) + 1
        for n in realNums:
            q.append(n)
            total += n
            if total >= realK:
                l = min(l, len(q))
            while total > realK:
                left = q.popleft()
                total -= left            
                
        return l if l < len(nums) + 1 else -1
