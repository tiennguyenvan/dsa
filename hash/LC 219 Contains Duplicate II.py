class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = Counter()
        for i, v in enumerate(nums):
            if c[v]: return True
            c[v] += 1
            j = i - k
            if j < 0: 
                continue
            c[nums[j]] -= 1
            # print(i,v,j,c)

        return False