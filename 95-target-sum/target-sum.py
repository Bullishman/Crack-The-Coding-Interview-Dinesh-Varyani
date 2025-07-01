class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        subset_sum_target = (total_sum + target) // 2

        dp = [0] * (subset_sum_target + 1)
        
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum_target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum_target]