# 107. Rotting Oranges

**Difficulty**: Medium

**Topics**: Array, Breadth-First Search, Matrix

**Link**: https://leetcode.com/problems/rotting-oranges

Of course. Let's break down this classic "Rotting Oranges" problem, which is a perfect example of a Breadth-First Search (BFS) algorithm.

### High-Level Overview

The goal is to find the minimum number of minutes required for all fresh oranges (value `1`) to become rotten (value `2`). The rot spreads from a rotten orange to its adjacent (up, down, left, right) fresh neighbors every minute. If some fresh oranges can never be reached, the task is impossible.

This problem is modeled as a **Multi-Source Breadth-First Search (BFS)** on a grid.

  * **Graph:** The grid itself is the graph, where each cell is a node.
  * **Shortest Path:** BFS is the ideal algorithm for finding the shortest path (in this case, minimum time) from a source to other nodes. Since the rot spreads one layer at a time per minute, this maps perfectly to the levels of a BFS traversal.
  * **Multi-Source:** We can have multiple rotten oranges at the start. BFS handles this naturally by putting all initial rotten oranges into the queue at "time 0".

The strategy is:

1.  **Initialization:** Find all initially rotten oranges and add them to a queue. Each item in the queue will store the orange's `[row, col, time]`.
2.  **BFS Traversal:** Process the queue level by level. For each rotten orange taken from the queue, "infect" its fresh neighbors, mark them as rotten, and add them to the queue with an incremented timestamp (`time + 1`).
3.  **Track Time:** The `time` of the last orange to be processed will be the total minutes elapsed.
4.  **Validation:** After the process is complete, check the grid one last time. If any fresh oranges (`1`) remain, they were unreachable, and we should return `-1`.

-----

### Line-by-Line Code Explanation

```python
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Line 1: m, n = len(grid), len(grid[0])
        # Get the dimensions of the grid: m rows, n columns.
        m, n = len(grid), len(grid[0])
        
        # Line 2: queue = []
        # Initialize a queue to store the rotten oranges we need to process.
        # We use a list here, but collections.deque is more efficient for pop(0).
        queue = []

        # --- Phase 1: Find all initially rotten oranges ---
        # Line 3: for i in range(m):
        # Line 4:     for j in range(n):
        # Iterate through every cell in the grid.
        for i in range(m):
            for j in range(n):
                # Line 5: if grid[i][j] == 2:
                # If a cell contains a rotten orange...
                if grid[i][j] == 2:
                    # Line 6: queue.append([i, j, 0])
                    # Add it to the queue with its coordinates (i, j) and the
                    # starting time, which is 0 minutes.
                    queue.append([i, j, 0])

        # Line 7: ans = 0
        # This variable will store the maximum time elapsed, which is our answer.
        ans = 0
        
        # --- Phase 2: The BFS Traversal ---
        # Line 8: while queue:
        # The loop continues as long as there are rotten oranges to process.
        while queue:
            # Line 9: i, j, time = queue.pop(0)
            # Dequeue the next rotten orange. This gives us its location (i, j)
            # and the time it took to become rotten (`time`).
            i, j, time = queue.pop(0)
            
            # Line 10: ans = time
            # Since we process oranges in the order they rot (level by level),
            # the `time` of the last processed orange will be the final answer.
            ans = time
            
            # Line 11: for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            # Iterate through the four possible directions: right, left, up, down.
            for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                # Line 12: ni, nj = i + x, j + y
                # Calculate the coordinates of the neighbor cell.
                ni, nj = i + x, j + y

                # Line 13: if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                # Check if the neighbor is valid:
                # 1. It's within the grid boundaries.
                # 2. It contains a fresh orange (value 1).
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    # Line 14: grid[ni][nj] = 2
                    # If it's a valid fresh orange, it now becomes rotten. We update the
                    # grid to mark it, preventing it from being added to the queue again.
                    grid[ni][nj] = 2
                    
                    # Line 15: queue.append([ni, nj, time + 1])
                    # Add the newly rotten orange to the queue. Its time is the current
                    # orange's time plus one minute.
                    queue.append([ni, nj, time + 1])

        # --- Phase 3: Final Validation ---
        # Line 16: for row in grid:
        # Line 17:     if 1 in row:
        # After the BFS is complete, iterate through the grid one last time
        # to see if any fresh oranges (1) are left.
        for row in grid:
            if 1 in row:
                # Line 18: return -1
                # If we find even one, it was unreachable. Return -1.
                return -1

        # Line 19: return ans
        # If no fresh oranges are left, return the final time recorded.
        return ans
```

