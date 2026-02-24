class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, nums[i] + i)

        return True