class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        q = deque()    
        if len(nums) < k+1:
            return [max(nums)]
        for i, n in enumerate(nums):        
            while q and nums[q[-1]] < n:
                q.pop()
            while q and (i - q[0]) >= k:
                q.popleft()
            q.append(i)
            
            if i + 1 >= k:
                ret.append(nums[q[0]])
        return ret