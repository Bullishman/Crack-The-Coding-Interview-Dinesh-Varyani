class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        result = []
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]

        p = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= p
            p *= nums[j]
        
        return result