class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        for i in range(len(haystack) + 1 - len(needle)):
            unmatched = False            
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    continue
                unmatched = True
                break
            if unmatched:
                continue
            return i
        return -1