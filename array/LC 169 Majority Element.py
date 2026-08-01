class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = (n // 2) + 1
        c = Counter()
        for v in nums:
            c[v] += 1
            if c[v] == m:
                return v
        return -1