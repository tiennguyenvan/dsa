class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        if grid[0][0] == 0:
            q.append([0,0])
            grid[0][0] = 1
        lvl = 0
        while len(q):
            l = len(q)
            lvl+=1
            for _ in range(l):
                r,c = q.popleft()
                if r == m-1 and c == n - 1: return lvl
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i == 0 and j == 0: continue
                        x = r + i
                        y = c + j
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 0: 
                            continue
                        # print((x,y))
                        if x==m-1 and y == n-1: return lvl+1
                        q.append([x,y])
                        grid[x][y] = 1
        return -1