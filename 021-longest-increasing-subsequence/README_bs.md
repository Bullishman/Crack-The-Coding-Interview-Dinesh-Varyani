# 21. Longest Increasing Subsequence

**Difficulty**: Medium

**Topics**: Array, Binary Search, Dynamic Programming

**Link**: https://leetcode.com/problems/longest-increasing-subsequence

This code implements a highly efficient algorithm for finding the length of the **Longest Increasing Subsequence (LIS)**. It uses a technique often called "Patience Sorting," which runs in  time.

The core idea is to maintain a list `res` that stores the smallest possible tail for all increasing subsequences of a given length.

---

## Line-by-Line Breakdown

### 1. Function Definition

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

```

* **`res = []`**: This list stores the "active" increasing subsequence. However, it’s important to note that `res` might not be *the* actual LIS, but its **length** will always match the length of the LIS.

### 2. The Binary Search Helper

This nested function finds the correct index to place or replace a number in the `res` list.

```python
        def binary_search(res, n):
            left, right = 0, len(res) - 1

            while left <= right:
                mid = (left + right) // 2
                if res[mid] == n:
                    return mid  # Found the exact number, return its index
                elif res[mid] > n:
                    right = mid - 1 # Look in the left half
                else:
                    left = mid + 1  # Look in the right half
            
            return left # Returns the insertion point (bisect_left)

```

* **Goal**: If `n` exists in `res`, return its position. If not, return the index where `n` *should* be placed to maintain sorted order.

### 3. The Main Loop

This is where we process each number in the input list.

```python
        for num in nums:
            if not res or res[-1] < num:
                res.append(num)

```

* **`if not res or res[-1] < num`**: If `res` is empty, or if the current number `num` is larger than the largest element currently in `res`, we simply append it. This effectively "extends" the longest subsequence found so far.

```python
            else:
                idx = binary_search(res, num)
                res[idx] = num

```

* **`else`**: If `num` is smaller than or equal to the last element, we find its place in `res` using binary search.
* **`res[idx] = num`**: We replace the element at `idx` with `num`. By replacing a larger value with a smaller one, we increase the chances of extending the subsequence later (because a smaller tail is easier to beat).

### 4. Return the Result

```python
        return len(res)

```

* The length of the `res` list represents the maximum length of an increasing subsequence encountered.

---

## Execution Trace

Let's trace the code with `nums = [10, 2, 5, 3, 7]`:

| Step | `num` | Action | `res` State | Reason |
| --- | --- | --- | --- | --- |
| 1 | 10 | Append | `[10]` | `res` was empty. |
| 2 | 2 | Replace | `[2]` | 2 is smaller than 10; replaces index 0. |
| 3 | 5 | Append | `[2, 5]` | 5 is greater than 2. |
| 4 | 3 | Replace | `[2, 3]` | 3 is smaller than 5; replaces 5 at index 1. |
| 5 | 7 | Append | `[2, 3, 7]` | 7 is greater than 3. |

**Final Length: 3**

Would you like me to show how this compares to the  Dynamic Programming approach?