# 6. 3sum

**Difficulty**: Medium

**Topics**: Array, Two Pointers, Sorting

**Link**: https://leetcode.com/problems/3sum

Of course. This code solves the "3Sum" problem, which asks for all **unique** triplets in a list of numbers that sum up to zero.

### The Core Idea

The algorithm uses a classic and efficient approach: **Sort + Two Pointers**.

1.  **Sort:** First, the input array `nums` is sorted. This is crucial because it allows us to move pointers in a predictable way.
2.  **Iterate and Fix:** The main `for` loop iterates through the sorted array, "fixing" one number at a time, `nums[i]`.
3.  **Two-Pointer Search:** For each fixed `nums[i]`, the problem is reduced to finding two other numbers in the rest of the array that sum to `-nums[i]`. This is a "2Sum" problem, which we can solve efficiently by using two pointers, `j` (left) and `k` (right), that start at either end of the remaining part of the array and move towards each other.
4.  **Handle Duplicates:** A `set` is used to automatically store only the unique triplets, preventing duplicate results.

Let's break down the code line by line with an example.

**Example:** `nums = [-1, 0, 1, 2, -1, -4]`
**Expected Result:** `[[-1, -1, 2], [-1, 0, 1]]` (order may vary)

-----

### **Initial Setup**

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
```

  * `s = set()`: An empty `set` is created. We will store our resulting triplets here. Using a set is a simple way to ensure that even if our code finds the same triplet multiple times, it will only be stored once.

<!-- end list -->

```python
        nums.sort()
```

  * **What it does:** Sorts the input array in place.
  * **Why it's essential:** This allows us to use the two-pointer technique. When our sum is too low, we can confidently move the left pointer to a larger number. When it's too high, we move the right pointer to a smaller number.
  * **For our example:** `nums` becomes `[-4, -1, -1, 0, 1, 2]`.

<!-- end list -->

```python
        n = len(nums)
```

  * Stores the length of the array for easy access. `n=6`.

-----

### **The Main Loops**

```python
        for i in range(n):
```

  * This is the outer loop that iterates through our sorted array from `i = 0` to `5`. In each iteration, `nums[i]` is the first "fixed" number of our potential triplet.

<!-- end list -->

```python
            j, k = i + 1, n - 1
```

  * Two pointers are initialized for the inner search.
  * `j`: The "left" pointer. It starts at the position right after `i`.
  * `k`: The "right" pointer. It starts at the very end of the array.
  * These pointers will scan the subarray to the right of `i`.

<!-- end list -->

```python
            while j < k:
```

  * The inner loop continues as long as the left pointer `j` has not crossed the right pointer `k`.

#### **The Core Logic Inside the Inner Loop**

```python
                tot = nums[i] + nums[j] + nums[k]
```

  * Calculates the sum of the three numbers pointed to by `i`, `j`, and `k`.

<!-- end list -->

```python
                if tot == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
```

  * **If the sum is 0**, we've found a valid triplet.
      * `s.add(...)`: We add the triplet **as a tuple** to our set `s`. (Tuples can be in sets, but lists cannot).
      * `j += 1` and `k -= 1`: We must move **both** pointers to look for a new, different pair of numbers.

<!-- end list -->

```python
                elif tot < 0:
                    j += 1
```

  * **If the sum is less than 0**, it's too small. To increase the sum, we need a larger number. Since the array is sorted, we move our left pointer `j` one step to the right.

<!-- end list -->

```python
                else: # This means tot > 0
                    k -= 1
```

  * **If the sum is greater than 0**, it's too big. To decrease the sum, we need a smaller number. We move our right pointer `k` one step to the left.

-----

### **The Final Return**

```python
        return [list(i) for i in s]
```

  * After all loops are finished, our set `s` contains all the unique triplets as tuples.
  * The problem asks for a list of lists as the output format.
  * This list comprehension `[list(i) for i in s]` iterates through each `tuple` `i` in the set, converts it to a `list`, and returns the final result.

-----

### **Live Trace Table Map**

**Sorted `nums` = `[-4, -1, -1, 0, 1, 2]`**

| `i` (value) | `j` (value) | `k` (value) | `tot` | Action | `s` (The Set) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** (-4) | 1 (-1) | 5 (2) | -3 | `tot < 0`, `j++` | `{}` |
| | 2 (-1) | 5 (2) | -3 | `tot < 0`, `j++` | `{}` |
| | 3 (0) | 5 (2) | -2 | `tot < 0`, `j++` | `{}` |
| | 4 (1) | 5 (2) | -1 | `tot < 0`, `j++`. Now `j=5`, `j` is not `< k`. Loop ends. | `{}` |
| **1** (-1) | 2 (-1) | 5 (2) | 0 | `tot == 0`, add `(-1,-1,2)`. `j++, k--` | `{ (-1,-1,2) }` |
| | 3 (0) | 4 (1) | 0 | `tot == 0`, add `(-1,0,1)`. `j++, k--` | `{ (-1,-1,2), (-1,0,1) }` |
| | 4 (1) | 3 (0) | | `j` is not `< k`. Loop ends. | `{ (-1,-1,2), (-1,0,1) }` |
| **2** (-1) | 3 (0) | 5 (2) | 1 | `tot > 0`, `k--` | `{ (-1,-1,2), (-1,0,1) }` |
| | 3 (0) | 4 (1) | 0 | `tot == 0`, add `(-1,0,1)`. Set doesn't change. `j++, k--`| `{ (-1,-1,2), (-1,0,1) }` |
| | 4 (1) | 3 (0) | | `j` is not `< k`. Loop ends. | `{ (-1,-1,2), (-1,0,1) }` |
| ... | ... | ... | ... | *Outer loop continues, but no more triplets sum to 0* | `{ (-1,-1,2), (-1,0,1) }` |

The function then returns `[list(i) for i in s]`, which gives `[[-1, -1, 2], [-1, 0, 1]]`.