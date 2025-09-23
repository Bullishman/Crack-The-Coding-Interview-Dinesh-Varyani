class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]

        while low < high:
            mid = low + (high - low) // 2
            
            count = 0
            row, col = 0, n - 1
            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    count += (col + 1)
                    row += 1 
                else:
                    col -= 1

            if count < k:
                low = mid + 1
            else:
                high = mid
        
        return low