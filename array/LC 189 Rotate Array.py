class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def gcd(a,b):
            while b != 0:
                a, b = b, a % b
            return a
        
        n = len(nums)
        if not k or not n or k >= n and k % n == 0:
            return
        g = gcd(n,k)

        segLen = n / g if g > 1 else 0
        seg = 0
        p = 0
        v = nums[p]
        for i in range(n):
            p = (p + k) % n
            t = nums[p]
            nums[p] = v
            v = t
            if not segLen:
                continue
            seg += 1
            if seg < segLen:
                continue
            p += 1
            v = nums[p]
            seg = 0