class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)        
        nums = sorted(nums)        
        ret = []
        pre_x = None
        for i in range(n):            
            x = nums[i]
            if x == pre_x:
                continue
            pre_x = x            
            left = i + 1
            right = n - 1            
            while left < right:
                y = nums[left]                               
                z = nums[right]
                s = x + y + z
                if s < 0:
                    left += 1
                    continue

                if s > 0:
                    right -= 1
                    continue
                
                ret.append([x, y, z])
                while left < right and nums[left] == y:
                    left += 1
                while left < right and nums[right] == z:
                    right -= 1
        return ret



