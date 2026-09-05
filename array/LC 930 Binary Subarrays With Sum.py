class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ret = 0
        left = 0
        cur_sum = 0
        lead_zeros = 0
        for right in range(len(nums)):
            n = nums[right]
            cur_sum += n
            if not cur_sum and n == 0: lead_zeros += 1

            if cur_sum < goal: continue
            
            if cur_sum == goal:
                ret += lead_zeros + 1 if goal else lead_zeros
                continue

            while left < right and nums[left] == 0: left +=1
            cur_sum -= nums[left]
            left += 1
            l = left
            lead_zeros = 0
            while l <= right and nums[l] == 0:
                l += 1
                lead_zeros += 1
            ret += lead_zeros + 1 if goal else lead_zeros
            
        return ret