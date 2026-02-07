class Solution:
    def numSquares(self, n: int) -> int:
        maxPerfect = int(n ** 0.5)
        perfectSquares = [x * x for x in range(1,maxPerfect+1)]
        perfectSquares.reverse()
        q = deque(perfectSquares)
        cur_lvl = 1
        while q:
            l = len(q)
            for _ in range(l):
                val = q.popleft()
                if val == n: return cur_lvl
                for psq in perfectSquares:
                    new_val = val + psq                    
                    if new_val == n:
                        return cur_lvl + 1
                    if new_val > n:
                        continue
                    q.append(new_val)                
            cur_lvl += 1
        return cur_lvl