class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums.pop(0)]
        for num in nums:
            if num > arr[-1]:
                arr.append(num)
            else:
                arr[bisect_left(arr, num)] = num
        
        return len(arr)