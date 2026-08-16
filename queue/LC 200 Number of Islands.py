class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        ret = 0

        def eraseIsland(r:int, c:int):
            q = deque()
            q.append( (r,c) )
            grid[r][c] = "0"
            
            dirs = [ (-1,0), (1,0), (0, -1), (0, 1) ]

            while q:
                l = len(q)
                for i in range(l):
                    a,b = q.popleft()
                    for dx, dy in dirs:
                        x = a + dx
                        y = b + dy

                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                            continue
                        q.append( (x,y) )
                        grid[x][y] = '0'

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '0':
                    continue
                
                ret += 1
                eraseIsland(r,c)

        return ret

