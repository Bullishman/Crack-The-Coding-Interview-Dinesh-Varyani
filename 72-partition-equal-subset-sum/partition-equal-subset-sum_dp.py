class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_num = sum(nums)
        
        if total_num % 2 == 1:
            return False
        
        target_num = total_num // 2
        dp = [True] + [False] * total_num
        
        for num in nums:
            for j in range(total_num, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target_num]