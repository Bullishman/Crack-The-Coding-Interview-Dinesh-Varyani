# 31. Find First and Last Position of Element in Sorted Array

**Difficulty**: Medium

**Topics**: Array, Binary Search

**Link**: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

This solution uses a clever modification of **Binary Search** to find the "starting" and "ending" boundaries of a target number in a sorted array. Instead of searching for the target twice with different logic, it uses a single helper function to find the **leftmost insertion point**.

---

### Line-by-Line Logic

```python
def search(x: int) -> int:
    l, r = 0, len(nums)
```

* **The Helper:** `search(x)` finds the first index where `x` could be inserted while maintaining order. If `x` exists, it returns the index of the **first** occurrence.
* **`r = len(nums)`:** We use an "exclusive" right bound (standard for finding insertion points).

```python
while l < r:
    m = l + (r - l) // 2
```

* **The Loop:** Continues as long as the search range is valid.
* **Midpoint:** Calculates the middle index safely to avoid integer overflow.

```python
if nums[m] < x:
    l = m + 1
else:
    r = m
```

* **The Shift:** If the middle element is smaller than `x`, the target must be to the right (`l = m + 1`).
* **The Boundary:** If `nums[m]` is greater than *or equal* to `x`, we move the right bound to `m`. By moving `r` even when we find `x`, we "squeeze" the range to the left to find the **very first** occurrence.

```python
low, high = search(target), search(target + 1) - 1
```

* **`low`:** Finds the first index of `target`.
* **`high`:** Finds the first index where `target + 1` would go, then subtracts 1. This effectively finds the **last** index of our `target`.

```python
if low <= high:
    return [low, high]
return [-1, -1]
```

* **Validation:** If the target wasn't in the list, `low` will end up being greater than `high`. If it is valid, we return the range.

---

### Step-by-Step Execution Map

**Input:** `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`

#### Step 1: `search(8)` (Finding `low`)

| Iteration | `l` | `r` | `m` | `nums[m]` | Action |
| --- | --- | --- | --- | --- | --- |
| Initial | 0 | 6 | - | - | - |
| 1 | 0 | 6 | 3 | 8 | `nums[3] == 8`. Set `r = 3` |
| 2 | 0 | 3 | 1 | 7 | `7 < 8`. Set `l = 1 + 1 = 2` |
| 3 | 2 | 3 | 2 | 7 | `7 < 8`. Set `l = 2 + 1 = 3` |
| **End** | **3** | 3 | - | - | **Returns `l = 3**` |

#### Step 2: `search(9)` (Finding `high`)

| Iteration | `l` | `r` | `m` | `nums[m]` | Action |
| --- | --- | --- | --- | --- | --- |
| Initial | 0 | 6 | - | - | - |
| 1 | 0 | 6 | 3 | 8 | `8 < 9`. Set `l = 4` |
| 2 | 4 | 6 | 5 | 10 | `10 >= 9`. Set `r = 5` |
| 3 | 4 | 5 | 4 | 8 | `8 < 9`. Set `l = 5` |
| **End** | **5** | 5 | - | - | **Returns `l = 5**` |

#### Step 3: Final Calculation

* `low = 3`
* `high = 5 - 1 = 4`
* **Check:** `3 <= 4` is True.
* **Output:** `[3, 4]`

---

### Why `search(target + 1) - 1`?

This is the "pro-gamer" move of this algorithm. Because the array is sorted, the index where the *next* number (target + 1) would start is exactly one position after the *last* index of our current target. This allows you to reuse the exact same binary search logic twice.

Would you like me to show how this handles a case where the `target` doesn't exist in the array?