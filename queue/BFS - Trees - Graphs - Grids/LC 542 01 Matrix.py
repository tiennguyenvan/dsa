class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])        
        dirs = [
            (1,0), (-1,0), (0, 1), (0, -1)
        ]
        q = deque()        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))                          
        while q:
            i,j = q.popleft()            
            for a,b in dirs:
                x,y = i+a,j+b
                if x < 0 or x >= m: continue
                if y < 0 or y >= n: continue
                if mat[x][y] <= 0: continue
                mat[x][y] = mat[i][j] - 1
                q.append((x,y))

        for i in range(m):
            for j in range(n):
                mat[i][j] = -mat[i][j]
        

        return mat