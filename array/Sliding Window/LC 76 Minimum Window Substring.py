class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCharCount = Counter(t)
        tLen = len(t)

        left = minLeft = 0
        minLen = len(s) + 1

        for right, sChar in enumerate(s):
            if tCharCount[sChar] > 0:
                tLen -= 1
            tCharCount[sChar] -= 1

            if tLen:
                continue            
            
            while tCharCount[s[left]] < 0:
                tCharCount[s[left]] += 1
                left += 1
                
            foundLen = right + 1 - left
            if foundLen < minLen:
                minLen, minLeft = foundLen, left

            roomToExpand = 1
            tCharCount[s[left]] += roomToExpand
            left += 1
            tLen += 1

        return s[minLeft:minLeft+minLen] if minLen < len(s) + 1 else ''


