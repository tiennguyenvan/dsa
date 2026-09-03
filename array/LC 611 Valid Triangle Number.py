class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        if n < 3: return 0

        ret = 0
        for i in range(2,n):
            left = 0
            right = i - 1
            c = sorted_nums[i]
            while left < right:
                a,b = sorted_nums[left], sorted_nums[right]
                if a + b <= c:
                    left += 1
                    continue
                ret += right - left                
                right -= 1

        return ret