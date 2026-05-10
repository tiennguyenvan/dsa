class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def gcd(a,b):
            while b != 0:
                a, b = b, a % b
            return a        
        c = gcd(n,k)

        pending = (nums[0], 0)
        n = len(nums)
        circle_reset_size = n
        if k % n == 0:
            circle_reset_size = 1
        elif n % k == 0:
            circle_reset_size = n // k
        

        circle_reset_checker = circle_reset_size
        for i in range(n):            
            target_i = (pending[1] + k) % n
            target_val = nums[target_i]
            nums[target_i] = pending[0]
            circle_reset_checker -= 1
            pending = (target_val, target_i + (1 if circle_reset_checker == 0 else 0))
            if circle_reset_checker == 0:
                circle_reset_checker = circle_reset_size

        

