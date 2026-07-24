
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = {}
        ret = 0 
        s = 0
        
        for i, n in enumerate(nums):
            n = -1 if n == 0 else 1
            if i == 0:
                sums[n], s = 0, n                    
                continue

            s += n            
            if s == 0:
                ret = i + 1
                continue

            if s not in sums:
                sums[s] = i                
                continue            

            ret = max(ret, i - sums[s])                  
 
        return ret
            
            
            
            

