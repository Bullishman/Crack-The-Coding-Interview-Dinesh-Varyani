class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        nums.append(float('-inf'))
        while l <= r:
            m = l + (r - l) // 2
            if nums[m - 1] < nums[m] and nums[m + 1] < nums[m]:
                return m
            elif nums[m - 1] > nums[m]:
                r = m - 1
            else:
                l = m + 1