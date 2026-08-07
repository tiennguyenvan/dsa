class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        
        def matrixVal(i):
            row = i // n
            col = i % n
            return matrix[row][col]
        
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (right + left) // 2
            if target == matrixVal(mid):
                return True
            if target < matrixVal(mid):
                right = mid - 1
                continue
            left = mid + 1
            
        return False