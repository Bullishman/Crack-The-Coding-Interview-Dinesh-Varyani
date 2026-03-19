# 33. Combination Sum

**Difficulty**: Medium

**Topics**: Array, Backtracking

**Link**: https://leetcode.com/problems/combination-sum

I love the tabular format! It is a fantastic way to visualize state changes in algorithms.

This code is a classic implementation of a **Backtracking algorithm** (using Depth-First Search) to solve the "Combination Sum" problem. Here is the line-by-line breakdown, followed by a step-by-step execution map styled like your table.

### Line-by-Line Breakdown

* **`class Solution:`** Standard object-oriented wrapper class, typical for coding platforms like LeetCode.
* **`def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:`** The main function. It takes the pool of numbers (`candidates`) and the `target` sum, returning a list of valid combinations.
* **`results = []`** Initializes an empty list to store all the successful combinations we find.
* **`def dfs(csum, index, path):`** Defines an inner helper function to perform the recursion.
* `csum` tracks the *remaining* sum needed to hit the target.
* `index` keeps track of where we are in the `candidates` array. We pass this forward to prevent duplicate combinations (e.g., finding `[2, 3]` and preventing a later `[3, 2]`).
* `path` is the current sequence of numbers we have chosen in this specific recursive branch.


* **`if csum < 0:`** **Base Case 1 (Overshoot):** If the remaining sum drops below zero, our current `path` has added up to a number greater than the target.
* **`return`** Stops this recursive branch. It "backtracks" to the previous state to try a different loop iteration.
* **`if csum == 0:`** **Base Case 2 (Success):** If the remaining sum is exactly zero, we have successfully found a combination!
* **`results.append(path)`** Adds the successful combination (`path`) to our `results` list.
* **`return`** Stops exploring this branch further, as adding any more numbers would exceed the target.
* **`for i in range(index, len(candidates)):`** Iterates through the `candidates`. Starting from `index` (instead of `0`) ensures we only look at the current number or numbers *after* it, which is how the algorithm avoids building duplicate sets.
* **`dfs(csum - candidates[i], i, path + [candidates[i]])`** The core recursive call:
* `csum - candidates[i]`: Subtracts the chosen number from the remaining target.
* `i`: Passes the *same* index we are currently on. This allows the algorithm to reuse the same number an unlimited number of times.
* `path + [candidates[i]]`: Creates a *brand new list* by taking the current sequence and adding the new number. Because we create a new list in memory here, we don't need a `path.pop()` statement later to clean up the state.


* **`dfs(target, 0, [])`** The initial trigger for the recursion. We start with the full `target`, at index `0`, with an empty sequence `[]`.
* **`return results`** Once all recursive branches finish, this returns the fully populated list of combinations.

---

### Step-by-Step Execution Map

To see exactly how the variables mutate, let's run a trace using a simple example:
**Input:** `candidates = [2, 3]`, `target = 5`

| Current State `dfs(csum, index, path)` | Loop `i` | `candidate` | Base Case Check | Action / Next Step |
| --- | --- | --- | --- | --- |
| `dfs(5, 0, [])` | 0 | 2 | None | Recurse: `dfs(3, 0, [2])` |
| `dfs(3, 0, [2])` | 0 | 2 | None | Recurse: `dfs(1, 0, [2, 2])` |
| `dfs(1, 0, [2, 2])` | 0 | 2 | None | Recurse: `dfs(-1, 0, [2, 2, 2])` |
| `dfs(-1, 0, [2, 2, 2])` | - | - | **`csum < 0`** | **Return (Backtrack)** |
| `dfs(1, 0, [2, 2])` | 1 | 3 | None | Recurse: `dfs(-2, 1, [2, 2, 3])` |
| `dfs(-2, 1, [2, 2, 3])` | - | - | **`csum < 0`** | **Return (Backtrack)** |
| `dfs(3, 0, [2])` | 1 | 3 | None | Recurse: `dfs(0, 1, [2, 3])` |
| `dfs(0, 1, [2, 3])` | - | - | **`csum == 0`** | **Save `[2, 3]`, Return** |
| `dfs(5, 0, [])` | 1 | 3 | None | Recurse: `dfs(2, 1, [3])` |
| `dfs(2, 1, [3])` | 1 | 3 | None | Recurse: `dfs(-1, 1, [3, 3])` |
| `dfs(-1, 1, [3, 3])` | - | - | **`csum < 0`** | **Return (Backtrack)** |
| *(Execution Finishes)* | - | - | All loops done | **Return `[[2, 3]]**` |

---

Using `path + [candidates[i]]` is clean and easy to read, but creating a new list on every single recursive call uses a lot of extra memory under the hood.

Would you like me to show you the slightly optimized version of this code that uses `.append()` and `.pop()` to reuse the same list in memory?