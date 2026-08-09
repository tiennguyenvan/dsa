class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ret = []
        for p in s:
            if not ret or p == '(':
                ret.append(p)
                continue
            if ret[-1] == '(':
                ret.pop()
                continue
            ret.append(p)
        return len(ret)