# 23. Maximum Product Subarray

**Difficulty**: Medium

**Topics**: Array, Dynamic Programming

**Link**: https://leetcode.com/problems/maximum-product-subarray

This code solves the **Maximum Product Subarray** problem using Dynamic Programming. The primary challenge of this problem is that a negative number can turn a very small negative product into a very large positive product. To handle this, the code tracks both the **maximum** and **minimum** products at each step.

---

### Line-by-Line Breakdown

| Line | Code | Explanation |
| --- | --- | --- |
| **1** | `if not nums: return 0` | **Edge Case:** If the input list is empty, return 0. |
| **2** | `min_num, max_num, res = nums[0], nums[0], nums[0]` | **Initialization:** We start by assuming the first number is our current minimum, maximum, and overall result. |
| **3** | `for i in range(1, len(nums)):` | **Iteration:** Start a loop from the second element (index 1) to the end of the list. |
| **4** | `num = nums[i]` | **Current Value:** Store the current element in a variable `num` for easier access. |
| **5** | `min_num *= num` | Temporarily multiply the current `min_num` by the current `num`. |
| **6** | `max_num *= num` | Temporarily multiply the current `max_num` by the current `num`. |
| **7** | `min_num, max_num = min(...), max(...)` | **The Core Logic:** We update `min_num` and `max_num` by comparing three values: the multiplied min, the multiplied max, and the current `num` itself. This handles signs flipping (negative  negative) and allows us to "restart" the subarray at the current number. |
| **8** | `res = max(res, max_num)` | **Update Result:** Update the global maximum product found so far. |
| **9** | `return res` | **Final Output:** Return the highest product product found across all subarrays. |

---

### Execution Trace Table

**Input:** `nums = [2, 3, -2, 4]`

| Step | `num` | `min_num` (before update) | `max_num` (before update) | `min_num` (after line 7) | `max_num` (after line 7) | `res` |
| --- | --- | --- | --- | --- | --- | --- |
| **Init** | - | - | - | 2 | 2 | 2 |
| **1** | **3** |  |  |  |  | **6** |
| **2** | **-2** |  |  |  |  | **6** |
| **3** | **4** |  |  |  |  | **6** |

**Final Result:** `6`

---

### Why do we need `min_num`?

Imagine the input is `[-2, 3, -4]`:

1. At `-2`: `min` is -2, `max` is -2.
2. At `3`: `min` becomes -6, `max` becomes 3.
3. At `-4`:
* `min_num * num` becomes .
* `max_num * num` becomes .
* The new `max_num` becomes **24**.



Without tracking the minimum, we would have "lost" the potential of that large positive product hidden behind two negative numbers.

Would you like me to explain how to modify this code to also return the actual subarray that produces the maximum product?