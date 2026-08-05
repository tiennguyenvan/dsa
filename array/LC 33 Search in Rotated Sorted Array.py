class Solution:
    def findPivot(self, nums):
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
    
    def ascBinSearch(self, target, nums, left, right):
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
                continue
            left = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        left = self.ascBinSearch(target, nums, 0, pivot-1)
        if left != -1:
            return left
        right = self.ascBinSearch(target, nums, pivot, len(nums)-1)
        if right != -1:
            return right
        return -1
        
        