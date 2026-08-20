class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)

        # for row in isConnected:
        #     print(row)
        visited = set()

        def visit(i):
            visited.add(i)
            for j in range(N):
                if isConnected[i][j] == 0 or j in visited:
                    continue
                visit(j)

        ret = 0
        for i in range(N):
            if i in visited:
                continue
            ret += 1
            visit(i)

        return ret
