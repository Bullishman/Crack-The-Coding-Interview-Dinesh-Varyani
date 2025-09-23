class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, l = 0, 0
        size = float("inf")

        for r in range(len(nums)):
            ans += nums[r]

            while ans >= target:
                size = min(size, r-l+1)
                ans -= nums[l]
                l += 1
                
        return size if size != float("inf") else 0