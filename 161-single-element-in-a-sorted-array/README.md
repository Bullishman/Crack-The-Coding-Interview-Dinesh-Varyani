# 161. Single Element In A Sorted Array

**Difficulty**: Medium

**Topics**: Array, Binary Search

**Link**: https://leetcode.com/problems/single-element-in-a-sorted-array

Of course. Let's do a detailed, line-by-line breakdown of this very clever binary search solution.

### The Logic: Binary Search on Pairs

This problem can be solved by a modified binary search. The key insight comes from the structure of the array: before the single element, all numbers form pairs at predictable indices: `(0,1)`, `(2,3)`, `(4,5)`, and so on. After the single element, this pattern is disrupted.

  * **In the "correct" half:** The first element of a pair is always at an **even** index, and its partner is at the next **odd** index.
  * **In the "disrupted" half:** This pattern is broken.

The algorithm uses binary search to find the exact point where this pattern breaks.

#### The `mid ^ 1` Trick

This is the brilliant core of the algorithm. The bitwise XOR `^` operation is used to find the "partner" index for any given `mid`:

  * If `mid` is **even** (e.g., `4`), `mid ^ 1` is `4 + 1 = 5`.
  * If `mid` is **odd** (e.g., `5`), `mid ^ 1` is `5 - 1 = 4`.

So, `nums[mid] == nums[mid ^ 1]` is a concise way to check if the number at `mid` and its intended partner are the same, regardless of whether `mid` is even or odd.

1.  **If `nums[mid] == nums[mid ^ 1]`:** The pair is intact. This means all pairs up to this point are correct, and the single element must be **to the right**. We discard the left half by setting `left = mid + 1`.
2.  **If `nums[mid] != nums[mid ^ 1]`:** The pair is broken. This means the single element has already appeared and disrupted the pattern. The single element must be **in the current position or to the left**. We discard the right half by setting `right = mid - 1`.

### The Example

Let's trace the execution with the following array:

  * `nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]`

The single non-duplicate element is **2**. The algorithm should return this value.

-----

### Code and Live Demonstration

#### 1\. Setup

```python
        left, right = 0, len(nums) - 2
```

  * `left` is `0`.
  * `len(nums)` is `9`. `right` is set to `9 - 2 = 7`.
  * **Why `len(nums) - 2`?** Because our check `mid ^ 1` always looks at a pair of indices. The last possible pair starts at the second-to-last element, so we don't need to include the final element in our initial search space. The logic will naturally guide the `left` pointer to it if needed.

#### 2\. The Main Loop (`while left <= right`)

This is our binary search. It will run until the `left` and `right` pointers cross.

-----

### **Live Trace Table Map**

| Iteration | `left` | `right` | `mid` Calculation | `mid` | `mid ^ 1` (Partner Idx) | Condition: `nums[mid] == nums[mid^1]`? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | 0 | 7 | - | - | - | - | - |
| **1** | 0 | 7 | `0 + (7-0)//2` | **3** | 2 | `nums[3]` (3) == `nums[2]` (2)? **False** | `right = mid - 1` |
| **2** | 0 | 2 | `0 + (2-0)//2` | **1** | 0 | `nums[1]` (1) == `nums[0]` (1)? **True** | `left = mid + 1` |
| **3** | 2 | 2 | `2 + (2-2)//2` | **2** | 3 | `nums[2]` (2) == `nums[3]` (3)? **False** | `right = mid - 1` |

  * The loop now terminates because the condition `left <= right` (`2 <= 1`) is **false**.

-----

### **Detailed Line-by-Line Breakdown**

#### Iteration 1

  * **Pointers**: `left = 0`, `right = 7`.
  * `mid = 0 + (7 - 0) // 2` -\> `mid` is **3**.
  * We are examining `nums[3]`, which is `3`.
  * **The check**: `if nums[mid] == nums[mid ^ 1]`
      * `mid` is `3`. `mid ^ 1` is `2`.
      * Is `nums[3] == nums[2]`? Is `3 == 2`? **False**.
  * **Action**: The pair is broken. The single element is at or to the left of `mid`. We discard the right half.
      * `right = mid - 1` -\> `right` becomes `3 - 1 = 2`.

#### Iteration 2

  * **Pointers**: `left = 0`, `right = 2`.
  * `mid = 0 + (2 - 0) // 2` -\> `mid` is **1**.
  * We are examining `nums[1]`, which is `1`.
  * **The check**: `if nums[mid] == nums[mid ^ 1]`
      * `mid` is `1`. `mid ^ 1` is `0`.
      * Is `nums[1] == nums[0]`? Is `1 == 1`? **True**.
  * **Action**: This pair is intact. The single element must be to the right of this pair. We discard the left half.
      * `left = mid + 1` -\> `left` becomes `1 + 1 = 2`.

#### Iteration 3

  * **Pointers**: `left = 2`, `right = 2`.
  * `mid = 2 + (2 - 2) // 2` -\> `mid` is **2**.
  * We are examining `nums[2]`, which is `2`.
  * **The check**: `if nums[mid] == nums[mid ^ 1]`
      * `mid` is `2`. `mid ^ 1` is `3`.
      * Is `nums[2] == nums[3]`? Is `2 == 3`? **False**.
  * **Action**: The pair is broken. The single element is at or to the left of `mid`. We discard the right half.
      * `right = mid - 1` -\> `right` becomes `2 - 1 = 1`.

The `while` loop condition `left <= right` (`2 <= 1`) is now false, so the loop terminates.

-----

### 3\. Final Return

```python
        return nums[left]
```

  * The loop has finished. The value of `left` is **2**.
  * The function returns `nums[2]`.
  * Looking at our array, `nums[2]` is **2**.
  * This is the correct answer. The `left` pointer successfully converged on the index of the first element that breaks the pairing pattern.