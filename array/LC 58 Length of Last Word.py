class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        l = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                if not l: continue
                return l
            l +=1
        return l