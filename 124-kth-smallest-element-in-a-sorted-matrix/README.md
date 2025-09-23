# 124. Kth Smallest Element In A Sorted Matrix

**Difficulty**: Medium

**Topics**: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix

**Link**: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

Of course. Let's do a detailed line-by-line walkthrough of this code with a live trace table map.

This algorithm is a clever application of **Binary Search**. Instead of searching for an *index*, it searches for the correct *value* within the range of possible numbers in the matrix.

### The Example

Let's use a clear example to trace the execution.

  * **Matrix**:
    ```
    [[ 1,  5,  9],
     [10, 11, 13],
     [12, 13, 15]]
    ```
  * **k**: `8`

If we flatten and sort the matrix, we get `[1, 5, 9, 10, 11, 12, 13, 13, 15]`. The 8th smallest element is **13**. Our goal is to see how the code arrives at this answer.

-----

### Code and Live Demonstration

#### 1\. Setup

```python
        n = len(matrix)
        # n = 3
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        # low = 1, high = 15
```

  * We establish the search space. The answer *must* be between the smallest element (`1`) and the largest element (`15`).

#### 2\. The Main Loop (`while low < high`)

This is the binary search. It will continue until `low` and `high` converge on a single number.

-----

### **Live Trace Table Map (Outer Loop)**

| Iteration | `low` | `high` | `mid` Calculation | `mid` Value | `count` (from inner loop) | `count < 8`? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 1 | 15 | `1 + (15 - 1) // 2` | 8 | 2 | `True` | `low = mid + 1` |
| **2** | 9 | 15 | `9 + (15 - 9) // 2` | 12 | 6 | `True` | `low = mid + 1` |
| **3** | 13 | 15 | `13 + (15 - 13) // 2` | 14 | 8 | `False`| `high = mid` |
| **4** | 13 | 14 | `13 + (14 - 13) // 2` | 13 | 8 | `False`| `high = mid` |

The loop terminates because the condition `low < high` (`13 < 13`) is now false.

-----

### **Detailed Inner Loop Traces (The Counting Logic)**

Now let's break down how the `count` was calculated in each iteration of the main loop. The `count` variable answers the question: "How many elements in the matrix are less than or equal to `mid`?"

#### **Iteration 1: `mid = 8`**

  * `count` starts at `0`. We start at the top-right: `row = 0`, `col = 2`.

| `row` | `col` | `matrix[row][col]` | `matrix[row][col] <= 8`? | Action | `count` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 2 | 9 | `False` | Element is too big. Move left. `col--` | 0 |
| 0 | 1 | 5 | `True` | This element and all to its left (2 elements total) are valid. `count += (col + 1)` which is `0 + 2`. Move down. `row++` | **2** |
| 1 | 1 | 11 | `False` | Element is too big. Move left. `col--` | 2 |
| 1 | 0 | 10 | `False` | Element is too big. Move left. `col--` | 2 |
| 1 | -1 | - | (col is out of bounds, inner loop terminates) | - | 2 |

  * **Final Count = 2**. Since `2 < k=8`, our guess `mid=8` is too small. The 8th element must be larger. So, we set `low = mid + 1 = 9`.

#### **Iteration 2: `mid = 12`**

  * `count` starts at `0`. We start at the top-right: `row = 0`, `col = 2`.

| `row` | `col` | `matrix[row][col]` | `matrix[row][col] <= 12`? | Action | `count` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 2 | 9 | `True` | All 3 elements in this row are valid. `count += (col + 1)` which is `0 + 3`. Move down. `row++` | **3** |
| 1 | 2 | 13 | `False` | Too big. Move left. `col--` | 3 |
| 1 | 1 | 11 | `True` | 2 elements in this row are valid. `count += (col + 1)` which is `3 + 2`. Move down. `row++` | **5** |
| 2 | 1 | 13 | `False` | Too big. Move left. `col--` | 5 |
| 2 | 0 | 12 | `True` | 1 element in this row is valid. `count += (col + 1)` which is `5 + 1`. Move down. `row++` | **6** |
| 3 | 0 | - | (row is out of bounds, inner loop terminates) | - | 6 |

  * **Final Count = 6**. Since `6 < k=8`, our guess `mid=12` is still too small. So, we set `low = mid + 1 = 13`.

#### **Iteration 3: `mid = 14`**

  * `count` starts at `0`. We start at the top-right: `row = 0`, `col = 2`.

| `row` | `col` | `matrix[row][col]` | `matrix[row][col] <= 14`? | Action | `count` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 2 | 9 | `True` | All 3 elements valid. `count += 3`. Move down. `row++` | **3** |
| 1 | 2 | 13 | `True` | All 3 elements valid. `count += 3`. Move down. `row++` | **6** |
| 2 | 2 | 15 | `False`| Too big. Move left. `col--` | 6 |
| 2 | 1 | 13 | `True` | 2 elements valid. `count += 2`. Move down. `row++` | **8** |
| 3 | 1 | - | (row is out of bounds, inner loop terminates) | - | 8 |

  * **Final Count = 8**. Since `8 >= k=8`, this `mid=14` *could* be our answer, but there might be a smaller number that also has a count of 8 (like our target, 13). So we can't discard this possibility, we just know the answer is **not** bigger than 14. We set `high = mid = 14`.

#### **Iteration 4: `mid = 13`**

  * This runs the same logic as `mid=14`, but the check is now `<= 13`.
  * The counting process will yield exactly the same result. **Final Count = 8**.
  * Since `8 >= k=8`, `mid=13` is a potential answer. We set `high = mid = 13`.

-----

#### 3\. Return Value

```python
        # The loop has finished because low (13) is no longer < high (13).
        return low
```

  * The loop terminates, and we return `low`, which is **13**. This is the correct 8th smallest element.