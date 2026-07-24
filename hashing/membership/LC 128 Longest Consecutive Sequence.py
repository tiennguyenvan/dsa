class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        num_set = set(nums)
        for x in num_set:
            is_x_a_start = (x - 1) not in num_set
            l = 1
            if is_x_a_start:                           
                while (x + 1) in num_set:
                    l += 1
                    x += 1
            ret = max(ret,l)
        return ret