from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Calculates the area of the largest square of '1's in the matrix.
        
        This uses a dynamic programming approach. The state dp[i][j] stores
        the side length of the largest square whose bottom-right corner is
        at matrix[i-1][j-1].
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        
        # Create a dp table with an extra row and column to simplify boundary checks.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side_length = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # We only care about cells that are '1's in the original matrix.
                if matrix[i-1][j-1] == '1':
                    # The side length of the square ending here is limited by its
                    # top, left, and top-left diagonal neighbors.
                    dp[i][j] = min(dp[i-1][j],      # Top neighbor
                                   dp[i][j-1],      # Left neighbor
                                   dp[i-1][j-1]) + 1 # Top-left neighbor
                    
                    # Keep track of the maximum side length found so far.
                    max_side_length = max(max_side_length, dp[i][j])
        
        # The final answer is the area of the largest square.
        return max_side_length ** 2