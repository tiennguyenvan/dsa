class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = Counter()
        c[0] = 1
        t = 0
        prefix = []
        l = len(nums)
        if l == 1:
            return 1 if nums[0] == k else 0

        ret = 0
        for i, n in enumerate(nums):            
            t+=n
            ret += c[t - k]
            c[t] +=1 
            prefix.append(t)
            # print(c, prefix)
            # if n == k:
            #     ret + 1
        return ret