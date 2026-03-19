# 162. Gas Station

**Difficulty**: Medium

**Topics**: Array, Greedy

**Link**: https://leetcode.com/problems/gas-station

Of course. Let's do a detailed, line-by-line breakdown of this very efficient greedy solution for the "Gas Station" problem.

### The Logic: A Greedy Approach

This problem seems complex, but it's built on two key insights that allow for a simple, single-pass greedy solution.

1.  **Possibility Check:** If the total amount of gas available in the entire circuit (`sum(gas)`) is less than the total cost to travel the entire circuit (`sum(cost)`), it is absolutely impossible to complete the trip, regardless of the starting point. This allows for a quick exit if no solution exists.

2.  **Greedy Start Point Selection:** If a solution *does* exist (guaranteed by the check above), we can find the starting point with a single pass.

      * We maintain a running `fuel` tank and a candidate `start` station.
      * We try to travel from one station to the next. If at any point `i`, we realize we can't make it to station `i+1` (i.e., our current `fuel` plus the `gas` at station `i` is not enough to cover the `cost`), it means something crucial:
      * **Not only is our current `start` invalid, but *every* station between our `start` and station `i` is also an invalid starting point.** Why? Because if we had started at any of those intermediate stations, we would have arrived at station `i` with even *less* fuel than we have now, and we would still fail.
      * Therefore, if we fail at station `i`, the only new possible candidate for a starting station is `i + 1`. We reset our `fuel` to `0` and update `start` to `i + 1`.

Because the initial check guarantees a solution exists, the `start` candidate we are left with at the end of the single pass must be the correct one.

### The Example

Let's trace the execution with a classic example:

  * `gas  = [1, 2, 3, 4, 5]`
  * `cost = [3, 4, 5, 1, 2]`

The correct starting station is index **3** (where `gas` is 4).

-----

### Code and Live Demonstration

#### 1\. The Possibility Check

```python
        if sum(gas) < sum(cost):
            return -1
```

  * `sum(gas)` = 1 + 2 + 3 + 4 + 5 = 15
  * `sum(cost)` = 3 + 4 + 5 + 1 + 2 = 15
  * The condition `15 < 15` is **False**.
  * The code proceeds, because we have proven that a solution is guaranteed to exist.

#### 2\. Initialization

```python
        start, fuel = 0, 0
```

  * `start`: Our current candidate for the answer. It starts at `0`.
  * `fuel`: The amount of gas in our tank. It starts at `0`.

#### 3\. The Main Loop (`for i in range(len(gas)):`)

This loop simulates the trip, updating `fuel` and the candidate `start` station as it goes.

-----

### **Live Trace Table Map**

| `i` | `gas[i]` | `cost[i]` | `fuel` (start of loop) | Condition: `fuel + gas[i] < cost[i]`? | Action | `start` (end of loop) | `fuel` (end of loop) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | 1 | 3 | 0 | `0 + 1 < 3` is **True** | Fail. Reset `start` and `fuel`. | **1** | **0** |
| **1** | 2 | 4 | 0 | `0 + 2 < 4` is **True** | Fail. Reset `start` and `fuel`. | **2** | **0** |
| **2** | 3 | 5 | 0 | `0 + 3 < 5` is **True** | Fail. Reset `start` and `fuel`. | **3** | **0** |
| **3** | 4 | 1 | 0 | `0 + 4 < 1` is **False**| Succeed. Update `fuel`. | 3 | **3** |
| **4** | 5 | 2 | 3 | `3 + 5 < 2` is **False**| Succeed. Update `fuel`. | 3 | **6** |

-----

### **Detailed Line-by-Line Breakdown**

#### Iteration `i = 0`

  * `fuel` is `0`.
  * **`if` Check**: `0 + gas[0] < cost[0]` -\> `1 < 3`. This is **True**.
  * **Action**: We can't get from station 0 to station 1. This means 0 cannot be the start. The new candidate is `i + 1`.
      * `start = 0 + 1` -\> `start` becomes **1**.
      * `fuel = 0`.

#### Iteration `i = 1`

  * `fuel` is `0`.
  * **`if` Check**: `0 + gas[1] < cost[1]` -\> `2 < 4`. This is **True**.
  * **Action**: We can't get from station 1 to station 2. New candidate is `i + 1`.
      * `start = 1 + 1` -\> `start` becomes **2**.
      * `fuel = 0`.

#### Iteration `i = 2`

  * `fuel` is `0`.
  * **`if` Check**: `0 + gas[2] < cost[2]` -\> `3 < 5`. This is **True**.
  * **Action**: We can't get from station 2 to station 3. New candidate is `i + 1`.
      * `start = 2 + 1` -\> `start` becomes **3**.
      * `fuel = 0`.

#### Iteration `i = 3`

  * `fuel` is `0`.
  * **`if` Check**: `0 + gas[3] < cost[3]` -\> `4 < 1`. This is **False**.
  * **Action**: We can successfully travel from station 3 to 4. We update our tank.
      * `fuel += gas[3] - cost[3]` -\> `fuel = 0 + 4 - 1` -\> `fuel` becomes **3**.
      * `start` remains **3**.

#### Iteration `i = 4`

  * `fuel` is `3`.
  * **`if` Check**: `3 + gas[4] < cost[4]` -\> `8 < 2`. This is **False**.
  * **Action**: We can successfully travel from station 4 to 0.
      * `fuel += gas[4] - cost[4]` -\> `fuel = 3 + 5 - 2` -\> `fuel` becomes **6**.
      * `start` remains **3**.

The loop has now finished.

-----

### 4\. Final Return

```python
        return start
```

  * The final value of `start` is **3**.
  * The function returns `3`, which is the correct starting index.