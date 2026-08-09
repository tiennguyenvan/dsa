class Solution:
    def makeGood(self, s: str) -> str:
        ret = []
        for c in s:
            if not ret:
                ret.append(c)
                continue

            last = ret[-1]
            if last != c and last.upper() == c.upper():
                ret.pop()
                continue
                
            ret.append(c)

        return ''.join(ret)
        