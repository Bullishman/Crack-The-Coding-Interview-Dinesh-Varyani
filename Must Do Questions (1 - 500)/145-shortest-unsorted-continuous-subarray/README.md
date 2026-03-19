# 145. Shortest Unsorted Continuous Subarray

**Difficulty**: Medium

**Topics**: Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack

**Link**: https://leetcode.com/problems/shortest-unsorted-continuous-subarray

You are absolutely right. The previous table was dense and hard to follow. My apologies\! A good demonstration should be easy to understand step-by-step.

Let's try a much clearer, more narrative approach. I'll break down each iteration of the loops, explaining the logic as we update the values.

### The Example

We will use the same array:

  * `nums = [2, 6, 4, 8, 10, 9, 15]`
  * **Goal:** Find the boundaries of the subarray `[6, 4, 8, 10, 9]`. The left boundary should be index `1` (`l=1`), and the right boundary should be index `5` (`r=5`).

-----

### Phase 1: Finding the Right Boundary `r` (Scanning Left-to-Right)

The goal of this pass is to find the index of the **last element** that is smaller than the maximum value seen so far on its left.

**Initialization:**

  * `r` starts at `-1` (meaning no unsorted section found yet).
  * `mx` starts at a very small number (`-1e6`) to ensure the first element is always larger.

**Live Trace: Finding `r`**

| `i` | `nums[i]` | `mx` (Max so far) | Logic: `nums[i] >= mx`? | Action | `r` |
| :-- | :--- | :--- | :--- | :--- | :--- |
| **0** | **2** | -1e6 | `2 >= -1e6` (True) | `mx` becomes **2** | -1 |
| **1** | **6** | 2 | `6 >= 2` (True) | `mx` becomes **6** | -1 |
| **2** | **4** | 6 | `4 >= 6` (**False**) | **`r` becomes `i`** | **2** |
| **3** | **8** | 6 | `8 >= 6` (True) | `mx` becomes **8** | 2 |
| **4** | **10**| 8 | `10 >= 8` (True) | `mx` becomes **10**| 2 |
| **5** | **9** | 10 | `9 >= 10` (**False**) | **`r` becomes `i`** | **5** |
| **6** | **15**| 10 | `15 >= 10` (True)| `mx` becomes **15**| 5 |

**Step-by-Step Explanation:**

  * **`i = 0, 1`**: The array is increasing (`2`, then `6`). We are just updating our running maximum `mx`. `r` is untouched.
  * **`i = 2` (Key Moment\!)**: We see `nums[2]` is `4`. The maximum we've seen so far is `6`. Since `4 < 6`, this element is "out of place." It's a dip after a peak. We record its index as our potential right boundary: **`r = 2`**.
  * **`i = 3, 4`**: The array is increasing again (`8`, `10`). We update `mx`, but `r` stays at `2`.
  * **`i = 5` (Key Moment\!)**: We see `nums[5]` is `9`. The maximum so far is `10`. Since `9 < 10`, this is another out-of-place element. Because its index (`5`) is further right than our current `r` (`2`), we **update `r = 5`**.
  * **`i = 6`**: The array increases again. `mx` is updated, but `r` is not.

At the end of this phase, we have found that the right boundary of the unsorted section is **`r = 5`**.

-----

### Phase 2: Finding the Left Boundary `l` (Scanning Right-to-Left)

Now we do the reverse. The goal is to find the index of the **first element** (from the left) that is larger than the minimum value seen so far on its right.

**Initialization:**

  * `l` starts at `n` (which is `7`).
  * `mn` starts at a very large number (`1e6`).

**Live Trace: Finding `l`**

| `i` | `nums[i]` | `mn` (Min so far) | Logic: `nums[i] <= mn`? | Action | `l` |
| :-- | :--- | :--- | :--- | :--- | :--- |
| **6** | **15**| 1e6 | `15 <= 1e6` (True) | `mn` becomes **15**| 7 |
| **5** | **9** | 15 | `9 <= 15` (True) | `mn` becomes **9** | 7 |
| **4** | **10**| 9 | `10 <= 9` (**False**) | **`l` becomes `i`** | **4** |
| **3** | **8** | 9 | `8 <= 9` (True) | `mn` becomes **8** | 4 |
| **2** | **4** | 8 | `4 <= 8` (True) | `mn` becomes **4** | 4 |
| **1** | **6** | 4 | `6 <= 4` (**False**) | **`l` becomes `i`** | **1** |
| **0** | **2** | 4 | `2 <= 4` (True) | `mn` becomes **2** | 1 |

**Step-by-Step Explanation:**

  * **`i = 6, 5`**: Scanning from the right, the numbers are decreasing (`15`, then `9`). We update our running minimum `mn`. `l` is untouched.
  * **`i = 4` (Key Moment\!)**: We see `nums[4]` is `10`. The minimum we've seen to the right is `9`. Since `10 > 9`, this element is out of place. It's a peak before a valley. We record its index as the potential left boundary: **`l = 4`**.
  * **`i = 3, 2`**: The numbers are decreasing again (`8`, `4`). We update `mn`, but `l` stays at `4`.
  * **`i = 1` (Key Moment\!)**: We see `nums[1]` is `6`. The minimum to its right is `4`. Since `6 > 4`, this is another out-of-place element. Because its index (`1`) is further left than our current `l` (`4`), we **update `l = 1`**.
  * **`i = 0`**: `2` is smaller than the minimum `4`, so we just update `mn`.

At the end of this phase, the left boundary of the unsorted section is **`l = 1`**.

-----

### Final Calculation

```python
return max(0, r - l + 1)
```

  * The code plugs in the final values: `r = 5` and `l = 1`.
  * Calculation: `max(0, 5 - 1 + 1)`
  * Result: `max(0, 5)`
  * The function returns **5**.