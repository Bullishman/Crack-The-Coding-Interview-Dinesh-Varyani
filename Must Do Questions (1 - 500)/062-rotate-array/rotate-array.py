class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copied_nums = nums[:]
        for i, num in enumerate(copied_nums):
            nums[(i + k) % len(nums)] = copied_nums[i]