class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:       
        n = len(nums)
        ret = n + 1

        # find max left
        max_left = -1
        max_total_left = 0
        while max_total_left < x and max_left < n-1:
            max_left += 1
            max_total_left += nums[max_left]            
        if max_total_left == x:
            ret = max_left+1
        # print(f"max_left: {max_left}, {ret}")
        
        # find min right
        min_right = n
        max_total_right = 0
        while max_total_right < x and min_right > 0:            
            min_right -= 1
            max_total_right += nums[min_right]            
        if max_total_right == x:
            ret = min(ret, n - min_right)
        # print(f"min_right: {min_right}, {ret}")
        
        # find between max left and min right
        left = max_left
        right = n
        total = max_total_left
        while right > min_right and left > -1:
            right -= 1
            total += nums[right]
            # print(f"    total={total}, right={right}")
            while total > x and left > -1:
                total -= nums[left]
                left -= 1            
            if total == x:
                ret = min(ret, abs(n - right + left+1))            
                # print(f"    ---> found new total={total}, n={n}, right={right}, left={left}, ret={ret}")

        return ret if ret != n + 1 else -1

        

