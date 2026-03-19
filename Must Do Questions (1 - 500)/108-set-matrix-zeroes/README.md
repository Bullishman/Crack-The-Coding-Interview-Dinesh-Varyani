# 108. Set Matrix Zeroes

**Difficulty**: Medium

**Topics**: Array, Hash Table, Matrix

**Link**: https://leetcode.com/problems/set-matrix-zeroes

Of course. Let's break down this code for setting matrix rows and columns to zero.

### High-Level Overview

The goal is to solve the "Set Matrix Zeroes" problem. Given a matrix of numbers, if any cell `(i, j)` has a value of 0, the entire `i`-th row and `j`-th column must be set to 0. This modification must be done "in-place," meaning we alter the original matrix directly.

A naive approach of zeroing out rows and columns as soon as you find a 0 will fail. The new zeros you write might cause a chain reaction, incorrectly zeroing out other rows and columns.

This code correctly solves the problem using a **two-pass approach** with auxiliary memory:

1.  **First Pass (Marking):** The code first iterates through the entire matrix to identify the locations of all the original zeros. Instead of modifying the matrix right away, it uses two separate boolean arrays (`zeroes_row` and `zeroes_col`) to "mark" which rows and columns need to be zeroed out.
2.  **Second Pass (Modifying):** After it has finished scanning the original matrix and marked all necessary rows and columns, it makes a second pass through the matrix. This time, it modifies the cells. For each cell `(i, j)`, it checks if its corresponding row `i` or column `j` was marked. If either is true, it sets the cell's value to 0.

This separation of "finding" and "modifying" prevents the chain reaction problem and leads to the correct result.

-----

### Line-by-Line Code Explanation

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Line 1: if not matrix: return
        # A simple edge case check. If the matrix is empty, there's nothing to do.
        if not matrix:
            return
                                                
        # Line 2: m, n = len(matrix), len(matrix[0])
        # Get the dimensions of the matrix: m rows and n columns.
        m, n = len(matrix), len(matrix[0])																		
        
        # Line 3: zeroes_row, zeroes_col = [False] * m, [False] * n
        # Create two boolean arrays to act as markers.
        # `zeroes_row` will have `m` elements, one for each row.
        # `zeroes_col` will have `n` elements, one for each column.
        # They are initialized to all `False`.
        zeroes_row, zeroes_col = [False] * m, [False] * n

        # --- PASS 1: Find and mark the rows/columns containing zeros ---
        # Line 4: for i in range(m):
        # Line 5:     for j in range(n):
        # Iterate through every cell (i, j) in the matrix.
        for i in range(m):																		
            for j in range(n):
                # Line 6: if matrix[i][j] == 0:
                # If we find a cell with the value 0...
                if matrix[i][j] == 0:
                    # Line 7: zeroes_row[i], zeroes_col[j] = True, True
                    # ...mark its corresponding row `i` and column `j` as True in our marker arrays.
                    zeroes_row[i], zeroes_col[j] = True, True	
                                                                    
        # --- PASS 2: Modify the matrix based on the markers ---
        # Line 8: for i in range(m):
        # Line 9:     for j in range(n):
        # Iterate through every cell (i, j) in the matrix again.
        for i in range(m):																		
            for j in range(n):																		
                # Line 10: if zeroes_row[i] or zeroes_col[j]:
                # For the current cell, check if its row `i` OR its column `j`
                # was marked as needing to be zeroed in the first pass.
                if zeroes_row[i] or zeroes_col[j]:																
                    # Line 11: matrix[i][j] = 0
                    # If the condition is true, set the current cell's value to 0.
                    matrix[i][j] = 0
```

-----

### Example Walkthrough

Let's trace the code with this example matrix:

```
matrix = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5]
]
```

**Initial State:**

  * `m = 3`, `n = 4`
  * `zeroes_row` = `[False, False, False]`
  * `zeroes_col` = `[False, False, False, False]`

#### Live Trace Table Map

**Pass 1: Marking Rows and Columns**

| `(i, j)` | `matrix[i][j]` | `matrix[i][j] == 0`? | `zeroes_row` after update | `zeroes_col` after update     |
| :------: | :------------: | :------------------: | :------------------------ | :---------------------------- |
| `(0, 0)` | 0              | `True`               | `[True, False, False]`    | `[True, False, False, False]` |
| `(0, 1)` | 1              | `False`              | (no change)               | (no change)                   |
| `(0, 2)` | 2              | `False`              | (no change)               | (no change)                   |
| `(0, 3)` | 0              | `True`               | `[True, False, False]`    | `[True, False, False, True]`  |
| `(1, 0)` | 3              | `False`              | (no change)               | (no change)                   |
| ...      | ...            | ...                  | ...                       | ...                           |
| `(2, 3)` | 5              | `False`              | (no change)               | (no change)                   |

**State after Pass 1:**

  * `zeroes_row` = `[True, False, False]` (Only row 0 had an initial zero)
  * `zeroes_col` = `[True, False, False, True]` (Columns 0 and 3 had initial zeros)
  * The `matrix` itself is still unchanged.

**Pass 2: Modifying the Matrix**

| `(i, j)` | `zeroes_row[i]` | `zeroes_col[j]` | `zeroes_row[i] or zeroes_col[j]`? | Action on `matrix[i][j]` |
| :------: | :-------------: | :-------------: | :------------------------------: | :----------------------- |
| `(0, 0)` | `True`          | `True`          | `True`                           | Set to 0                 |
| `(0, 1)` | `True`          | `False`         | `True`                           | Set to 0                 |
| `(0, 2)` | `True`          | `False`         | `True`                           | Set to 0                 |
| `(0, 3)` | `True`          | `True`          | `True`                           | Set to 0                 |
| `(1, 0)` | `False`         | `True`          | `True`                           | Set to 0                 |
| `(1, 1)` | `False`         | `False`         | `False`                          | No change (remains 4)    |
| `(1, 2)` | `False`         | `False`         | `False`                          | No change (remains 5)    |
| `(1, 3)` | `False`         | `True`          | `True`                           | Set to 0                 |
| `(2, 0)` | `False`         | `True`          | `True`                           | Set to 0                 |
| `(2, 1)` | `False`         | `False`         | `False`                          | No change (remains 3)    |
| `(2, 2)` | `False`         | `False`         | `False`                          | No change (remains 1)    |
| `(2, 3)` | `False`         | `True`          | `True`                           | Set to 0                 |

**Final Result:**
The function doesn't return anything, but the `matrix` is modified in-place to become:

```
[
  [0, 0, 0, 0],
  [0, 4, 5, 0],
  [0, 3, 1, 0]
]
```

-----

### Complexity Analysis

  * **Time Complexity:** $O(M \\times N)$, where `M` is the number of rows and `N` is the number of columns.
      * The code iterates through the entire `M x N` matrix twice, which results in $2 \\times M \\times N$ operations. In Big O notation, the constant 2 is dropped.
  * **Space Complexity:** $O(M + N)$.
      * This is the main characteristic of this specific solution. We use two auxiliary arrays, `zeroes_row` and `zeroes_col`, whose sizes are proportional to the number of rows and columns, respectively.
      * *(Note: A more advanced solution can achieve this with $O(1)$ constant space by cleverly using the first row and first column of the matrix itself as the marker arrays.)*