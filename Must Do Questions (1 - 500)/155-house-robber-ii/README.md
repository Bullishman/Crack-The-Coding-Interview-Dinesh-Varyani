# 155. House Robber Ii

**Difficulty**: Medium

**Topics**: Array, Dynamic Programming

**Link**: https://leetcode.com/problems/house-robber-ii

Of course. Let's do a detailed, line-by-line breakdown of this space-optimized solution for the "House Robber II" problem.

### The Logic: Breaking the Circle

The main challenge is that the houses are in a circle, meaning the first and last houses are neighbors and cannot be robbed together. The code cleverly solves this by breaking the problem into two separate, standard "House Robber I" (linear) scenarios:

1.  **Scenario A:** Calculate the maximum profit from all houses **except the last one** (`nums[:-1]`).
2.  **Scenario B:** Calculate the maximum profit from all houses **except the first one** (`nums[1:]`).

The true maximum profit must be the highest value found in either Scenario A or Scenario B.

The `get_max` helper function solves the linear version of the problem using a space-optimized dynamic programming approach. Instead of a full DP array, it only keeps track of the maximum profit from the previous house (`max_rob`) and the one before that (`prev_rob`).

### The Example

Let's trace the execution with this array:

  * `nums = [1, 2, 3, 1]`

The optimal solution is to rob house 1 (value `1`) and house 3 (value `3`) for a total of **4**. Let's see how the code arrives at this.

-----

### Code and Live Demonstration

#### 1\. Main Function Call

The execution starts at the `return` statement of the `rob` function.

```python
        return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])
```

This line does three things and finds the maximum of their results:

1.  Calls `get_max` with `nums[:-1]`, which is **`[1, 2, 3]`**.
2.  Calls `get_max` with `nums[1:]`, which is **`[2, 3, 1]`**.
3.  Includes `nums[0]` (`1`) in the `max` comparison. This is a concise way to handle the edge case where `nums` has only one element. For longer arrays, this value is usually redundant.

Let's trace each `get_max` call separately.

-----

### **Trace 1: `get_max([1, 2, 3])`**

#### Initialization inside `get_max`

```python
        prev_rob = max_rob = 0
```

  * `prev_rob` = Max profit from two houses ago.
  * `max_rob` = Max profit from the previous house.

#### The Loop (`for cur_val in nums:`)

**Live Trace Table for `get_max([1, 2, 3])`**

| `cur_val` | `prev_rob` (start) | `max_rob` (start) | `temp` Calculation: `max(max_rob, prev_rob + cur_val)` | `prev_rob` (end) | `max_rob` (end) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 0 | 0 | `max(0, 0 + 1)` = **1** | 0 | **1** |
| **2** | 0 | 1 | `max(1, 0 + 2)` = **2** | 1 | **2** |
| **3** | 1 | 2 | `max(2, 1 + 3)` = **4** | 2 | **4** |

**Step-by-Step Explanation:**

  * **`cur_val = 1`**:
      * `temp = max(max_rob, prev_rob + cur_val)` -\> `max(0, 0 + 1)` -\> `temp` is `1`.
      * `prev_rob` becomes the old `max_rob` -\> `prev_rob` is `0`.
      * `max_rob` becomes `temp` -\> `max_rob` is `1`.
  * **`cur_val = 2`**:
      * `temp = max(max_rob, prev_rob + cur_val)` -\> `max(1, 0 + 2)` -\> `temp` is `2`. (It's better to just rob this house than the previous one).
      * `prev_rob` becomes `1`.
      * `max_rob` becomes `2`.
  * **`cur_val = 3`**:
      * `temp = max(max_rob, prev_rob + cur_val)` -\> `max(2, 1 + 3)` -\> `temp` is `4`. (It's better to rob this house and the one from two steps ago than to stick with the previous profit).
      * `prev_rob` becomes `2`.
      * `max_rob` becomes `4`.

The loop finishes. `get_max` returns `max_rob`, which is **4**.

-----

### **Trace 2: `get_max([2, 3, 1])`**

#### Initialization inside `get_max`

`prev_rob = 0`, `max_rob = 0`

#### The Loop (`for cur_val in nums:`)

**Live Trace Table for `get_max([2, 3, 1])`**

| `cur_val` | `prev_rob` (start) | `max_rob` (start) | `temp` Calculation: `max(max_rob, prev_rob + cur_val)` | `prev_rob` (end) | `max_rob` (end) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2** | 0 | 0 | `max(0, 0 + 2)` = **2** | 0 | **2** |
| **3** | 0 | 2 | `max(2, 0 + 3)` = **3** | 2 | **3** |
| **1** | 2 | 3 | `max(3, 2 + 1)` = **3** | 3 | **3** |

The loop finishes. `get_max` returns `max_rob`, which is **3**.

-----

### 2\. Final Calculation and Return

The main `rob` function now computes the final result:

```python
        return max(4, 3, 1)
```

  * The first argument (`4`) comes from `get_max([1, 2, 3])`.
  * The second argument (`3`) comes from `get_max([2, 3, 1])`.
  * The third argument (`1`) comes from `nums[0]`.

The `max` of these values is `4`. The function returns **4**, which is the correct maximum profit.