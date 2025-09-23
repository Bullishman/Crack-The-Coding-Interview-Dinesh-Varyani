# 110. Search A 2d Matrix

**Difficulty**: Medium

**Topics**: Array, Binary Search, Matrix

**Link**: https://leetcode.com/problems/search-a-2d-matrix

Of course. Let's break down this highly efficient code for searching in a 2D matrix.

### High-Level Overview

This code is designed to solve the "Search a 2D Matrix" problem, which has a specific set of rules for the input matrix:

1.  Each row is sorted from left to right.
2.  The first number in any row is greater than the last number of the row above it.

These two rules mean that the entire matrix can be treated as a single, flattened, sorted 1D array. For example:

```
[ [ 1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60] ]
```

is functionally equivalent to the sorted array:
`[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]`

The algorithm cleverly leverages this property. Instead of performing a complex 2D search, it performs a classic **Binary Search** on this "virtual" 1D array. It uses mathematical formulas to map the 1D `mid` index of the binary search back to the `(row, col)` coordinates in the 2D matrix.

-----

### Prerequisites: Mapping 1D Index to 2D Coordinates

The most crucial part of this algorithm is converting a 1D array index (`mid`) into 2D matrix coordinates (`row`, `col`). This is done with simple integer arithmetic. If a matrix has `n` columns:

  * `row = index // n` (Integer division gives the row number)
  * `col = index % n` (Modulo operation gives the column number)

**Example:** In the matrix above, `n = 4`. Let's find the element at virtual index `mid = 6`.

  * `row = 6 // 4 = 1`
  * `col = 6 % 4 = 2`
  * The element is at `matrix[1][2]`, which is `16`. This is correct.

The code uses `divmod(mid, n)`, which is a built-in Python function that efficiently computes both the quotient (`//`) and the remainder (`%`) at the same time.

-----

### Line-by-Line Code Explanation

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Line 1: if not matrix: return False
        # Edge case: If the matrix is empty, the target cannot be in it.
        if not matrix:
            return False
            
        # Line 2: m, n = len(matrix), len(matrix[0])
        # Get the dimensions: m rows and n columns.
        m, n = len(matrix), len(matrix[0])
        
        # Line 3: left, right = 0, m * n - 1
        # Initialize the pointers for our binary search. Instead of a 2D space,
        # we define a 1D search space from the first element (index 0)
        # to the last element (index m * n - 1).
        left, right = 0, m * n - 1

        # Line 4: while left <= right:
        # This is the standard condition for a binary search loop. It continues
        # as long as our search space is valid.
        while left <= right:
            
            # Line 5: mid = (left + right) // 2
            # Calculate the middle index of the current search space.
            mid = (left + right) // 2
            
            # Line 6: mid_row, mid_col = divmod(mid, n)
            # Convert the 1D `mid` index into 2D (row, col) coordinates.
            mid_row, mid_col = divmod(mid, n)

            # Line 7: if matrix[mid_row][mid_col] == target:
            # Check if the element at the middle of our search space is the target.
            if matrix[mid_row][mid_col] == target:
                # Line 8: return True
                # If it is, we've found it!
                return True
                
            # Line 9: elif matrix[mid_row][mid_col] < target:
            # If the middle element is smaller than the target...
            elif matrix[mid_row][mid_col] < target:
                # Line 10: left = mid + 1
                # ...we know the target must be in the "right half" of our search space.
                # So, we discard the left half by moving the `left` pointer.
                left = mid + 1
                
            # Line 11: else:
            # If the middle element is greater than the target...
            else:
                # Line 12: right = mid - 1
                # ...we know the target must be in the "left half".
                # So, we discard the right half by moving the `right` pointer.
                right = mid - 1

        # Line 13: return False
        # If the `while` loop finishes without finding the target (i.e., `left` becomes
        # greater than `right`), it means the target is not in the matrix.
        return False
```

-----

### Example Walkthroughs

Let's use the following matrix for our examples:
`matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]`

  * `m = 3`, `n = 4`
  * `left = 0`, `right = 3 * 4 - 1 = 11`

#### Example 1: `target = 3` (Target is Found)

| Iteration | `left` | `right` | `mid` | `divmod(mid, 4)` | `matrix[row][col]` | Comparison vs `target=3` | Action              |
| :-------: | :----: | :-----: | :---: | :---------------: | :----------------: | :----------------------- | :------------------ |
| 1         | 0      | 11      | 5     | `(1, 1)`          | 11                 | `11 > 3`                 | `right = 5 - 1 = 4`   |
| 2         | 0      | 4       | 2     | `(0, 2)`          | 5                  | `5 > 3`                  | `right = 2 - 1 = 1`   |
| 3         | 0      | 1       | 0     | `(0, 0)`          | 1                  | `1 < 3`                  | `left = 0 + 1 = 1`    |
| 4         | 1      | 1       | 1     | `(0, 1)`          | 3                  | `3 == 3`                 | **`return True`** |

#### Example 2: `target = 13` (Target is Not Found)

| Iteration | `left` | `right` | `mid` | `divmod(mid, 4)` | `matrix[row][col]` | Comparison vs `target=13` | Action              |
| :-------: | :----: | :-----: | :---: | :---------------: | :----------------: | :------------------------ | :------------------ |
| 1         | 0      | 11      | 5     | `(1, 1)`          | 11                 | `11 < 13`                 | `left = 5 + 1 = 6`    |
| 2         | 6      | 11      | 8     | `(2, 0)`          | 23                 | `23 > 13`                 | `right = 8 - 1 = 7`   |
| 3         | 6      | 7       | 6     | `(1, 2)`          | 16                 | `16 > 13`                 | `right = 6 - 1 = 5`   |

At this point, `left` is `6` and `right` is `5`. The `while left <= right` condition becomes `False`, and the loop terminates.

  * **Line 13:** The function proceeds to `return False`.

-----

### Complexity Analysis

  * **Time Complexity:** $O(\\log(M \\times N))$
      * This is the standard time complexity for a binary search. The total number of elements in our search space is $M \\times N$. In each step, we cut the search space in half.
  * **Space Complexity:** $O(1)$
      * The algorithm is very space-efficient. It only uses a few variables to store pointers and dimensions (`m`, `n`, `left`, `right`, `mid`, etc.). The space required is constant and does not grow with the size of the input matrix.