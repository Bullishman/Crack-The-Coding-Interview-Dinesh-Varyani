# 131. Max Area Of Island

**Difficulty**: Medium

**Topics**: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

**Link**: https://leetcode.com/problems/max-area-of-island

Of course. Let's break down this classic grid traversal problem.

### The Logic: Depth-First Search (DFS)

The code uses a common and effective strategy to solve this problem. It iterates through every cell of the grid. If it finds a cell that is part of an island (`grid[i][j] == 1`), it triggers a **Depth-First Search (DFS)** starting from that cell.

The `dfs` helper function does three key things:

1.  **Counts:** It counts the current land cell (`1`) it's on.
2.  **Sinks the Island:** It changes the value of the current land cell from `1` to `0`. This is a crucial step to ensure that we don't visit this same cell again and recount it as part of another search.
3.  **Explores Neighbors:** It recursively calls itself for all four adjacent neighbors (up, down, left, right).

The main function keeps track of the largest area found so far and returns it after checking the entire grid.

### The Example

Let's trace the code with the following grid. It has two islands, one with an area of 5 and another with an area of 2.

  * **Grid**:
    ```
    [[0, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 1],
     [1, 1, 0, 0]]
    ```
  * **Expected Result**: `5`

-----

### Code and Live Demonstration

#### 1\. Setup (Main Function)

```python
        m, n = len(grid), len(grid[0])
        # m = 4, n = 4
        max_area = 0
        # max_area = 0
```

  * We get the dimensions of the grid and initialize `max_area` to `0`.

#### 2\. Main Loops

```python
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
```

  * The code starts scanning the grid from `(0, 0)`.
  * It finds `0`s until it reaches `(0, 1)`.
  * At `(i=0, j=1)`, `grid[0][1]` is `1`. This triggers the first call to `dfs(0, 1)`.

-----

### **Live Trace Table Map (First DFS Call)**

This trace shows how `dfs(0, 1)` explores the first, larger island.

**Call Stack & Grid State:**

| DFS Call | `(i, j)` | Condition Check | Action on `grid` | Return Value Calculation | Returns |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`dfs(0, 1)`** | `(0, 1)` | In bounds, `grid[0][1]==1` | `grid[0][1] = 0` | `1 + dfs(1,1) + dfs(-1,1) + dfs(0,2) + dfs(0,0)` | **5** |
|   ↳ **`dfs(1, 1)`**| `(1, 1)` | In bounds, `grid[1][1]==1` | `grid[1][1] = 0` | `1 + dfs(2,1) + dfs(0,1) + dfs(1,2) + dfs(1,0)` | **3** |
|     ↳ **`dfs(2, 1)`**| `(2, 1)` | In bounds, `grid[2][1]==0` | - | `0` (Base case) | **0** |
|     ↳ **`dfs(0, 1)`**| `(0, 1)` | In bounds, `grid[0][1]==0` | - | `0` (Base case, already sunk) | **0** |
|     ↳ **`dfs(1, 2)`**| `(1, 2)` | In bounds, `grid[1][2]==0` | - | `0` (Base case) | **0** |
|     ↳ **`dfs(1, 0)`**| `(1, 0)` | In bounds, `grid[1][0]==0` | - | `0` (Base case) | **0** |
|   ↳ **`dfs(-1, 1)`**| `(-1, 1)`| `i < 0` | - | `0` (Base case, out of bounds) | **0** |
|   ↳ **`dfs(0, 2)`**| `(0, 2)` | In bounds, `grid[0][2]==1` | `grid[0][2] = 0` | `1 + dfs(1,2) + dfs(-1,2) + dfs(0,3) + dfs(0,1)` | **1** |
|     ↳ ... | ... | (All neighbors are 0 or out of bounds) | - | Returns 0 for all calls | ... |
|   ↳ **`dfs(0, 0)`**| `(0, 0)` | In bounds, `grid[0][0]==0` | - | `0` (Base case) | **0** |

  * **After `dfs(0, 1)` returns:**
      * The `dfs` call returns the total area it found: `5`.
      * The main loop updates `max_area`: `max_area = max(0, 5)` -\> `max_area` is now `5`.
      * The grid now looks like this (the first island is "sunk"):
        ```
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 1],
         [1, 1, 0, 0]]
        ```

#### 3\. Continuing the Main Loops

  * The `for` loops continue scanning from where they left off.
  * They will pass over `(0, 2)`, `(1, 1)`, etc., because the `if grid[i][j] == 1` condition is now false for those cells.
  * The scan continues until it reaches `(2, 2)`.
  * At `(i=2, j=2)`, `grid[2][2]` is `1`. This triggers a new DFS call: `dfs(2, 2)`.

-----

#### **Second DFS Call (for the smaller island)**

  * `dfs(2, 2)` is called.

      * It sinks `grid[2][2]`.
      * It recursively calls `dfs(2, 3)` (which sinks `grid[2][3]`) and `dfs(3, 2)` (which finds `grid[3][2]` is `0`).
      * The calls explore the connected components and eventually return `2`.

  * **After `dfs(2, 2)` returns:**

      * The main loop updates `max_area`: `max_area = max(5, 2)` -\> `max_area` remains `5`.
      * The grid is now fully sunk.

-----

#### 4\. Final Loops and Return

  * The main loops continue scanning the rest of the grid.
  * They find another `1` at `(3, 0)` and start a `dfs` call there.
  * The `dfs(3,0)` will explore `(3,0)` and `(3,1)` and return an area of `2`.
  * The main loop updates `max_area = max(5, 2)`, so it remains `5`.
  * After the loops finish scanning the entire grid, the function returns the final `max_area`.

<!-- end list -->

```python
        return max_area  # Returns 5
```