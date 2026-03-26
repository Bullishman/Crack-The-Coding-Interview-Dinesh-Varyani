class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        
        # Start from the second-to-last row, moving upwards to the peak
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Modify the current element in-place to store the minimum path sum
                # from the current position down to the base of the triangle.
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
                
        # The top element now inherently contains the global minimum path sum
        return triangle[0][0] if triangle else 0
