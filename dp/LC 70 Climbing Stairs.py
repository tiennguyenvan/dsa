class Solution:
    def climbStairs(self, n: int) -> int:
        # n = S(n - 1) + S(n - 2)
        # S(1) = 1, s(2) = 1
        s1 = 1
        if n == 1:
            return s1
        s2 = 2
        for i in range(3, n + 1):
            s2, s1 = s1 + s2, s2
        return s2
