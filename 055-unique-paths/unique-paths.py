class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]																	
        for i in range(m):																	
            for j in range(n):																		
                if i == 0 or j == 0:															
                    dp[i][j] = 1														
                else:															
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]