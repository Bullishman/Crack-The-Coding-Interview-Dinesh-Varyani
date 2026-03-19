from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        count = Counter(nums)
        
        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    
                    backtrack()
                    
                    path.pop()
                    count[num] += 1
                    
        backtrack()
        return res
