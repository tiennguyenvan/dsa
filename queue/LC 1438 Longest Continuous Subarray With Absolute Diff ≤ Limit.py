class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxi = deque()   
        mini = deque()
        left = 0
        ret = 1
        def diff(i):
            return max(
                0 if not maxi else abs(nums[i] - nums[maxi[0]]), 
                0 if not mini else abs(nums[i] - nums[mini[0]])
            )
        for i in range(len(nums)):
            while diff(i) > limit:
                if maxi and maxi[0] == left:
                    maxi.popleft()
                if mini and mini[0] == left:
                    mini.popleft()
                left += 1
            n = nums[i]
            while maxi and nums[maxi[-1]] < n: 
                maxi.pop()
            maxi.append(i)
            while mini and nums[mini[-1]] > n:
                mini.pop()
            mini.append(i)
            ret = max(ret, i-left+1)
        return ret
