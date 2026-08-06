class Solution:
    def firstTargetIndex(self, nums, target):
        answer = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid] :
                answer = mid
            if target <= nums[mid]:
                right = mid - 1
                continue
            left = mid + 1
        return answer

    def lastTargetIndex(self, nums, target):
        left = 0
        right = len(nums) - 1
        answer = -1
        while left <= right:
            mid = (right + left) // 2            
            if target == nums[mid]:
                answer = mid
            if nums[mid] <= target:
                left = mid + 1
                continue
            right = mid - 1
        return answer
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstTargetIndex(nums, target), self.lastTargetIndex(nums, target)]
        