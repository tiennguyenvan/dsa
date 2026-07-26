class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
                continue
            right = mid                        
        return left

    def searchSegment(self,nums: List[int], start: int, end: int, target: int) -> int:
        left = start
        right = end-1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
                continue
            right = mid
        return left if nums[left] == target else -1


    def search(self, nums: List[int], target: int) -> int:
        pi = self.pivotIndex(nums)
        leftSearch = self.searchSegment(nums, 0, pi, target)
        rightSearch = self.searchSegment(nums, pi, len(nums), target)

        return leftSearch if leftSearch != -1 else rightSearch