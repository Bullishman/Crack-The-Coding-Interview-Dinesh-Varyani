# 11. Search In Rotated Sorted Array

**Difficulty**: Medium

**Topics**: Array, Binary Search

**Link**: https://leetcode.com/problems/search-in-rotated-sorted-array

Of course. This code implements a **Modified Binary Search** to find a `target` value in a sorted array that has been rotated.

### The Core Idea

A standard binary search relies on the entire array being sorted. Since this array is only "piecewise" sorted, we need to adapt.

The key insight is that for any rotated sorted array, if you split it in the middle, **at least one of the two halves must be sorted**.

The algorithm works like this:

1.  Start with left (`l`) and right (`r`) pointers at the ends of the array.
2.  Calculate the middle index `m`.
3.  Check if `nums[m]` is our target. If so, we're done.
4.  If not, determine which half is sorted: the left half (`l` to `m`) or the right half (`m` to `r`).
5.  Check if the `target` could exist within the range of that sorted half.
      * If yes, search in that sorted half by moving the appropriate pointer (`l` or `r`).
      * If no, the target must be in the *other*, unsorted half, so search there.
6.  Repeat until the pointers cross.

Let's break down the code line by line with an example.

**Example:** `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`
**Expected Result:** `4` (the index of the target `0`).

-----

### **Initial Setup**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
```

  * A simple edge case check. If the input list is empty, the target can't be there, so return -1.

<!-- end list -->

```python
        n = len(nums)
        l, r = 0, n - 1
```

  * **What it does:** This initializes the two pointers for our binary search.
  * `l`: The left pointer, starting at index `0`.
  * `r`: The right pointer, starting at the last index of the array.
  * **For our example:** `l=0`, `r=6`.

-----

### **The Main Binary Search Loop**

```python
        while l <= r:
```

  * The search continues as long as our left pointer has not crossed the right pointer.

<!-- end list -->

```python
            m = l + (r - l) // 2
```

  * Calculates the middle index `m`. This is a safe way to prevent potential integer overflow in other languages and is good practice.

<!-- end list -->

```python
            if nums[m] == target: return m
```

  * The simplest case. If the middle element happens to be our target, we've found it and can return its index `m` immediately.

-----

### **The Core Logic: Finding the Sorted Half**

This is where the modified logic begins. We must first figure out which side of `m` is the normally sorted part.

```python
            if nums[l] <= nums[m]:
```

  * **What it does:** This checks if the **left half** (from `l` to `m`) is sorted. If the element at the start of the window (`nums[l]`) is less than or equal to the middle element, this segment is guaranteed to be a standard, non-rotated, sorted subarray.
  * **Inside this `if` block, we know `nums[l...m]` is sorted.**

<!-- end list -->

```python
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
```

  * Now we ask: Is our `target` within the range of this sorted left half?
  * **If `yes` (`nums[l] <= target < nums[m]`):** The target must be in this left half. We can discard the right half by setting `r = m - 1`.
  * **If `no`:** The target is not in the sorted left half, so it must be in the unsorted right half. We discard the left half by setting `l = m + 1`.

<!-- end list -->

```python
            else:
```

  * **What it does:** If the `if` condition `nums[l] <= nums[m]` was false, it means the pivot point lies somewhere in the left half, and therefore the **right half** (from `m` to `r`) must be the sorted part.
  * **Inside this `else` block, we know `nums[m...r]` is sorted.**

<!-- end list -->

```python
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
```

  * Now we ask: Is our `target` within the range of this sorted right half?
  * **If `yes` (`nums[m] < target <= nums[r]`):** The target must be in this right half. We discard the left half by setting `l = m + 1`.
  * **If `no`:** The target is not in the sorted right half, so it must be in the unsorted left half. We discard the right half by setting `r = m - 1`.

-----

### **Final Return**

```python
        return -1
```

  * If the `while` loop finishes (meaning `l` has crossed `r`) and we haven't found the target, it means the target is not in the list. We return -1.

-----

### **Live Trace Table Map for `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`**

| Iteration | `l` | `r` | `m` | `nums[m]` | Which half is sorted? | Condition Check | Action (`l` or `r` changes) |
|:---:|:---:|:---:|:---:|:---:|:---|:---|:---|
| **1** | 0 | 6 | 3 | 7 | Left (`[4,5,6,7]`) | `target` (0) is NOT between 4 and 7. | Search right half. `l = 3 + 1 = 4`. |
| **2** | 4 | 6 | 5 | 1 | Right (`[1,2]`) | `target` (0) is NOT between 1 and 2. | Search left half. `r = 5 - 1 = 4`. |
| **3** | 4 | 4 | 4 | 0 | - | `nums[m]` (0) equals `target` (0). | **Return `m` (which is 4).** |

The function returns **`4`**.