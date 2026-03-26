import unittest
from typing import List

# Import from valid-sudoku.py
# Since it's in the same directory, we'll import it directly
from valid_sudoku import Solution

class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_board(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(self.solution.isValidSudoku(board))

    def test_invalid_board(self):
        board = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        # In this board, board[0][0] = '8' and board[3][0] = '8', which is in the same column.
        # So it should be invalid.
        self.assertFalse(self.solution.isValidSudoku(board))

if __name__ == "__main__":
    unittest.main()
