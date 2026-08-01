class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ret = 0
        premin = prices[0]
        for v in prices:
            ret = max(v - premin, ret)
            premin = min(v, premin)
        return ret
