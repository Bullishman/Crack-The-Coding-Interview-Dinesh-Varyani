# 183. Valid Sudoku

**Difficulty**: Medium

**Topics**: Array, Hash Table, Matrix

**Link**: [https://leetcode.com/problems/valid-sudoku](https://leetcode.com/problems/valid-sudoku)

## Solution Explanation

The goal is to determine if a 9x9 Sudoku board is valid. A Sudoku board is valid if:
1. Each row contains the digits 1-9 without repetition.
2. Each column contains the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes contains the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need to be validated.

### **The `isValidSudoku` Function**

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
```

This function takes a 2D list `board` representing the Sudoku grid and returns a boolean.

#### **Variable Initialization**

```python
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
```

*   **`rows`**: An array of 9 sets, where `rows[i]` tracks the numbers seen in the i-th row.
*   **`cols`**: An array of 9 sets, where `cols[j]` tracks the numbers seen in the j-th column.
*   **`boxes`**: An array of 9 sets, where `boxes[k]` tracks the numbers seen in the k-th 3x3 sub-box.

#### **The Main Loop**

```python
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
```

We iterate through every cell `(r, c)` in the 9x9 board. If the cell is empty (`"."`), we skip it.

#### **Validation Logic**

For each non-empty cell:

1.  **Check Row:**
    ```python
                if val in rows[r]:
                    return False
                rows[r].add(val)
    ```
    If the value `val` is already in the set for the current row `r`, the board is invalid.

2.  **Check Column:**
    ```python
                if val in cols[c]:
                    return False
                cols[c].add(val)
    ```
    If `val` is already in the set for the current column `c`, the board is invalid.

3.  **Check 3x3 Box:**
    ```python
                idx = (r // 3) * 3 + (c // 3)
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
    ```
    The index for the 3x3 sub-box can be calculated using the formula `(r // 3) * 3 + (c // 3)`. This maps each cell to one of the 9 boxes (indexed 0 to 8). If `val` is already in the set for that box, the board is invalid.

#### **Conclusion**

```python
        return True
```

If we successfully iterate through the entire board without finding any repetitions, the board is valid.

### **Complexity Analysis**

*   **Time Complexity:** $O(1)$ or $O(81)$ since the board size is fixed at 9x9. We traverse each cell exactly once.
*   **Space Complexity:** $O(1)$ or $O(81)$ as the sets will store at most 81 elements in total across rows, columns, and boxes.
