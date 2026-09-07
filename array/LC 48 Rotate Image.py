class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0,0 -> 1,1 -> 2,2 ... < n//2, n//2
        # transform: row,col become col, n - 1 - row

        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n - i-1):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1 -
                                                                             j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
