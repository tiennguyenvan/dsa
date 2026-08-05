class Solution:
    def ascBinSearch(self, target, nums, left = None, right = None):
        if left == None: left = 0
        if right == None: right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
                continue
            left = mid + 1
        return -1

    def ascPivotSearch(self, nums):
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
                continue
            right = mid
        return left
