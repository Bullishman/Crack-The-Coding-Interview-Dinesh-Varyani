# 179. Combination Sum II

**Difficulty**: Medium

**Topics**: Array, Backtracking

**Link**: https://leetcode.com/problems/combination-sum-ii

This problem can be solved using an elegant **Backtracking with Sorting and Pruning** approach.

### The Core Idea

The goal is to find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number can be used at most once, and the solution set must not contain duplicate combinations.

To ensure we don't generate duplicate combinations, we first **sort** the candidates array. This naturally groups identical numbers together. During backtracking, at any given depth of our recursion tree, if we encounter a number that is identical to the previous one we just considered (at the same level), we **skip** it. 

Sorting also gives us a massive performance boost via pruning: if the current candidate exceeds the remaining target, we can instantly `break` out of the loop because all subsequent elements will also exceed the target.

Let's break down the code line by line with an example.

**Example:** `candidates = [10, 1, 2, 7, 6, 1, 5]`, `target = 8`
**Sorted:** `[1, 1, 2, 5, 6, 7, 10]`
**Expected Result:** `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]`

-----

### **Initial Setup**

```python
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
```

  * **What it does:** This initializes our state.
      * `candidates.sort()`: We sort the list in-place so identical elements are adjacent.
      * `res = []`: The list that will store all our valid unique combinations.

-----

### **The Backtracking Function**

```python
        def backtrack(start, target_rem, path):
```

  * **What it does:** This is the recursive helper function that builds the combinations.
      * `start`: Tracks the starting index for the current recursive call to avoid using elements backward.
      * `target_rem`: The remaining sum needed to hit our `target`.
      * `path`: The current branch/combination we are building.

#### **Base Cases**

```python
            if target_rem == 0:
                res.append(list(path))
                return
            if target_rem < 0:
                return
```

  * **What it does:** 
      * If `target_rem == 0`, we have successfully built a valid combination. We append a copy of `path` to `res` and return to backtrack.
      * If `target_rem < 0`, our subset sum has exceeded the target, so we return immediately (this is a fallback, though our pruning often prevents this).

#### **Inside the Loop: Recursion, Duplicate Skipping, and Pruning**

```python
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
```

  * **What it does:** We iterate through the available candidates starting from `start`. 
  * **Duplicate Skipping:** The condition `i > start` ensures we only skip duplicates at the *same* recursive depth. If `candidates[i]` is identical to the one right before it, we `continue` to avoid exploring identical branches.

```python
                if candidates[i] > target_rem:
                    break
```

  * **What it does:** **Pruning.** Because the array is sorted, if the current candidate is larger than `target_rem`, all subsequent candidates will also be too large. We can safely `break` the loop, saving massive amounts of computation.

```python
                path.append(candidates[i])
                backtrack(i + 1, target_rem - candidates[i], path)
                path.pop()
```

  * **This is the recursive backtracking step.**
    *   We add `candidates[i]` to our `path`.
    *   `backtrack()`: We recursively explore deeper, starting from `i + 1` (since elements can only be used once), and subtract the candidate from `target_rem`.
    *   `path.pop()`: Once the recursion returns, we undo our choice and backtrack to try the next available candidate.

-----

### **Final Return**

```python
        backtrack(0, target, [])
        return res
```

  * We trigger the recursion by calling `backtrack()` with index `0`, the full `target`, and an empty `path`. When finished, `res` will hold all unique combinations.

-----

### **Live Trace Table Map**

**`candidates` (sorted) = `[1, 1, 2, 5, 6, 7, 10]`**, **`target` = 8**

| Step | Depth | `start` | `i` | `candidates[i]` | `target_rem` | Action | `path` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 1 | 0 | 0 | 0 | `1` (1st) | `8` | Use `1` (1st). Call `backtrack()` | `[1]` |
| 2 | 1 | 1 | 1 | `1` (2nd) | `7` | Use `1` (2nd). Call `backtrack()` | `[1, 1]` |
| 3 | 2 | 2 | 2 | `2` | `6` | Use `2`. Call `backtrack()` | `[1, 1, 2]` |
| 4 | 3 | 3 | 3 | `5` | `4` | `5 > 4`. **Pruned (Loop breaks)** | `[1, 1, 2]` |
| 5 | 2 | 2 | backtrack | - | - | Undoes `2`, returns to step 3 loop | `[1, 1]` |
| 6 | 2 | 2 | 3 | `5` | `6` | Use `5`. Call `backtrack()` | `[1, 1, 5]` |
| 7 | 3 | 4 | 4 | `6` | `1` | `6 > 1`. **Pruned (Loop breaks)** | `[1, 1, 5]` |
| 8 | 2 | 2 | backtrack | - | - | Undoes `5`, returns to step 6 loop | `[1, 1]` |
| 9 | 2 | 2 | 4 | `6` | `6` | Use `6`. Call `backtrack()` | `[1, 1, 6]` |
| 10 | 3 | 5 | 5 | - | `0` | `target_rem` is 0. **Append `[1, 1, 6]`** | `[1, 1, 6]` |
| 11 | 2 | 2 | backtrack | - | - | Undoes `6`, returns to step 9 loop | `[1, 1]` |
| ... | ... | ... | ... | ... | ... | Backtracking continues... | ... |
| 20 | 0 | 0 | backtrack | - | - | Undoes `1` (1st) completely! | `[]` |
| 21 | 0 | 0 | 1 | `1` (2nd) | `8` | `i > start` (1 > 0) & `1 == 1`. **Skip.**| `[]` |
| 22 | 0 | 0 | 2 | `2` | `8` | Use `2`. Call `backtrack()` | `[2]` |

The function accurately skips the duplicate branches and only returns valid arrays.
