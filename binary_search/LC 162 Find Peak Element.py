class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return -1
        
        def leftVal(i):
            return nums[i-1] if i-1 > -1 else -float('inf')
        def rightVal(i):
            return nums[i+1] if i+1 < n else -float('inf')

        left = 0
        right = n - 1
        while left <= right:
            mid = (right + left) // 2
            if leftVal(mid) < nums[mid] and nums[mid] > rightVal(mid):
                return mid
            if leftVal(mid) < nums[mid] < rightVal(mid):
                left = mid + 1
                continue
            right = mid - 1
        return left

        

        
        