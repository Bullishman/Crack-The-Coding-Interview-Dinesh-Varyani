# 28. Jump Game

**Difficulty**: Medium

**Topics**: Array, Dynamic Programming, Greedy

**Link**: https://leetcode.com/problems/jump-game

This code solves the **Jump Game** problem using a **Greedy** approach. The goal is to determine if you can reach the last index of the array, starting from the first index, where each element represents your maximum jump length from that position.

---

### Line-by-Line Breakdown

| Line | Code | Explanation |
| --- | --- | --- |
| **1** | `max_index = 0` | **Initialization:** We track the furthest index we can currently reach. We start at index 0, so the initial "reachable" limit is 0. |
| **2** | `for i in range(len(nums)):` | **Iteration:** We walk through every index `i` in the list from start to finish. |
| **3** | `if i > max_index:` | **The Safety Check:** If our current index `i` is greater than `max_index`, it means we have reached a point that is impossible to get to from any previous jump. |
| **4** | `return False` | If the safety check fails, we immediately return `False` because the end is unreachable. |
| **5** | `max_index = max(max_index, nums[i] + i)` | **Updating Reach:** At each step, we calculate how much further we could jump from here (`nums[i] + i`) and update `max_index` if this new jump goes further than our current record. |
| **6** | `return True` | **Final Success:** If we finish the loop without ever getting "stuck" (line 3), it means we successfully navigated through or past every index, so we return `True`. |

---

### Execution Trace Table

**Input:** `nums = [2, 3, 1, 0, 4]`

| Step | Index `i` | `nums[i]` | `i > max_index`? | `nums[i] + i` (Potential Reach) | `max_index` (Updated) |
| --- | --- | --- | --- | --- | --- |
| **Init** | - | - | - | - | 0 |
| **1** | 0 | 2 |  (No) |  |  |
| **2** | 1 | 3 |  (No) |  |  |
| **3** | 2 | 1 |  (No) |  |  |
| **4** | 3 | 0 |  (No) |  |  |
| **5** | 4 | 4 |  (No) |  |  |

**Final Result:** `True` (Loop finished successfully)

---

### Why this is "Greedy"

Instead of trying every possible combination of jumps (which would be very slow), we only care about the **furthest possible horizon** at any given moment. If our "horizon" (`max_index`) ever falls behind our current position, we know we've hit a dead end (usually a `0` that we can't jump over).

Would you like me to show you an example trace where the result would be `False`, such as with `[3, 2, 1, 0, 4]`?