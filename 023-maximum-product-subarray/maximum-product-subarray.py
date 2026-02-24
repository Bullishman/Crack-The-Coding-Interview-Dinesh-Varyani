class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        min_num, max_num, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            min_num *= num
            max_num *= num
            min_num, max_num = min(min_num, max_num, num), max(min_num, max_num, num)
            res = max(res, max_num)
        
        return res