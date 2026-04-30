class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = deque()    
        for i,n in enumerate(nums): 
            while q and q[0][0] < i - k:
                q.popleft()
            best = n + q[0][1] if q else n
            while q and best >= q[-1][1]:
                q.pop()            
            q.append((i,best))            
            # print(n, q)
        return q[-1][1]