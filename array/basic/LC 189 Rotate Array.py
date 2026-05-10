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
        c = gcd(n,k)
        cirle_size = n // c
        pending = (0, nums[0])
        circle_check = cirle_size
        # print(cirle_size)
        for i in range(n):            
            target_i = (pending[0] + k) % n
            target_val = nums[target_i]
            nums[target_i] = pending[1]
            circle_check -= 1
            if circle_check == 0:
                circle_check = cirle_size
                target_i = (target_i + 1) % n
                target_val = nums[target_i]

            pending = (target_i, target_val)
            
            # print(i, nums, pending, circle_check)

        

