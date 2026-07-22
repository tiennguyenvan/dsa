class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sc = Counter()
        tc = Counter(t)
        extra = Counter()
        n = len(s)
        left = 0
        min_len = n + 1
        min_left = -1
        for right in range(n):
            c = s[right]
            # print(right, c)
            if not tc[c]: continue
            if sc[c] < tc[c]:
                sc[c] += 1
            else: 
                extra[c] += 1

            while left <= right and (sc == tc or not tc[s[left]]):                
                lc = s[left]                
                l = right + 1 - left
                if sc == tc and l < min_len:
                    min_len = l
                    min_left = left
                left+=1 
                if not tc[lc]:
                    continue
                if extra[lc]:
                    extra[lc] -=1
                    continue
                sc[lc]-=1

            # print((left, min_left, min_len), sc, extra)
        
        return s[min_left:min_left+min_len] if min_left != -1 else ''


