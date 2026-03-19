# 168. Surrounded Regions

**Difficulty**: Medium

**Topics**: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

**Link**: https://leetcode.com/problems/surrounded-regions

This code elegantly solves the classic **"Surrounded Regions"** problem using a **Reverse Thinking** pattern. Instead of trying to find the `'O'`s that are surrounded, it looks for the `'O'`s that are *safe* (connected to the borders) and marks them. Everything else gets captured!

Here is the line-by-line breakdown, followed by a live trace table mapping out the board's state changes.

### Line-by-Line Breakdown

* **`class Solution:`** The standard object-oriented wrapper class for LeetCode.
* **`def dfs(self, board: List[List[str]], row: int, col: int) -> None:`** A helper function that performs Depth-First Search (DFS) to find all `'O'`s connected to a specific cell.
* **`if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':`** The base case and boundary check all in one. It only proceeds if the `row` and `col` are within the board's limits AND the current cell is an `'O'`.
* **`board[row][col] = 'A'`** Temporarily changes the safe `'O'` to an `'A'` (for "Alive" or "Active"). This marks it so we don't process it again and saves it from being flipped later.
* **`self.dfs(board, row + 1, col)`** (and the next 3 lines): Recursively calls `dfs` on the 4 adjacent cells (Down, Up, Right, Left) to find connected `'O'`s and mark them as `'A'` as well.
* **`def solve(self, board: List[List[str]]) -> None:`** The main function that drives the logic. It modifies the board in-place.
* **`m, n = len(board), len(board[0])`** Stores the number of rows (`m`) and columns (`n`) for easy access.
* **`for i in range(m):`** Iterates through every row to check the left and right borders.
* **`self.dfs(board, i, 0)`** Triggers DFS on the first column (Left border).
* **`self.dfs(board, i, n - 1)`** Triggers DFS on the last column (Right border).
* **`for i in range(n):`** Iterates through every column to check the top and bottom borders.
* **`self.dfs(board, 0, i)`** Triggers DFS on the first row (Top border).
* **`self.dfs(board, m - 1, i)`** Triggers DFS on the last row (Bottom border).
* **`board[:] = [['XO'[col == 'A'] for col in row] for row in board]`** A brilliant, Pythonic one-liner to finalize the board. Let's break it down:
* It loops through every cell (`col`) in every `row`.
* **`col == 'A'`**: Evaluates to `True` (which Python treats as `1`) if the cell was marked safe, and `False` (`0`) if it's anything else (`'X'` or an surrounded `'O'`).
* **`'XO'[...]`**: Uses the `True/False` (1/0) as an index. If `1`, it pulls `'O'` (restoring the safe cell). If `0`, it pulls `'X'` (capturing the surrounded `'O'`s and leaving existing `'X'`s alone).
* **`board[:] = ...`**: Replaces the entire contents of the original board array in memory with the newly constructed list.



---

### Live Trace Table Map

Let's watch the board mutate using a 4x4 matrix.
**Input:**

```text
X X X X
X O O X
X X O X
X O X X

```

Notice there is a cluster of `'O'`s in the middle, and a single `'O'` on the bottom border.

| Phase | Step | Action | Resulting Board State | Notes |
| --- | --- | --- | --- | --- |
| **1. Left/Right Borders** | `i=0` to `3` | `dfs()` on cols 0 and 3. | *(No changes)* | No `'O'`s found on the far left or right edges. |
| **2. Top Border** | `i=0` to `3` | `dfs()` on row 0. | *(No changes)* | No `'O'`s found on the top edge. |
| **3. Bottom Border** | `i=1` | `dfs(3, 1)` finds an `'O'`! | `X X X X`<br> <br>`X O O X`<br> <br>`X X O X`<br> <br>`X `<strong style="color:blue">A</strong>` X X` | Bottom border `'O'` is marked `'A'`. |
| **3. Bottom DFS Extends** | Inside `dfs(3,1)` | Checks Up, Down, Left, Right | *(No changes)* | The surrounding cells are all `'X'` or out of bounds. Recursion stops. |
| **4. Final Flip** | `board[:] = ...` | Re-evaluates every cell. | `X X X X`<br> <br>`X `<strong style="color:red">X X</strong>` X`<br> <br>`X X `<strong style="color:red">X</strong>` X`<br> <br>`X `<strong style="color:blue">O</strong>` X X` | Middle `'O'`s were never marked `'A'`, so they become `'X'`. The `'A'` reverts to `'O'`. |

**Why did the middle `'O'`s turn into `'X'`s?**
Because the DFS only ever started from the outer edges. Since the middle `'O'`s weren't touching an edge (or touching another `'O'` that touched an edge), the DFS never reached them. They remained as `'O'` in step 3, and the final list comprehension replaced any cell that wasn't `'A'` with an `'X'`.

---

Would you like me to explain the Time and Space Complexity for this algorithm, or shall we explore how this differs from a standard BFS (Breadth-First Search) approach?