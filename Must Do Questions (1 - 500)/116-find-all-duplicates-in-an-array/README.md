# 116. Find All Duplicates In An Array

**Difficulty**: Medium

**Topics**: Array, Hash Table

**Link**: https://leetcode.com/problems/find-all-duplicates-in-an-array

Of course. Let's break down this very clever Python code.

### Algorithm Goal

The function `findDuplicates` is designed to find all duplicate elements in an array `nums`. The key constraints for this specific solution to work are:

1.  The length of the array is `n`.
2.  All integers in the array are in the range `[1, n]`.
3.  Each integer appears either once or twice.

The algorithm is brilliant because it solves the problem in O(n) time and uses O(1) extra space (excluding the output list) by modifying the input array itself to keep track of the numbers it has seen. It uses the array's indices as a form of hash map and the sign of the number at each index as a "seen" flag.

### Line-by-Line Code Explanation

Here is a detailed breakdown of each line.

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
```

  * This defines the `Solution` class and the `findDuplicates` method.

<!-- end list -->

```python
        ans = []
```

  * **Purpose:** Initializes an empty list `ans` which will store the duplicate numbers we find.

<!-- end list -->

```python
        n = len(nums) 
```

  * **Purpose:** Gets the length of the input array. Although `n` is not directly used in the loop, it's good practice for understanding the constraints.

<!-- end list -->

```python
        for x in nums:
```

  * **Purpose:** This loop iterates through each number `x` in the input list `nums`.

<!-- end list -->

```python
            x = abs(x)
```

  * **Purpose:** This is a crucial step. As we iterate, we will be modifying the array by making some numbers negative. To ensure we always get the correct original value to use as an index, we take the absolute value of `x`.

<!-- end list -->

```python
            if nums[x - 1] < 0:
```

  * **Purpose:** This is the core logic for detecting a duplicate.
  * **How it works:** We use the value of the current number `x` to map to an index in the array (`x - 1` because arrays are 0-indexed). We then check the sign of the number at that index.
  * If `nums[x - 1]` is already negative, it means we have encountered the number `x` **before**. The first time we saw `x`, we would have flipped `nums[x - 1]` to be negative. So, finding it already negative means this is the second time we're seeing `x`, making it a duplicate.

<!-- end list -->

```python
                ans.append(x)
```

  * **Purpose:** If the `if` condition was true, we've confirmed `x` is a duplicate, so we add it to our `ans` list.

<!-- end list -->

```python
            nums[x - 1] *= -1
```

  * **Purpose:** This is the "marking" step. After checking the sign, we flip the sign of the number at index `x - 1` to be negative.
  * If this is the first time we've seen the number `x`, this action marks it as "seen". If it's the second time, this flip doesn't hurt; the number just stays negative. This ensures that the next time (if any) we see `x`, the check `nums[x-1] < 0` will be true.

<!-- end list -->

```python
        return ans
```

  * **Purpose:** After the loop has finished processing all numbers, the `ans` list contains all the duplicates, and the function returns it.

-----

### Live Trace Table Example

Let's trace the execution with the example `nums = [4, 3, 2, 7, 8, 2, 3, 1]`.

**Initial State:**

  * `ans = []`
  * `nums = [4, 3, 2, 7, 8, 2, 3, 1]`

**Trace Map:**

| Loop Iteration (`x` from original `nums`) | `x = abs(x)` | Index (`x-1`) | `nums` array state (before the flip) | `nums[x-1] < 0`? | Action | `nums` array state (after the flip) | `ans` |
| :--- | :--- | :--- | :--- | :--- | :--- |:--- | :--- |
| **x = 4** | 4 | 3 | `[4, 3, 2, 7, 8, 2, 3, 1]` | `False` (`7 > 0`) | Flip `nums[3]` | `[4, 3, 2, -7, 8, 2, 3, 1]` | `[]` |
| **x = 3** | 3 | 2 | `[4, 3, 2, -7, 8, 2, 3, 1]` | `False` (`2 > 0`) | Flip `nums[2]` | `[4, 3, -2, -7, 8, 2, 3, 1]` | `[]` |
| **x = 2** | 2 | 1 | `[4, 3, -2, -7, 8, 2, 3, 1]` | `False` (`3 > 0`) | Flip `nums[1]` | `[4, -3, -2, -7, 8, 2, 3, 1]` | `[]` |
| **x = 7** | 7 | 6 | `[4, -3, -2, -7, 8, 2, 3, 1]` | `False` (`3 > 0`) | Flip `nums[6]` | `[4, -3, -2, -7, 8, 2, -3, 1]` | `[]` |
| **x = 8** | 8 | 7 | `[4, -3, -2, -7, 8, 2, -3, 1]` | `False` (`1 > 0`) | Flip `nums[7]` | `[4, -3, -2, -7, 8, 2, -3, -1]`| `[]` |
| **x = 2** | 2 | 1 | `[4, -3, -2, -7, 8, 2, -3, -1]`| **`True`** (`-3 < 0`) | **Append 2**; Flip `nums[1]` | `[4, 3, -2, -7, 8, 2, -3, -1]` | `[2]` |
| **x = 3** | 3 | 2 | `[4, 3, -2, -7, 8, 2, -3, -1]` | **`True`** (`-2 < 0`) | **Append 3**; Flip `nums[2]` | `[4, 3, 2, -7, 8, 2, -3, -1]` | `[2, 3]` |
| **x = 1** | 1 | 0 | `[4, 3, 2, -7, 8, 2, -3, -1]` | `False` (`4 > 0`) | Flip `nums[0]` | `[-4, 3, 2, -7, 8, 2, -3, -1]`| `[2, 3]` |

**Final Step:**

1.  The loop finishes.
2.  The function returns the final `ans` list.

The returned value is **`[2, 3]`**, which correctly identifies the duplicates.