class Solution:
    def ascBinSearch(self, target, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
                continue
            left = mid + 1
        return -1

    def ascBinSearchFirstIndex(self, target, nums):
        answer = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                answer = mid
            if target <= nums[mid]:
                right = mid - 1
                continue
            left = mid + 1
        return answer

    def ascBinSearchLastIndex(self, target, nums):
        answer = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                answer = mid
            if nums[mid] <= target:
                left = mid + 1
                continue
            right = mid - 1
        return answer

    def ascPivotBinSearch(self, nums):
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
