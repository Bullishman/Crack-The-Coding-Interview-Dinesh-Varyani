# 12. Number Of Islands

**Difficulty**: Medium

**Topics**: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

**Link**: https://leetcode.com/problems/number-of-islands

Of course. This code solves the "Number of Islands" problem, a classic graph traversal question on a 2D grid.

### The Core Idea

The algorithm iterates through every cell of the grid. If it finds a cell that is land (`'1'`), it knows it has found a new, undiscovered island. It then does two things:

1.  Increments the island `count`.
2.  Immediately launches a **Depth-First Search (DFS)** from that cell. The DFS is responsible for finding every piece of land connected to that starting point and "sinking" it (by changing its value from `'1'` to `'0'`).

By "sinking" the entire island as soon as its first piece is discovered, we ensure that we will never count the same island more than once.

Let's break down the code line by line with an example.

**Example:**

```python
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

**Expected Result:** `3`

-----

### The `numIslands` (Outer) Function

This function is the main driver that scans the grid and coordinates the search.

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
```

This defines the main function.

```python
        # ... (dfs function definition) ...

        count = 0
```

A variable `count` is initialized to `0`. This will keep track of the number of islands we find.

```python
        for i in range(len(grid)):
            for j in range(len(grid[0])):
```

These nested `for` loops iterate through every cell of the grid, with `i` being the row index and `j` being the column index.

```python
                if grid[i][j] == '1':
```

This is the trigger. If the cell at `(i, j)` contains a `'1'`, it means we have found a piece of land that has not yet been visited (or "sunk").

```python
                    dfs(i, j)
```

As soon as we find the first piece of a new island, we call our `dfs` helper function. The job of this `dfs` call is to find and sink all connected parts of this *single* island.

```python
                    count += 1
```

**After** the `dfs` function has completed its work (meaning the entire island starting at `(i, j)` has been sunk), we increment our `count` by one.

```python
        return count
```

After the nested loops have scanned every cell in the grid, the final `count` is returned.

-----

### The `dfs` (Recursive Helper) Function

This is the recursive engine that explores and "sinks" a single island.

```python
        def dfs(i, j):
```

The function takes the coordinates `i` and `j` of the cell to explore.

#### **The Base Case / Guard Clause**

```python
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1'):
                return
```

This is the stopping condition for the recursion. The function will stop and return if any of the following are true:

1.  The `i` coordinate is out of bounds (off the top or bottom).
2.  The `j` coordinate is out of bounds (off the left or right).
3.  The cell at `(i, j)` is water (`'0'`) or has already been visited (and turned into `0`).

#### **The "Sinking" or Marking Step**

```python
            grid[i][j] = '0'
```

This is the most crucial step within the `dfs`. To mark the current cell as "visited" and prevent infinite loops, we immediately change its value from `'1'` to `'0'`. This is like sinking that piece of the island so we don't visit it again.

#### **The Recursive Exploration**

```python
            dfs(i + 1, j) # Down
            dfs(i - 1, j) # Up
            dfs(i, j + 1) # Right
            dfs(i, j - 1) # Left
```

From the current cell, the function calls itself for all four adjacent neighbors (down, up, right, left). This creates a chain reaction that explores every connected `'1'` in the current island.

-----

### **Live Trace Table Map**

A traditional table is hard for a 2D problem, so let's trace the state of the `grid` and `count` at key moments.

**Initial State:**
`count = 0`
`grid` = `[["1","1","0",...], ["1","1","0",...], ...]`

-----

**Main loop `(i=0, j=0)`:**

  * `grid[0][0]` is `'1'`. This is a new island.
  * **Call `dfs(0, 0)`**. This will recursively find and change all connected `'1'`s to `'0'`s.
  * **`count` becomes `1`**.
  * **State of `grid` after `dfs(0,0)` returns:**

<!-- end list -->

```
  [["0","0","0","0","0"],
   ["0","0","0","0","0"],
   ["0","0","1","0","0"],
   ["0","0","0","1","1"]]
```

-----

**Main loop continues...**

  * It scans through all the cells that are now `'0'`s and does nothing.
  * ...
  * **Main loop `(i=2, j=2)`:**
  * `grid[2][2]` is `'1'`. This is a new island.
  * **Call `dfs(2, 2)`**. This finds only one piece of land.
  * **`count` becomes `2`**.
  * **State of `grid` after `dfs(2,2)` returns:**

<!-- end list -->

```
  [["0","0","0","0","0"],
   ["0","0","0","0","0"],
   ["0","0","0","0","0"],
   ["0","0","0","1","1"]]
```

-----

**Main loop continues...**

  * ...
  * **Main loop `(i=3, j=3)`:**
  * `grid[3][3]` is `'1'`. This is a new island.
  * **Call `dfs(3, 3)`**. This will find and sink both `grid[3][3]` and `grid[3][4]`.
  * **`count` becomes `3`**.
  * **State of `grid` after `dfs(3,3)` returns:**

<!-- end list -->

```
  [["0","0","0","0","0"],
   ["0","0","0","0","0"],
   ["0","0","0","0","0"],
   ["0","0","0","0","0"]]
```

-----

The main loops finish scanning the rest of the grid, finding no more `'1'`s.

The function returns the final `count`, which is **3**.