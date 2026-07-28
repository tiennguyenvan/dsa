class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = len(v1)
        m = len(v2)
        for i in range(max(m,n)):
            v1n = int(v1[i]) if i < n else 0
            v2n = int(v2[i]) if i < m else 0
            if v1n == v2n:
                continue
            return 1 if v1n > v2n else -1
        return 0
        