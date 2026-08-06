class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2        
        while left <= right:
            mid = (right + left) // 2
            if x == mid * mid :
                return mid
            if x < mid * mid:
                right = mid - 1
                continue
            left = mid + 1
        return max(1, left - 1)
            

