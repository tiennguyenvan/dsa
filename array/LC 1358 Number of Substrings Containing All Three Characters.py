class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total = 0
        count = Counter()
        left = 0
        preHasAll = -1
        checkSet = set(['a', 'b', 'c'])

        def hasAll():
            for c in checkSet:
                if not count[c]:
                    return False
            return True
        n = len(s)
        for right in range(n):
            c = s[right]
            count[c] += 1
            if not hasAll():
                continue
            while left < right and (s[left] not in checkSet or count[s[left]] > 1):
                count[s[left]] -= 1
                left += 1
            total += (left - (preHasAll+1) + 1) * (n - right)
            # print(f'found {dict(left=left,right=right,inc=((left + 1) * (n - right)),total= total)}')
            preHasAll = left
            while left <= right and hasAll():
                count[s[left]] -= 1
                left += 1

        return total
