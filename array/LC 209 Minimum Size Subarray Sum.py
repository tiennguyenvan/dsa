class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)        
        ret = n + 1

        left = 0
        cur_sum = 0
        for right in range(n):
            cur_sum += nums[right]
            if cur_sum < target: continue

            while left <= right and cur_sum >= target:
                cur_sum -= nums[left]
                ret = min(ret, right + 1 - left) 
                left += 1

        return 0 if ret == n + 1 else ret
        