-----

### Example Walkthrough

Let's trace the code with this grid: `grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]`

**Phase 1: Initialization**

  * The initial scan finds a rotten orange at `(0, 0)`.
  * **Initial `queue`**: `[[0, 0, 0]]`
  * **Initial `ans`**: `0`

#### Live Trace Table Map (BFS Traversal)

| Minute / Level | `queue` at start of minute                      | Processing `[i, j, time]` | Action: Neighbors that rot and get enqueued       | `grid` state after processing                                        | `ans` |
| :------------- | :---------------------------------------------- | :------------------------ | :------------------------------------------------ | :------------------------------------------------------------------- | :---- |
| **Minute 0** | `[[0, 0, 0]]`                                   | `[0, 0, 0]`               | `(0,1)` rots -\> enq `[0,1,1]`.\<br\>`(1,0)` rots -\> enq `[1,0,1]`. | `[[2,2,1],`\<br\>`[2,1,0],`\<br\>`[0,1,1]]`                                | 0     |
| **Minute 1** | `[[0, 1, 1], [1, 0, 1]]`                        | `[0, 1, 1]`               | `(0,2)` rots -\> enq `[0,2,2]`.\<br\>`(1,1)` rots -\> enq `[1,1,2]`. | `[[2,2,2],`\<br\>`[2,2,0],`\<br\>`[0,1,1]]`                                | 1     |
|                | `[[1, 0, 1], [0, 2, 2], [1, 1, 2]]`             | `[1, 0, 1]`               | Neighbor `(1,1)` is already `2`. No change.        | `[[2,2,2],`\<br\>`[2,2,0],`\<br\>`[0,1,1]]` (no change)                       | 1     |
| **Minute 2** | `[[0, 2, 2], [1, 1, 2]]`                        | `[0, 2, 2]`               | No fresh neighbors.                               | (no change)                                                          | 2     |
|                | `[[1, 1, 2]]`                                   | `[1, 1, 2]`               | `(2,1)` rots -\> enq `[2,1,3]`.                      | `[[2,2,2],`\<br\>`[2,2,0],`\<br\>`[0,2,1]]`                                | 2     |
| **Minute 3** | `[[2, 1, 3]]`                                   | `[2, 1, 3]`               | `(2,2)` rots -\> enq `[2,2,4]`.                      | `[[2,2,2],`\<br\>`[2,2,0],`\<br\>`[0,2,2]]`                                | 3     |
| **Minute 4** | `[[2, 2, 4]]`                                   | `[2, 2, 4]`               | No fresh neighbors.                               | (no change)                                                          | 4     |

The `while queue:` loop is now finished.

**Phase 3: Validation**

  * The code scans the final grid: `[[2,2,2], [2,2,0], [0,2,2]]`.
  * It finds no `1`'s.
  * **Line 19:** `return ans`

**Final Result:** `4`

-----

### Complexity Analysis

  * **Time Complexity:** $O(M \\times N)$, where `M` is the number of rows and `N` is the number of columns.
      * The initial scan to find rotten oranges takes $O(M \\times N)$.
      * The BFS process ensures that each cell is enqueued and dequeued at most once. For each cell, we do a constant amount of work (checking 4 neighbors). This also takes $O(M \\times N)$.
      * The final scan for leftover fresh oranges takes $O(M \\times N)$.
      * Overall, the complexity is linear in the number of cells.
  * **Space Complexity:** $O(M \\times N)$.
      * In the worst-case scenario, the `queue` could hold all the oranges in the grid (e.g., a grid full of rotten oranges), so the space required is proportional to the number of cells.