class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        r, mx = -1, -1e6
        for i in range(n):
            if nums[i] >= mx:
                mx = nums[i]
            else:
                r = i

        l, mn = n, 1e6
        for i in range(n - 1, -1, -1):
            if nums[i] <= mn:
                mn = nums[i]
            else:
                l = i

        return max(0, r - l + 1)