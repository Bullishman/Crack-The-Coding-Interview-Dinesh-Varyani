# 133. 3sum Closest

**Difficulty**: Medium

**Topics**: Array, Two Pointers, Sorting

**Link**: https://leetcode.com/problems/3sum-closest

Of course. Let's do a detailed line-by-line walkthrough of the `threeSumClosest` code.

### The Logic: Two-Pointer Approach

This algorithm is a classic and efficient solution for "3Sum" style problems. The core strategy is:

1.  **Sort:** First, sort the input array. This is the most critical step, as it allows us to use the two-pointer technique.
2.  **Iterate and Fix:** Iterate through the sorted array with a primary loop, fixing one number (`nums[i]`) at a time.
3.  **Two-Pointer Search:** For each fixed `nums[i]`, use two pointers, `l` (left) and `r` (right), to scan the rest of the array. `l` starts just after `i`, and `r` starts at the very end.
4.  **Converge and Update:** Move the `l` and `r` pointers towards each other based on whether their sum is too small or too large, continuously updating the closest sum found so far.

### The Example

Let's trace the execution with a standard example:

  * `nums = [-1, 2, 1, -4]`
  * `target = 1`

The expected output is `2`, because the sum `(-1 + 2 + 1 = 2)` has a difference of `abs(1 - 2) = 1` from the target, which is the smallest possible difference.

-----

### Code and Live Demonstration

#### 1\. Setup and Sorting

```python
        n = len(nums)
        # n = 4
        nums.sort()
        # nums is now [-4, -1, 1, 2]
        ans = float('inf')
        # ans is initialized to infinity
```

  * We sort the array to enable the two-pointer approach.
  * `ans` is initialized to infinity. The first valid sum we calculate will always be "closer" to the target than infinity, so this gives us a starting point for our comparisons.

#### 2\. The Main Loop (`for i...`)

```python
        for i in range(n-1):
```

  * This loop will iterate with `i` taking values `0`, `1`, and `2`. It fixes the first number of our potential triplet.

-----

### **Live Trace Table Map**

This table will track the state of all important variables during the execution.

| `i` | `nums[i]` | `l` | `r` | `nums[l]` | `nums[r]` | `temp_sum` | `abs(target-ans)` | `abs(target-temp_sum)` | `ans` (Best Sum) | Action on Pointers |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | - | - | - | - | - | - | `inf` | - | `inf` | - |
| **0** | **-4** | 1 | 3 | -1 | 2 | `-4 + -1 + 2 = -3` | `inf` | `abs(1 - (-3)) = 4` | **-3** | `sum < target` -\> `l++` |
| | | 2 | 3 | 1 | 2 | `-4 + 1 + 2 = -1` | `abs(1 - (-3)) = 4` | `abs(1 - (-1)) = 2` | **-1** | `sum < target` -\> `l++` |
| | | 3 | 3 | - | - | (loop ends `l < r` is false) | | | | |
| **1** | **-1** | 2 | 3 | 1 | 2 | `-1 + 1 + 2 = 2` | `abs(1 - (-1)) = 2` | `abs(1 - 2) = 1` | **2** | `sum > target` -\> `r--` |
| | | 2 | 2 | - | - | (loop ends `l < r` is false) | | | | |
| **2** | **1** | 3 | 3 | - | - | (loop ends `l < r` is false) | | | | |

-----

### **Detailed Line-by-Line Breakdown**

#### Outer Loop: `i = 0` (`nums[i] = -4`)

  * `l, r` are initialized to `1` and `3`.
  * **Inner loop 1:**
      * `l=1`, `r=3`. `nums[l]=-1`, `nums[r]=2`.
      * `temp_sum = -4 + (-1) + 2 = -3`.
      * `temp_sum` is not the target.
      * `temp_sum < target` (`-3 < 1`), so we need a larger sum. We move the left pointer: `l += 1`.
      * **Update `ans`**: Is `temp_sum` closer than `ans`? `abs(1 - (-3)) = 4`. `abs(1 - inf) = inf`. `4 < inf`, so `ans` becomes `-3`.
  * **Inner loop 2:**
      * `l=2`, `r=3`. `nums[l]=1`, `nums[r]=2`.
      * `temp_sum = -4 + 1 + 2 = -1`.
      * `temp_sum < target` (`-1 < 1`), so we need a larger sum. `l += 1`.
      * **Update `ans`**: Is `temp_sum` closer? `abs(1 - (-1)) = 2`. `abs(1 - ans) = abs(1 - (-3)) = 4`. `2 < 4`, so `ans` becomes `-1`.
  * Now `l` is `3`, `r` is `3`. The `while l < r` condition is false. The inner loop finishes for `i=0`.

#### Outer Loop: `i = 1` (`nums[i] = -1`)

  * `l, r` are initialized to `2` and `3`.
  * **Inner loop 1:**
      * `l=2`, `r=3`. `nums[l]=1`, `nums[r]=2`.
      * `temp_sum = -1 + 1 + 2 = 2`.
      * `temp_sum > target` (`2 > 1`), so we need a smaller sum. We move the right pointer: `r -= 1`.
      * **Update `ans`**: Is `temp_sum` closer? `abs(1 - 2) = 1`. `abs(1 - ans) = abs(1 - (-1)) = 2`. `1 < 2`, so `ans` becomes `2`.
  * Now `l` is `2`, `r` is `2`. The `while l < r` condition is false. The inner loop finishes for `i=1`.

#### Outer Loop: `i = 2` (`nums[i] = 1`)

  * `l, r` are initialized to `3` and `3`.
  * The `while l < r` (`3 < 3`) condition is immediately false. This inner loop does not run.

-----

#### 3\. Final Return

```python
        return ans
```

  * The outer `for` loop has finished.
  * The final value stored in `ans` is `2`.
  * The function returns **2**.