class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums, temp_nums, ans):
        if not nums:
            ans.append(temp_nums)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], temp_nums + [nums[i]], ans)