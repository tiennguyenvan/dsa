class Solution:
    def diffPointPalindromeWithSkip(self, s, skip_index = -1):
        n = len(s)
        l = 0
        r = n - 1        
        while l < r:
            if l == skip_index:
                l += 1
                continue
            if r == skip_index:
                r -= 1
            if s[l] != s[r]:
                break
            l +=1 
            r -=1
        if l >= r:
            return (-1,-1)
        return (l,r)


    def validPalindrome(self, s: str) -> bool:
        br_l,br_r = self.diffPointPalindromeWithSkip(s)
        if br_l == -1:
            return True
        if self.diffPointPalindromeWithSkip(s, br_l)[0] == -1:
            return True
        if self.diffPointPalindromeWithSkip(s,br_r)[0] == -1:
            return True        
        return False