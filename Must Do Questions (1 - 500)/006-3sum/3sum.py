class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums.sort()
        n = len(nums)

        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif tot < 0:
                    j += 1
                else:
                    k -= 1

        return [list(i) for i in s]