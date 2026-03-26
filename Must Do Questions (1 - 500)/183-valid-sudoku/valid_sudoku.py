from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # Check row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # Check column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # Check 3x3 box
                # Box index is (r // 3) * 3 + (c // 3)
                idx = (r // 3) * 3 + (c // 3)
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
                
        return True
