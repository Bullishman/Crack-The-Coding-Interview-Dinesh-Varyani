# 135. Find Peak Element

**Difficulty**: Medium

**Topics**: Array, Binary Search

**Link**: https://leetcode.com/problems/find-peak-element

Of course. Let's do a detailed, line-by-line demonstration of this binary search algorithm for finding a peak element.

### The Logic: Binary Search on a Slope

This code uses a modified binary search to efficiently find a peak. A peak is defined as an element that is strictly greater than its immediate neighbors. The key insight is that by looking at the middle element (`m`) and its neighbors, we can determine if we are on an "uphill" or "downhill" slope, which tells us which half of the array is guaranteed to contain a peak.

1.  **Check for a Peak**: If `nums[m]` is greater than both `nums[m-1]` and `nums[m+1]`, we've found a peak and can return its index.
2.  **Check the Downhill Slope**: If `nums[m-1] > nums[m]`, it means we are on a "downhill" slope to the right. A peak *must* exist to the left of `m` (since the element at `m-1` is higher). So, we discard the right half by setting `r = m - 1`.
3.  **Check the Uphill Slope**: If neither of the above is true, it implies `nums[m+1] > nums[m]`. This means we are on an "uphill" slope to the right. A peak *must* exist to the right of `m`. So, we discard the left half by setting `l = m + 1`.

The code cleverly adds `float('-inf')` to the end to handle edge cases where the peak is the last element, ensuring `nums[m+1]` doesn't go out of bounds and is always smaller.

### The Example

Let's trace the execution with the following array:

  * `nums = [1, 2, 1, 3, 5, 6, 4]`

This array has two peaks: `2` (at index 1) and `6` (at index 5). The algorithm is guaranteed to find one of them. Let's see which one it finds and how.

-----

### Code and Live Demonstration

#### 1\. Setup

```python
        l, r = 0, len(nums) - 1
        # l = 0, r = 6
        nums.append(float('-inf'))
        # nums is now [1, 2, 1, 3, 5, 6, 4, -inf]
```

  * We initialize `l` (left) and `r` (right) pointers to the start and end of the original array.
  * We append negative infinity. This simplifies the logic inside the loop, especially when `m` points to the last element of the original array. For example, if `m` is `6` (the index of `4`), the check `nums[m+1] < nums[m]` becomes `nums[7] < nums[6]` (`-inf < 4`), which is true.

#### 2\. The Main Loop (`while l <= r`)

This is the binary search. It will continue as long as our search space is valid.

-----

### **Live Trace Table Map**

This table will track the state of the pointers and the logic at each step.

| Iteration | `l` | `r` | `m` Calculation | `m` | `nums[m]` | Condition Check | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | 0 | 6 | - | - | - | - | - |
| **1** | 0 | 6 | `0 + (6 - 0) // 2` | **3** | 3 | `nums[2] > nums[3]`? (`1 > 3` is False) | `else` -\> `l = m + 1` |
| **2** | 4 | 6 | `4 + (6 - 4) // 2` | **5** | 6 | `nums[4]<nums[5]` AND `nums[6]<nums[5]`? (`5<6` AND `4<6`) | **Peak Found\!** |
| **3** | 4 | 6 | - | - | - | - | `return m` |

-----

### **Detailed Line-by-Line Breakdown**

#### Iteration 1

  * **Pointers**: `l = 0`, `r = 6`. The search space is the entire array `[1, 2, 1, 3, 5, 6, 4]`.
  * `m = 0 + (6 - 0) // 2` -\> `m` becomes **3**.
  * We are now examining `nums[3]`, which is `3`.
  * **`if` condition**: `nums[m-1] < nums[m]` AND `nums[m+1] < nums[m]`?
      * `nums[2] < nums[3]`? (`1 < 3` is True).
      * `nums[4] < nums[3]`? (`5 < 3` is **False**).
      * The `if` block is skipped.
  * **`elif` condition**: `nums[m-1] > nums[m]`?
      * `nums[2] > nums[3]`? (`1 > 3` is **False**).
      * The `elif` block is skipped.
  * **`else` block**:
      * This block executes. It implies we are on an uphill slope to the right (`nums[m] < nums[m+1]`).
      * We know a peak must be to the right of `m`.
      * We discard the left half by updating the left pointer: `l = m + 1` -\> `l` becomes **4**.

#### Iteration 2

  * **Pointers**: `l = 4`, `r = 6`. The search space has been narrowed to `[5, 6, 4]`.
  * `m = 4 + (6 - 4) // 2` -\> `m` becomes **5**.
  * We are now examining `nums[5]`, which is `6`.
  * **`if` condition**: `nums[m-1] < nums[m]` AND `nums[m+1] < nums[m]`?
      * `nums[4] < nums[5]`? (`5 < 6` is **True**).
      * `nums[6] < nums[5]`? (`4 < 6` is **True**).
      * Both conditions are **True**. We have found a peak\!
  * The code enters the `if` block.

#### 3\. Final Return

```python
        return m
```

  * The function immediately returns the current value of `m`, which is **5**.
  * This is the index of the peak element `6`, which is a valid answer.