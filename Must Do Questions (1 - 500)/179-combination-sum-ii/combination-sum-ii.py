class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Sort the array so that identical elements are adjacent
        candidates.sort()
        res = []
        
        def backtrack(start, target_rem, path):
            # Base case: we've reached exactly the target sum
            if target_rem == 0:
                res.append(list(path))
                return
            # Base case: we've exceeded the target sum
            if target_rem < 0:
                return
            
            # Iterate through available candidates starting from 'start'
            for i in range(start, len(candidates)):
                # Skip identical elements to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # Prune the search tree: if candidate is greater than target_rem,
                # subsequent elements will be even greater, so we can break early
                if candidates[i] > target_rem:
                    break
                    
                # Include candidates[i] in the current subset and recurse
                path.append(candidates[i])
                backtrack(i + 1, target_rem - candidates[i], path)
                
                # Backtrack: remove the last element before trying the next candidate
                path.pop()
                
        # Start backtracking from index 0 with the initial target and an empty path
        backtrack(0, target, [])
        return res
