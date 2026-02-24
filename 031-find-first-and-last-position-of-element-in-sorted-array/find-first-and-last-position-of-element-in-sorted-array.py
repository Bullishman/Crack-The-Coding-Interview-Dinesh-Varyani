class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x: int) -> int:
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) //2
                if nums[m] < x:
                    l = m + 1
                else:
                    r = m
            
            return l
        
        low, high = search(target), search(target + 1) - 1

        if low <= high:
            return [low, high]

        return [-1, -1]