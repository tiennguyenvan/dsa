class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kLargestNums = []
        for num in nums:
            heapq.heappush(kLargestNums, num)
            if len(kLargestNums) > k:
                smallestInKLargestNums = heapq.heappop(kLargestNums)
        smallestInKLargestNums = heapq.heappop(kLargestNums)
        return smallestInKLargestNums