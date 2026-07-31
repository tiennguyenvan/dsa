class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefix = []
        while strs:                        
            misMatched = False
            for s in strs:
                if i >= len(s):
                    return s
                if s[i] != strs[0][i]:
                    misMatched = True
                    break
            if misMatched:
                break
            prefix.append(strs[0][i])
            i+=1                

        return ''.join(prefix)
