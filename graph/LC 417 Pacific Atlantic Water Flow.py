class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(1,0), (0,1), (-1, 0), (0,-1)]

        def BFS(initR, initCol):
            q = deque()
            visited = set()
            for c in range(COLS):
                q.append((initR, c))
                visited.add((initR, c))
            for r in range(ROWS):
                q.append((r,initCol))
                visited.add((r,initCol))
            while q: 
                x,y = q.popleft()
                for dx,dy in DIRS:
                    x1, y1 = x+dx, y+dy
                    if (x1 < 0 or x1 >= ROWS or 
                        y1 < 0 or y1 >= COLS or 
                        (x1,y1) in visited or
                        heights[x][y] > heights[x1][y1]
                    ):
                        continue
                    q.append((x1,y1))
                    visited.add((x1,y1))
            return visited

        fromPO = BFS(0,0)
        fromAO = BFS(ROWS-1, COLS-1)
        return [[a,b] for a,b in fromPO if (a,b) in fromAO]