# 32. Permutations

**Difficulty**: Medium

**Topics**: Array, Backtracking

**Link**: https://leetcode.com/problems/permutations

This code generates all possible **permutations** of a list of numbers using **recursion (Depth-First Search)**. The core idea is to pick a number, remove it from the available pool, add it to your current chain, and repeat until no numbers are left.

### Line-by-Line Breakdown

#### The Setup (`permute` function)

```python
def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []
```

* **Initialize Result:** We create an empty list `ans` to store our final list of permutations (e.g., `[[1,2], [2,1]]`).

```python
    self.dfs(nums, [], ans)
    return ans
```

* **Kickoff:** We call the helper function `dfs`.
* `nums`: The pool of available numbers (initially full).
* `[]`: The current path/permutation we are building (initially empty).
* `ans`: The reference to the result list to store completed paths.


* **Return:** Once `dfs` finishes exploring all paths, we return the filled `ans`.

#### The Recursive Engine (`dfs` function)

```python
def dfs(self, nums, temp_nums, ans):
    if not nums:
        ans.append(temp_nums)
        return
```

* **Base Case:** If `nums` is empty (meaning we've used up all available numbers), we have a complete permutation.
* **Action:** We append the current path (`temp_nums`) to our final answer list `ans`.
* **Return:** We stop this branch of recursion and go back up.

```python
    for i in range(len(nums)):
```

* **Branching:** We loop through the currently available numbers. Each iteration represents a decision: "What if I pick the number at index `i` next?"

```python
        self.dfs(nums[:i] + nums[i + 1:], temp_nums + [nums[i]], ans)
```

* **The Recursive Leap:** This line does three critical things at once to set up the *next* step:
1. **Remove the chosen number:** `nums[:i] + nums[i + 1:]` creates a *new* list that excludes the number at index `i`. This becomes the new "available pool."
2. **Add to path:** `temp_nums + [nums[i]]` creates a *new* list with the chosen number added to the end.
3. **Recurse:** It calls `dfs` again with these updated lists.



---

### Step-by-Step Execution Map

**Input:** `nums = [1, 2, 3]`

We will track the "State" as `(Available Numbers, Current Path)`.

| Step | Action / Decision | `nums` (Available) | `temp_nums` (Current Path) | Note |
| --- | --- | --- | --- | --- |
| **1** | **Initial Call** | `[1, 2, 3]` | `[]` | Start DFS |
| **2** | Loop `i=0` (Pick 1) | `[2, 3]` | `[1]` | Recurse |
| **3** |   Loop `i=0` (Pick 2) | `[3]` | `[1, 2]` | Recurse |
| **4** |     Loop `i=0` (Pick 3) | `[]` | `[1, 2, 3]` | Recurse |
| **5** |     **Base Case** | `[]` | `[1, 2, 3]` | **Add to `ans**`, Return |
| **6** |   Loop `i=1` (Pick 3) | `[2]` | `[1, 3]` | Back in Step 2 context |
| **7** |     Loop `i=0` (Pick 2) | `[]` | `[1, 3, 2]` | Recurse |
| **8** |     **Base Case** | `[]` | `[1, 3, 2]` | **Add to `ans**`, Return |
| **9** | Loop `i=1` (Pick 2) | `[1, 3]` | `[2]` | Back in Step 1 context |
| **10** |   Loop `i=0` (Pick 1) | `[3]` | `[2, 1]` | Recurse |
| **11** |     Loop `i=0` (Pick 3) | `[]` | `[2, 1, 3]` | Recurse |
| **12** |     **Base Case** | `[]` | `[2, 1, 3]` | **Add to `ans**`, Return |

*(The process continues similarly for the branch starting with 3)*

### Visualizing the Data Flow

The most important part to understand is how the arguments change in the recursive call:

If `nums` is `[1, 2, 3]` and `i = 1` (we pick "2"):

1. **New Nums:** `nums[:1]` is `[1]`. `nums[2:]` is `[3]`.
* Result: `[1, 3]` (2 is removed).


2. **New Path:** `temp_nums` was `[]`. `[nums[1]]` is `[2]`.
* Result: `[2]` (2 is added).



This ensures that deeper levels of the recursion never see the numbers we have already used in the current path.