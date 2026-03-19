# 21. Longest Increasing Subsequence

**Difficulty**: Medium

**Topics**: Array, Binary Search, Dynamic Programming

**Link**: https://leetcode.com/problems/longest-increasing-subsequence

This code uses a **greedy strategy with binary search** (Patience Sorting) to find the length of the Longest Increasing Subsequence. While the `arr` list doesn't always represent the actual subsequence itself, it maintains the smallest possible tail values for subsequences of various lengths, which is enough to determine the maximum length.

---

### Line-by-Line Explanation

| Line | Code | Explanation |
| --- | --- | --- |
| **1** | `arr = [nums.pop(0)]` | Initializes the tracking list `arr` with the first element of `nums`. `pop(0)` removes it from the input list. |
| **2** | `for num in nums:` | Iterates through the remaining elements in the `nums` list one by one. |
| **3** | `if num > arr[-1]:` | Checks if the current number is greater than the largest (last) number in our tracking list. |
| **4** | `arr.append(num)` | If it's larger, we've found a way to make a longer increasing subsequence, so we extend `arr`. |
| **5** | `else:` | If the current number is smaller than or equal to the last element of `arr`... |
| **6** | `idx = bisect_left(arr, num)` | Use binary search to find the index of the first element in `arr` that is  `num`. |
| **7** | `arr[idx] = num` | Replace the value at that index with `num`. This keeps our "tails" as small as possible. |
| **8** | `return len(arr)` | The length of `arr` represents the maximum length achieved. |

---

### Execution Trace Table

**Input:** `nums = [10, 9, 2, 5, 3, 7, 101, 18]`

| Step | `num` (Current) | Comparison | Action | `arr` State (Tails) | LIS Length |
| --- | --- | --- | --- | --- | --- |
| **0** | - | Initializing | `pop(0)` | `[10]` | 1 |
| **1** | **9** | `9 < 10` | Replace `10` | `[9]` | 1 |
| **2** | **2** | `2 < 9` | Replace `9` | `[2]` | 1 |
| **3** | **5** | `5 > 2` | Append `5` | `[2, 5]` | 2 |
| **4** | **3** | `3 < 5` | Replace `5` (idx 1) | `[2, 3]` | 2 |
| **5** | **7** | `7 > 3` | Append `7` | `[2, 3, 7]` | 3 |
| **6** | **101** | `101 > 7` | Append `101` | `[2, 3, 7, 101]` | 4 |
| **7** | **18** | `18 < 101` | Replace `101` (idx 3) | `[2, 3, 7, 18]` | 4 |

**Final Output:** `4`

---

### Key Takeaway

Replacing an element (e.g., replacing `101` with `18`) doesn't increase the length of the LIS immediately, but it makes the list "better" for the future. A `18` is much more likely to be followed by another increasing number than `101` is. This greedy approach ensures we always have the best chance to extend the sequence.

Would you like to see how this logic changes if we wanted to find the **Longest Non-Decreasing Subsequence** instead?