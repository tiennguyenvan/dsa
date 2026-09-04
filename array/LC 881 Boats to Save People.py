class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        w = sorted(people)
        ret = 0
        left = 0
        right = len(w) - 1
        while left < right:
            ret += 1
            if w[left] + w[right] <= limit:                
                left+=1                
            right-=1
        if left == right:
            ret += 1
        return ret            


