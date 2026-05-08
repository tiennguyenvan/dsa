class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ret = 0
        left = 0
        remain = k
        for right, n in enumerate(nums):
            if n == 1:
                ret = max(ret, right-left+1)
                # print(f'A: {right,n} => ret:', ret)
                continue
            if k == 0:
                left = right + 1
                # print(f'B: {right,n} => left: ', left)
                continue
            while remain == 0:
                if nums[left] == 0:
                    remain+=1
                left+=1
            remain-=1
            ret = max(ret,right-left+1)
            # print(f'C: {right,n} => ret:', ret)


        return ret