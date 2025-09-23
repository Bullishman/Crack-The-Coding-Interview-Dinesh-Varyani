# 115. Minimum Size Subarray Sum

**Difficulty**: Medium

**Topics**: Array, Binary Search, Sliding Window, Prefix Sum

**Link**: https://leetcode.com/problems/minimum-size-subarray-sum

Of course. Let's break down this Python code, which is a classic example of the **sliding window** technique.

### Algorithm Goal

The function `minSubArrayLen` aims to find the minimum length of a **contiguous subarray** whose elements sum up to be greater than or equal to a given `target`. If no such subarray exists, it should return 0.

The "sliding window" is a conceptual window formed over the array by two pointers, a left pointer (`l`) and a right pointer (`r`).

1.  The window **expands** by moving the right pointer (`r`) to the right.
2.  The window **shrinks** by moving the left pointer (`l`) to the right.

This technique allows us to efficiently check all possible contiguous subarrays without using nested loops, which would be much slower (O(n²)). The sliding window approach has a time complexity of O(n).

-----

### Line-by-Line Code Explanation

Here is a detailed breakdown of each line.

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
```

  * This defines the class `Solution` and the method `minSubArrayLen`.

<!-- end list -->

```python
        ans, l = 0, 0
```

  * **Purpose:** Initialize the core variables.
  * **`ans = 0`**: This variable will hold the running sum of the elements within the current sliding window. It's named `ans` here, but it's more of a `current_sum`.
  * **`l = 0`**: This initializes the left pointer (`l`) of our sliding window to the start of the array (index 0).

<!-- end list -->

```python
        size = float("inf")
```

  * **Purpose:** Initialize the variable that will store our final answer.
  * We initialize `size` to positive infinity (`float("inf")`) so that the very first valid subarray length we find will be smaller and will replace it. This is a common pattern for finding a minimum value.

<!-- end list -->

```python
        for r in range(len(nums)):
```

  * **Purpose:** This is the main loop that drives the window expansion.
  * The right pointer (`r`) iterates through the array from the first element (index 0) to the last. With each iteration, the window expands to the right to include `nums[r]`.

<!-- end list -->

```python
            ans += nums[r]
```

  * **Purpose:** As the window expands, add the value of the new element (`nums[r]`) to the running sum (`ans`).

<!-- end list -->

```python
            while ans >= target:
```

  * **Purpose:** This is the crucial part that shrinks the window.
  * Once the sum of our current window (`ans`) is greater than or equal to the `target`, we have found a valid subarray. Now, we must try to make this subarray as small as possible by shrinking it from the left. This `while` loop continues as long as the window's sum remains valid.

<!-- end list -->

```python
                size = min(size, r - l + 1)
```

  * **Purpose:** Update our minimum size.
  * The length of the current valid window is `r - l + 1`. We compare this length to our current minimum `size` and keep the smaller of the two.

<!-- end list -->

```python
                ans -= nums[l]
```

  * **Purpose:** To shrink the window from the left, we subtract the value of the leftmost element (`nums[l]`) from our running sum.

<!-- end list -->

```python
                l += 1
```

  * **Purpose:** We move the left pointer (`l`) one step to the right, completing the "shrink" operation. The `while` loop will then re-check if the new, smaller window still has a sum `>= target`.

<!-- end list -->

```python
        return size if size != float("inf") else 0
```

  * **Purpose:** Return the final result.
  * After the main `for` loop has finished, if `size` is still `float("inf")`, it means we never found a valid subarray that met the target sum. In this case, we return `0`.
  * Otherwise, we return the minimum `size` we found.

-----

### Live Trace Table Example

Let's trace the execution with `target = 7` and `nums = [2, 3, 1, 2, 4, 3]`.

**Initial State:** `l = 0`, `ans = 0`, `size = inf`

**Trace Map:**

| `r` | `nums[r]` | `ans` (after `+=`) | `ans >= 7`? | `while` loop actions | `l` | `size` | Window (`nums[l:r+1]`) |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- | :--- |
| 0 | 2 | 2 | `False` | - | 0 | `inf` | `[2]` |
| 1 | 3 | 5 | `False` | - | 0 | `inf` | `[2, 3]` |
| 2 | 1 | 6 | `False` | - | 0 | `inf` | `[2, 3, 1]` |
| 3 | 2 | 8 | **`True`** | `size=min(inf, 3-0+1=4)` -\> **4**\<br/\>`ans = 8 - nums[0](2)` -\> 6\<br/\>`l = 1` | 1 | 4 | `[2, 3, 1, 2]` |
| | | 6 | `False` | Loop ends. | 1 | 4 | `[3, 1, 2]` |
| 4 | 4 | 10 | **`True`** | `size=min(4, 4-1+1=4)` -\> **4**\<br/\>`ans = 10 - nums[1](3)` -\> 7\<br/\>`l = 2` | 2 | 4 | `[3, 1, 2, 4]` |
| | | 7 | **`True`** | `size=min(4, 4-2+1=3)` -\> **3**\<br/\>`ans = 7 - nums[2](1)` -\> 6\<br/\>`l = 3` | 3 | 3 | `[1, 2, 4]` |
| | | 6 | `False` | Loop ends. | 3 | 3 | `[2, 4]` |
| 5 | 3 | 9 | **`True`** | `size=min(3, 5-3+1=3)` -\> **3**\<br/\>`ans = 9 - nums[3](2)` -\> 7\<br/\>`l = 4` | 4 | 3 | `[2, 4, 3]` |
| | | 7 | **`True`** | `size=min(3, 5-4+1=2)` -\> **2**\<br/\>`ans = 7 - nums[4](4)` -\> 3\<br/\>`l = 5` | 5 | 2 | `[4, 3]` |
| | | 3 | `False` | Loop ends. | 5 | 2 | `[3]` |

**Final Step:**

1.  The `for` loop finishes.
2.  The final value of `size` is `2`.
3.  The function checks `if size != float("inf")`. This is `True` (`2 != inf`).
4.  It returns `size`, which is **2**.