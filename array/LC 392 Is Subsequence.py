class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        matched = 0
        if not s: return True
        for c in t:                        
            if c != s[matched]: continue
            matched +=1
            if matched == len(s): return True            
        return False