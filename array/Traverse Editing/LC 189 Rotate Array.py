class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or k > n and k % n == 0:
            return
        k = k % n
        segLen = n / k if n % k == 0 else 0
        seg = 0
        p = 0
        v = nums[p]
        for i in range(n):
            p = (p + k) % n
            t = nums[p]
            nums[p] = v
            v = t

            seg += 1
            if seg >= segLen:
                p += 1
                v = nums[p]
                seg = 0