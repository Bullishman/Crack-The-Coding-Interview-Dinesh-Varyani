# 14. Merge Intervals

**Difficulty**: Medium

**Topics**: Array, Sorting

**Link**: https://leetcode.com/problems/merge-intervals

Of course. Let's do a detailed, line-by-line breakdown of this classic and efficient solution for the "Merge Intervals" problem.

### The Logic: Sort and Merge

This algorithm relies on a simple but powerful greedy approach. If you want to merge intervals, it's much easier if you process them in a predictable order.

1.  **Sort:** The most crucial step is to sort the list of intervals based on their **start times** (`x[0]`). Once sorted, we are guaranteed that we are always looking at the next interval in chronological order.

2.  **Iterate and Merge:** We then iterate through this sorted list and maintain a `merged` list. For each `current_interval` we are looking at:

      * **Check for Overlap:** We compare the `current_interval` with the **last interval** added to our `merged` list. An overlap exists if the `current_interval`'s start time is less than or equal to the last merged interval's end time (`current_interval[0] <= last_merged[1]`).
      * **If Overlap:** We don't add a new interval. Instead, we "stretch" the last interval in `merged` by updating its end time to be the maximum of its current end time and the `current_interval`'s end time. This effectively combines the two.
      * **If No Overlap:** The `current_interval` is distinct and doesn't touch the previous one. We simply append it to the `merged` list as a new interval.

### The Example

Let's trace the execution with a standard example:

  * `intervals = [[1,4], [0,2], [3,5]]`

The expected result is `[[0,5]]` after merging all overlapping intervals.

-----

### Code and Live Demonstration

#### 1\. Initialization and Sorting

```python
        merged = []
        
        # The loop iterates through a sorted version of the intervals.
        # sorted(intervals, key = lambda x: x[0])
```

  * **Original `intervals`**: `[[1,4], [0,2], [3,5]]`
  * **Sorted `intervals`**: `[[0,2], [1,4], [3,5]]`
  * **`merged` list starts as**: `[]`

The `for` loop will now iterate through `[[0,2], [1,4], [3,5]]`.

#### 2\. The Main Loop (`for i in sorted(...)`)

-----

### **Live Trace Table Map**

| `i` (Current Interval) | `merged` (start of loop) | Condition: `merged` and `i[0] <= merged[-1][1]`? | Action | `merged` (end of loop) |
| :--- | :--- | :--- | :--- | :--- |
| **`[0,2]`** | `[]` | `merged` is empty (False) | `else`: Append `i` | `[[0,2]]` |
| **`[1,4]`** | `[[0,2]]` | `1 <= 2` is **True** | Update `merged[-1][1]` | `[[0,4]]` |
| **`[3,5]`** | `[[0,4]]` | `3 <= 4` is **True** | Update `merged[-1][1]` | `[[0,5]]` |

-----

### **Detailed Line-by-Line Breakdown**

#### Iteration 1: `i = [0,2]`

  * `merged` is `[]`.
  * **`if merged ...`**: The first part of the condition (`if merged`) is **False** because the list is empty.
  * **`else` block**: The code runs the `else` block.
      * `merged += i,` -\> This is a concise way to append `i` to the `merged` list.
  * **End of Loop 1 State**: `merged` is now `[[0,2]]`.

#### Iteration 2: `i = [1,4]`

  * `merged` is `[[0,2]]`. The last element `merged[-1]` is `[0,2]`.
  * **`if merged ...`**: The condition is checked:
      * `merged` is not empty.
      * `i[0] <= merged[-1][1]` -\> `1 <= 2`. The condition is **True**. There is an overlap.
  * **`if` block**: The `if` block runs.
      * `merged[-1][1] = max(merged[-1][1], i[1])`
      * `merged[-1][1] = max(2, 4)`
      * `merged[-1][1]` is updated to `4`.
  * **End of Loop 2 State**: `merged` is now `[[0,4]]`. The interval `[1,4]` was successfully merged into `[0,2]`.

#### Iteration 3: `i = [3,5]`

  * `merged` is `[[0,4]]`. The last element `merged[-1]` is `[0,4]`.
  * **`if merged ...`**: The condition is checked:
      * `merged` is not empty.
      * `i[0] <= merged[-1][1]` -\> `3 <= 4`. The condition is **True**. There is an overlap.
  * **`if` block**: The `if` block runs.
      * `merged[-1][1] = max(merged[-1][1], i[1])`
      * `merged[-1][1] = max(4, 5)`
      * `merged[-1][1]` is updated to `5`.
  * **End of Loop 3 State**: `merged` is now `[[0,5]]`. The interval `[3,5]` was merged.

The loop has now finished processing all the sorted intervals.

-----

### 3\. Final Return

```python
        return merged
```

  * The function returns the final `merged` list.
  * The return value is `[[0,5]]`, which is the correct answer.