class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')

        for i in range(n - 1):
            l, r = i + 1, n - 1
            while l < r:
                temp_sum = nums[l] + nums[r] + nums[i]
                if temp_sum == target: 
                    return temp_sum

                if temp_sum > target: 
                    r -= 1
                else: 
                    l += 1
                    
                ans = min(ans, temp_sum, key=lambda x: abs(target - x))
        return ans