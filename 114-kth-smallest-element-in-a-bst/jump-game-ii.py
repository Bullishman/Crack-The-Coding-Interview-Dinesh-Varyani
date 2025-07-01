class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        jump_count = 0
        current_reach = 0
        max_reach = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == current_reach:
                jump_count += 1
                current_reach = max_reach

                if current_reach >= len(nums) - 1:
                    return jump_count
                    
        return jump_count