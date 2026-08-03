class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        l = 0
        maxOdd = 0
        # print(c, len(s))
        for v in c:
            if c[v] % 2 == 0:
                l += c[v]
                continue
            l += c[v] - 1
            maxOdd = max(maxOdd, c[v])
        return l + (1 if maxOdd else 0)