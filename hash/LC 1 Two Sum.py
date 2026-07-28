class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = {}
        for i,n in enumerate(nums):
            m = target-n
            if m in pre: return [pre[m],i]
            pre[n] = i
        return [0,0]
