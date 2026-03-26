# 180. Triangle

**Difficulty**: Medium

**Topics**: Array, Dynamic Programming

**Link**: https://leetcode.com/problems/triangle

This problem can be solved optimally using an **In-place Bottom-Up Dynamic Programming** approach.

### The Core Idea

The goal is to find the minimum path sum from the top of the triangle to its base. Instead of trying all paths top-down (which leads to overlapping subproblems and potential exponential time), we can evaluate the triangle **bottom-up**.

By starting from the second-to-last row and moving upwards, we can treat every element as the "top" of a smaller sub-triangle. We compute the minimum path sum from that element to the base by adding the element's own value to the minimum of its two direct children from the row beneath it. 

Because we are allowed to mutate the input, we can overwrite each element with this computed minimum sum. Once we reach the very top of the triangle, the single element `triangle[0][0]` will represent the minimum path sum for the entire triangle.

Let's break down the code line by line with an example.

**Example:**
```
triangle = [
     [2],
    [3, 4],
   [6, 5, 7],
  [4, 1, 8, 3]
]
```
**Expected Result:** `11` (Path: `2 -> 3 -> 5 -> 1`)

-----

### **Initial Setup & Iteration Logic**

```python
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        
        for row in range(n - 2, -1, -1):
```

  * **What it does:** We determine the number of rows `n`. We then start our loop from `n - 2` (the second-to-last row) and step backward `-1` until we reach row `0`. We don't process the very bottom row `n - 1` because its elements already represent the minimum path sum to the base!

#### **The Inner Loop & Overwriting State**

```python
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
```

  * **What it does:** We iterate through every element in the current `row`.
  * For the element at `triangle[row][col]`, its two children in the row below are at the identical column index `col` and the adjacent index `col + 1` (`triangle[row + 1][col]` and `triangle[row + 1][col + 1]`).
  * We pick the minimum of these two children and add it directly to the current element. This overwrites `triangle[row][col]` to store the optimal sum from itself down to the bottom.

#### **Final Return**

```python
        return triangle[0][0] if triangle else 0
```

  * Once the loops finish running all the way through row `0`, the element at the tip of the triangle, `triangle[0][0]`, inherently contains the minimum sum of the entire structure.

-----

### **Live Trace Table Map**

**Initial `triangle`:**
```
Row 0: [2]
Row 1: [3, 4]
Row 2: [6, 5, 7]
Row 3: [4, 1, 8, 3]
```

| Step | `row` | `col` | Current Val | Children in Row Below | Minimum Child | New Value (Val + Min Child) |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 1 | `2` | `0` | `6` | `4` (col 0), `1` (col 1) | `1` | `6 + 1 = 7` |
| 2 | `2` | `1` | `5` | `1` (col 1), `8` (col 2) | `1` | `5 + 1 = 6` |
| 3 | `2` | `2` | `7` | `8` (col 2), `3` (col 3) | `3` | `7 + 3 = 10` |

**State after evaluating Row 2:**
```
Row 0: [2]
Row 1: [3, 4]
Row 2: [7, 6, 10]    <-- Updated
Row 3: [4, 1, 8, 3]
```

| Step | `row` | `col` | Current Val | Children in Row Below | Minimum Child | New Value (Val + Min Child) |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 4 | `1` | `0` | `3` | `7` (col 0), `6` (col 1) | `6` | `3 + 6 = 9` |
| 5 | `1` | `1` | `4` | `6` (col 1), `10` (col 2) | `6` | `4 + 6 = 10` |

**State after evaluating Row 1:**
```
Row 0: [2]
Row 1: [9, 10]       <-- Updated
Row 2: [7, 6, 10]
...
```

| Step | `row` | `col` | Current Val | Children in Row Below | Minimum Child | New Value (Val + Min Child) |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 6 | `0` | `0` | `2` | `9` (col 0), `10` (col 1) | `9`| `2 + 9 = 11` |

**Final State of Row 0:**
```
Row 0: [11]          <-- Final Answer
```

The algorithm returns `11`.
