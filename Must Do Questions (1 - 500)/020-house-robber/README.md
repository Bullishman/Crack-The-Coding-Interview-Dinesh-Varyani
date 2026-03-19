# 20. House Robber

**Difficulty**: Medium

**Topics**: Array, Dynamic Programming

**Link**: https://leetcode.com/problems/house-robber

Of course. Let's do a detailed, line-by-line breakdown of this very compact and elegant solution for the "House Robber" problem.

### The Logic: Space-Optimized Dynamic Programming

This code solves the problem using dynamic programming but in a highly space-efficient way. Instead of building a full DP array (which would take O(n) space), it realizes that to decide the maximum profit at the *current* house, you only need to know the maximum profits from the *previous* two houses.

The `bag` tuple is the key. It's a clever way to store the only two pieces of information we need as we iterate:

  * `bag[0]`: The maximum profit you could have from two houses ago.
  * `bag[1]`: The maximum profit you could have from the previous house.

The core logic inside the loop decides the new maximum profit by comparing two choices for the current `house`:

1.  **Rob the current house:** The profit would be `house + bag[0]` (the current house's value plus the max profit from two houses ago, since you can't have robbed the previous one).
2.  **Don't rob the current house:** The profit would simply be `bag[1]` (the max profit you had from the previous step).

The algorithm takes the `max` of these two choices and then updates the `bag` for the next iteration.

### The Example

Let's trace the execution with a classic example:

  * `nums = [2, 7, 9, 3, 1]`

The optimal solution is to rob houses with values `2`, `9`, and `1` for a total profit of **12**.

-----

### Code and Live Demonstration

#### 1\. Initialization

```python
        if not nums:
            return # Should ideally be 0, but following the code.

        bag = (0, 0)
```

  * The code handles the empty list case.
  * `bag` is initialized to `(0, 0)`. This represents the state before we've looked at any houses. The profit from the "previous" house is 0, and the profit from the "house before that" is also 0.

#### 2\. The Main Loop (`for house in nums:`)

The loop will iterate through each value in `[2, 7, 9, 3, 1]`.

-----

### **Live Trace Table Map**

| `house` | `bag` (start of loop) `(profit 2 ago, profit 1 ago)` | `bag[0] + house` (Rob current) | `bag[1]` (Skip current) | `max(...)` | `bag` (end of loop) `(old bag[1], new max)` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | `(0, 0)` | - | - | - | `(0, 0)` |
| **2** | `(0, 0)` | `0 + 2 = 2` | 0 | **2** | `(0, 2)` |
| **7** | `(0, 2)` | `0 + 7 = 7` | 2 | **7** | `(2, 7)` |
| **9** | `(2, 7)` | `2 + 9 = 11` | 7 | **11** | `(7, 11)` |
| **3** | `(7, 11)` | `7 + 3 = 10` | 11 | **11** | `(11, 11)` |
| **1** | `(11, 11)` | `11 + 1 = 12` | 11 | **12** | `(11, 12)` |

-----

### **Detailed Line-by-Line Breakdown**

#### Iteration 1: `house = 2`

  * Current `bag` is `(0, 0)`.
  * The new `bag` is calculated: `(bag[1], max(bag[0] + house, bag[1]))`
  * `bag = (0, max(0 + 2, 0))`
  * `bag` becomes **`(0, 2)`**. The max profit after considering the first house is 2.

#### Iteration 2: `house = 7`

  * Current `bag` is `(0, 2)`.
  * The new `bag` is calculated: `(bag[1], max(bag[0] + house, bag[1]))`
  * `bag = (2, max(0 + 7, 2))`
  * `bag` becomes **`(2, 7)`**. The max profit is 7 (by robbing the 7 and skipping the 2).

#### Iteration 3: `house = 9`

  * Current `bag` is `(2, 7)`.
  * The new `bag` is calculated: `(bag[1], max(bag[0] + house, bag[1]))`
  * `bag = (7, max(2 + 9, 7))` -\> `max(11, 7)` is 11.
  * `bag` becomes **`(7, 11)`**. The max profit is 11 (by robbing the 2 and 9, skipping the 7).

#### Iteration 4: `house = 3`

  * Current `bag` is `(7, 11)`.
  * The new `bag` is calculated: `(bag[1], max(bag[0] + house, bag[1]))`
  * `bag = (11, max(7 + 3, 11))` -\> `max(10, 11)` is 11.
  * `bag` becomes **`(11, 11)`**. The max profit is still 11 (skipping the 3 is better than robbing it).

#### Iteration 5: `house = 1`

  * Current `bag` is `(11, 11)`.
  * The new `bag` is calculated: `(bag[1], max(bag[0] + house, bag[1]))`
  * `bag = (11, max(11 + 1, 11))` -\> `max(12, 11)` is 12.
  * `bag` becomes **`(11, 12)`**. The max profit is 12 (by robbing the 1, which implies robbing the 9 and 2 before it).

The loop has finished.

-----

### 3\. Final Return

```python
        return bag[1]
```

  * The final state of `bag` is `(11, 12)`.
  * `bag[1]` holds the maximum profit calculated up to the very last house.
  * The function returns **12**, which is the correct answer.