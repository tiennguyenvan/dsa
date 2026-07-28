
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = Counter()
        pre[0] = 1
        ret = 0
        curSum = 0
        for n in nums:
            curSum += n
            ret += pre[curSum-k]
            pre[curSum]+=1

        return ret

        