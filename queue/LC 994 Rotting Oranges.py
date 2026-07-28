class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        q = deque()
        good = 0        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good+=1
                if grid[i][j] != 2:
                    continue
                q.append([i, j])

        minutes = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]        
        while q:
            minutes += 1
            l = len(q)
            for i in range(l):
                x0, y0 = q.popleft()                
                for dx, dy in dirs:
                    x1 = x0 + dx
                    y1 = y0 + dy
                    if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n or grid[x1][y1] in [0, 2]:
                        continue
                    grid[x1][y1] = 2
                    good-=1
                    q.append([x1, y1])
        if good:
            return -1
        return minutes - 1 if minutes else 0
