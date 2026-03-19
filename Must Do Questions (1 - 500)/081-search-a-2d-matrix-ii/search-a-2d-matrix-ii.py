class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not target:
            return False

        r, c = 0, len(matrix[0]) - 1

        while r <= len(matrix) - 1 and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1

        return False