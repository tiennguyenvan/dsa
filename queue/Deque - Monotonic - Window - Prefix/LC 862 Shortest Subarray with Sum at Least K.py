class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:       
        t = 0
        sums = []
        for i,n in enumerate(nums):                        
            if n >= k:            
                return 1
            sums.append((t,i))             
            t+=n            
        # print(sums)
        q = deque()
        l = len(nums) + 1
        def valid_sum_front(s,q0,n,k):
            if not len(q):
                return False
            s_f = s - q0 + n
            # if s_f >= k:
                # print('        Sum front?', s, '-', q0, '+', n,'=',s_f)                
            return s - q0 + n >= k
        for s in sums:            
            i = s[1]
            t = s[0]
            n = nums[i]
            # print('i =',i,'t =',t,'n =', n, q)
            while len(q) and valid_sum_front(t, q[0][0], n, k):
                left = q.popleft()
                l = min(l, i - left[1]+1)                
                # print('    Front: ', l, q )                
            while len(q) and q[-1][0] >= t:
                q.pop()
                # print('    Back: ', q)
            q.append(s)
            # print('    ', s,'==>', q)
        return -1 if l > len(nums) else l
            
