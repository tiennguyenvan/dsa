class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        ret = float("-inf")
        for i, n in enumerate(nums):
            while q and q[0][0] < i - k:
                ret = max(ret, q.popleft()[1])
            best = max(n, n if not q else n + q[0][1])
            while q and best >= q[-1][1]:
                ret = max(ret, q.pop()[1])
            q.append((i,best))
            # print((i,n),best,q)

        return max(ret,q[0][1])