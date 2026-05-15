class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshMap = Counter()       
        q = deque()
        nr = len(grid)
        nc = len(grid[0])
        
        for i in range(nr):
            for j in range(nc):
                o = grid[i][j]
                if o == 0:
                    continue
                if o == 1:
                    freshMap[(i,j)] = 1
                if o == 2:
                    q.append((i,j))

        minutes = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q and len(freshMap):
            ql = len(q)
            for qi in range(ql):
                i,j = q.popleft()
                grid[i][j] = 0
                for d in dirs:
                    r, c = i+d[0], j+d[1]                    
                    if r < 0 or r >= nr or c < 0 or c >= nc:
                        continue
                    if grid[r][c] == 0 :
                        continue
                    if grid[r][c] == 1:
                        del freshMap[(r,c)]
                        q.append((r,c))
            if not q: 
                break
            minutes+=1           
        
        
        return minutes if len(freshMap) == 0 else -1