class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set(nums)

        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                return num