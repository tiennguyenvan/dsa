class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ret = float("-inf")
        q = deque()
        def val(p1,p2):
            return p1[1] + p2[1] + abs(p1[0] - p2[0])
        
        for p in points:
            x,y = p
            print((x,y))
            if not q:
                q.append((x,y))
                # print("    queue:", q)
                continue
            while q and q[0][0] + k < x:                
                # print('    out range', q[0][0], '+', k, '=', q[0][0] + k)
                q.popleft()
            best = float("-inf") if not q else val(q[0], (x,y))
            ret = max(best, ret)                        
            cur_val = val(p,p)
            # print('    cur_val', cur_val)
            while q and val(q[-1], p) <= cur_val:                
                last = q.pop()
                # print('    pop_val', last, val(last,p))
            q.append((x,y))
            # print("    queue:", q)
        return ret