class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # pick all rotted oranges to start with
        q = deque()
        fresh = 0
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell == 2:
                    q.append((i,j))
                    continue
                if cell == 1:
                    fresh+=1
        if fresh == 0: return 0
        if len(q) == 0: return -1
        time = 0
        # print(q, fresh)
        dirs = [(1,0), (-1,0), (0,-1), (0,1)]
        
        while q:
            time += 1
            bk_fresh = fresh
            l = len(q)
            # print(time)
            for _ in range(l):
                (i,j) = q.popleft()
                # print(i,j)
                for a,b in dirs:
                    x = i + a
                    y = j + b
                    # print(f'  {x}, {y}')
                    is_fresh = x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1
                    if is_fresh:
                        grid[x][y] = 2
                        q.append((x,y))
                        fresh -= 1
                        if fresh == 0: return time
                        
            # print(grid, fresh)
            if bk_fresh == fresh: return -1
        return time
