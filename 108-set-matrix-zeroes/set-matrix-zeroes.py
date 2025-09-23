class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
                                            
        m, n = len(matrix), len(matrix[0])																		
        zeroes_row, zeroes_col = [False] * m, [False] * n

        for i in range(m):																		
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes_row[i], zeroes_col[j] = True, True	
                                                                                
        for i in range(m):																		
            for j in range(n):																		
                if zeroes_row[i] or zeroes_col[j]:																
                    matrix[i][j] = 0
            