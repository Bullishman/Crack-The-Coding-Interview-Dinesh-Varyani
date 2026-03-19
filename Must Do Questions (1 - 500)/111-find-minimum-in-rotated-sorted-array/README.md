# 111. Find Minimum In Rotated Sorted Array

**Difficulty**: Medium

**Topics**: Array, Binary Search

**Link**: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

Of course\! Let's break down this Python code.

The function `findMin` is designed to find the minimum element in a sorted array that has been rotated. For example, `[1, 2, 3, 4, 5]` might be rotated to become `[4, 5, 1, 2, 3]`. This code uses a modified binary search algorithm to find that minimum element efficiently.

### Algorithm Goal

The main idea is to find the "pivot point" where the rotation happened. This pivot point will always be the smallest number in the array. The algorithm cleverly uses binary search to narrow down the search space until it finds this point.

-----

### Line-by-Line Code Explanation

Here is a detailed explanation of each line.

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
```

  * This defines a class `Solution` and a method `findMin` within it.
  * `nums: List[int]` means the function expects a list of integers as input.
  * `-> int` means the function is expected to return a single integer.

<!-- end list -->

```python
        left, right = 0, len(nums) - 1
```

  * **Purpose:** Initialize two pointers, `left` and `right`.
  * **`left = 0`**: The `left` pointer starts at the very first index of the array (index 0).
  * **`right = len(nums) - 1`**: The `right` pointer starts at the very last index of the array.
  * These two pointers define the current search space.

<!-- end list -->

```python
        while left < right:
```

  * **Purpose:** This loop continues as long as our search space has at least two elements (`left` is not yet the same as `right`). The goal is to shrink this space until `left` and `right` point to the same element, which will be the minimum.

<!-- end list -->

```python
            mid = left + (right - left) // 2
```

  * **Purpose:** Calculate the middle index of the current search space.
  * Using `left + (right - left) // 2` is a safe way to calculate the middle index that prevents potential integer overflow in other languages, and it works perfectly in Python. `//` ensures we get an integer result (floor division).

<!-- end list -->

```python
            if nums[mid] > nums[right]:
```

  * **Purpose:** This is the core logic of the algorithm. We compare the value at the `mid` index with the value at the `right` index.
  * **Reasoning:**
      * If `nums[mid]` is greater than `nums[right]`, it tells us that the pivot point (the smallest number) **must** be somewhere to the right of `mid`.
      * Think about the example `[4, 5, 6, 7, 0, 1, 2]`. If `mid` points to `7` and `right` points to `2`, then `7 > 2`. This proves that the section from `left` to `mid` is part of the larger numbers from before the rotation, so we can discard it.

<!-- end list -->

```python
                left = mid + 1
```

  * **Purpose:** If the condition `nums[mid] > nums[right]` was true, we discard the left half of the search space (including `mid`) by moving our `left` pointer to `mid + 1`.

<!-- end list -->

```python
            else:
```

  * **Purpose:** This `else` block handles the case where `nums[mid] <= nums[right]`.
  * **Reasoning:**
      * If `nums[mid]` is less than or equal to `nums[right]`, it means the section from `mid` to `right` is sorted correctly.
      * This implies that the minimum element is either `nums[mid]` itself or is somewhere to the left of `mid`.

<!-- end list -->

```python
                right = mid
```

  * **Purpose:** We discard the right half of the search space by moving the `right` pointer to `mid`. We keep `mid` in our search space because it could potentially be the minimum element.

<!-- end list -->

```python
        return nums[left]
```

  * **Purpose:** When the `while` loop finishes, `left` and `right` will be pointing to the same index. This index holds the smallest element in the array. The function returns this value.

-----

### Live Trace Table Example

Let's trace the execution with the example `nums = [4, 5, 6, 7, 0, 1, 2]`.

**Initial State:**

| Variable | Value | Notes |
| :--- | :--- | :--- |
| `nums` | `[4, 5, 6, 7, 0, 1, 2]` | The input array. |
| `left` | `0` | Pointer to the start. |
| `right` | `6` | Pointer to the end (`len(nums) - 1`). |

**Trace Map:**

| Iteration | `left` | `right` | `left < right`? | `mid` | `nums[mid]` | `nums[right]` | `nums[mid] > nums[right]`? | Action |
| :--- | :-: | :-: | :--- | :-: | :--- | :--- | :--- | :--- |
| **Start** | 0 | 6 | `True` | - | - | - | - | Start loop. |
| **1** | 0 | 6 | `True` | `3` | `7` | `2` | `True` (7 \> 2) | The minimum is to the right. Set `left = mid + 1`. |
| **2** | 4 | 6 | `True` | `5` | `1` | `2` | `False` (1 \<= 2) | The minimum is at `mid` or to its left. Set `right = mid`. |
| **3** | 4 | 5 | `True` | `4` | `0` | `1` | `False` (0 \<= 1) | The minimum is at `mid` or to its left. Set `right = mid`. |
| **4** | 4 | 4 | `False` | - | - | - | - | Loop terminates because `left` is no longer less than `right`. |

**Final Step:**

1.  The `while` loop condition `left < right` (`4 < 4`) is now `False`.
2.  The loop exits.
3.  The function executes `return nums[left]`.
4.  Since `left` is `4`, it returns `nums[4]`, which is **0**.

The code correctly identified **0** as the minimum value in the rotated array.