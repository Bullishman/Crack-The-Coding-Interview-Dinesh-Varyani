# 177. Permutations II

**Difficulty**: Medium

**Topics**: Array, Backtracking

**Link**: https://leetcode.com/problems/permutations-ii

This problem can be solved using an elegant **Backtracking with a Hash Map (Counter)** approach.

### The Core Idea

The goal is to find all possible unique permutations of an array that may contain duplicates. 

To ensure we don't generate duplicate permutations, we track the *frequency* or *available count* of each unique number using a hash map (or Counter). Every time we build our path recursively, we iterate only over the **unique numbers**. If a number is still available (count > 0), we use it, decrement its count, recurse, and then restore its count when backtracking. 

Because we iterate over distinct unique numbers at each step, we fundamentally cannot produce identical branches at the same position, preventing duplicate permutations natively.

Let's break down the code line by line with an example.

**Example:** `nums = [1, 1, 2]`
**Expected Result:** `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`

-----

### **Initial Setup**

```python
from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
```

This imports `Counter` and defines the main class and function.

```python
        res = []
        path = []
        count = Counter(nums)
```

  * **What it does:** This initializes the state.
      * `res = []`: The list that will store all our valid unique permutations.
      * `path = []`: The current branch/permutation we are building.
      * `count = Counter(nums)`: A hash map that calculates the frequency of each number. For `[1, 1, 2]`, it gives `{1: 2, 2: 1}`.

-----

### **The Backtracking Function**

```python
        def backtrack():
```

  * **What it does:** This is the recursive helper function that builds the permutations locally.

#### **Base Case**

```python
            if len(path) == len(nums):
                res.append(path.copy())
                return
```

  * **What it does:** If the current `path` length equals the original array length, we have successfully built a full permutation. We append a copy of it to `res` and return to backtrack. 

#### **Inside the Loop: Recursion and Pruning**

```python
            for num in count:
                if count[num] > 0:
```

  * **What it does:** We iterate through every *unique* number in our frequency map. If the number's count is greater than zero, it means we can still add it to our current branch.

```python
                    path.append(num)
                    count[num] -= 1
                    
                    backtrack()
                    
                    path.pop()
                    count[num] += 1
```

  * **This is the recursive backtracking step.**
    *   We add `num` to our `path` and decrement its available `count`.
    *   `backtrack()`: We recursively explore all deeper paths starting with this state.
    *   `path.pop()` & `count[num] += 1`: Once the recursion returns, we undo our choices to backtrack and try placing the next available unique number in this slot.

-----

### **Final Return**

```python
        backtrack()
        return res
```

  * We trigger the recursion by calling `backtrack()`. When it finishes, `res` will hold all unique permutations. The function returns this value.

-----

### **Live Trace Table Map**

**`nums` = `[1, 1, 2]`** -> `count` = `{1: 2, 2: 1}`

| Step | `num` (Choice) | `count` map State | Current `path` length | Action | `path` |
|:---:|:---:|:---|:---:|:---|:---|
| 1 | `1` | `{1: 2, 2: 1}` | 0 | Use `1`. Decrement count. Call `backtrack()` | `[1]` |
| 2 | `1` | `{1: 1, 2: 1}` | 1 | Use `1`. Decrement count. Call `backtrack()` | `[1, 1]` |
| 3 | `1` | `{1: 0, 2: 1}` | 2 | `count[1]` is 0. **Skip.** | `[1, 1]` |
| 4 | `2` | `{1: 0, 2: 1}` | 2 | Use `2`. Decrement count. Path full. **Append `[1, 1, 2]`** | `[1, 1, 2]` |
| 5 | backtrack | `{1: 0, 2: 0}` -> `{1: 0, 2: 1}`| 2 | Undoes `2`, returns to step 2 loop | `[1, 1]` |
| 6 | backtrack | `{1: 0, 2: 1}` -> `{1: 1, 2: 1}`| 1 | Undoes `1`, returns to step 1 loop | `[1]` |
| 7 | `2` | `{1: 1, 2: 1}` | 1 | Use `2`. Decrement count. Call `backtrack()`| `[1, 2]` |
| 8 | `1` | `{1: 1, 2: 0}` | 2 | Use `1`. Decrement count. Path full. **Append `[1, 2, 1]`**| `[1, 2, 1]` |
| 9 | backtrack | `{1: 1, 2: 1}` -> `{1: 2, 2: 1}`| 0 | Undoes `1` completely! | `[]` |
| 10 | `2` | `{1: 2, 2: 1}` | 0 | Use `2`. Decrement count. Call `backtrack()`| `[2]` |
| 11 | `1` | `{1: 2, 2: 0}` | 1 | Use `1`. Decrement count. Call `backtrack()`| `[2, 1]` |
| 12 | `1` | `{1: 1, 2: 0}` | 2 | Use `1`. Decrement count. Path full. **Append `[2, 1, 1]`**| `[2, 1, 1]` |

The function returns the final list containing the 3 unique valid arrays.
