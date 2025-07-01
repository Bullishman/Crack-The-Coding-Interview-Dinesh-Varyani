# 9. Container With Most Water

**Difficulty**: Medium

**Topics**: Array, Two Pointers, Greedy

**Link**: https://leetcode.com/problems/container-with-most-water

Of course. This code solves the "Container With Most Water" problem using an efficient **Two-Pointer** approach.

### The Core Idea

The goal is to find the pair of vertical lines that can hold the most water. The area of water is determined by `width * height`, where the `width` is the distance between the lines and the `height` is limited by the **shorter** of the two lines.

The algorithm starts with the widest possible container (using the two outermost lines) and then intelligently "shrinks" the container by moving one of the pointers inwards. The key insight is this: to have any chance of finding a larger area, we must move the pointer that points to the **shorter line**. Moving the taller line's pointer would only decrease the width without any chance of increasing the limiting height, thus guaranteeing a smaller area.

Let's break down the code line by line with an example.

**Example:** `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
**Expected Result:** `49` (Formed by the line of height 8 at index 1 and the line of height 7 at index 8. Area = `min(8, 7) * (8 - 1) = 7 * 7 = 49`).

-----

### **Initial Setup**

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
```

This defines the main function.

```python
        mx, l, r = 0, 0, len(height) - 1
```

  * **What it does:** This initializes the three main variables in one line.
      * `mx = 0`: The `max` area found so far. We start with 0.
      * `l = 0`: The `left` pointer, which starts at the very beginning of the list (index 0).
      * `r = len(height) - 1`: The `right` pointer, which starts at the very end of the list.
  * **For our example:** `mx = 0`, `l = 0`, `r = 8`.

-----

### **The Main Loop**

```python
        while l < r:
```

  * **What it does:** The loop continues as long as the left pointer has not met or crossed the right pointer. This ensures we check all potential container widths.

#### **Inside the Loop: Calculation and Pointer Movement**

```python
            mx = max(mx, min(height[l], height[r]) * (r - l))
```

  * **This is the area calculation.** Let's break it down:
    1.  `min(height[l], height[r])`: Finds the shorter of the two lines, which dictates the water level (the height).
    2.  `(r - l)`: Calculates the distance between the lines (the width).
    3.  The height and width are multiplied to get the area of the current container.
    4.  `max(mx, ...)`: This compares the area of the current container with the maximum area found so far (`mx`) and updates `mx` if the current area is larger.

<!-- end list -->

```python
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
```

  * **This is the greedy pointer movement.**
  * **`if height[l] < height[r]: l += 1`**: If the left line is shorter than the right line, the left line is our limiting factor. The only way we can possibly find a bigger area is by finding a taller left line. So, we move the `l` pointer one step to the right.
  * **`else: r -= 1`**: If the right line is shorter (or if they are equal), the right line is the limiting factor. We move the `r` pointer one step to the left, hoping to find a taller right line.

-----

### **Final Return**

```python
        return mx
```

  * After the `while` loop finishes (when `l` and `r` meet), `mx` will hold the maximum possible area that could be formed. The function returns this value.

-----

### **Live Trace Table Map**

**`height` = `[1, 8, 6, 2, 5, 4, 8, 3, 7]`**

| `l` | `r` | `height[l]` | `height[r]` | `Width (r-l)` | `Height (min)` | Current Area | `mx` (Max Area) | Which pointer moves? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 8 | 1 | 7 | 8 | 1 | 8 | **8** | `l++` (since 1 \< 7) |
| 1 | 8 | 8 | 7 | 7 | 7 | 49 | **49** | `r--` (since 8 \> 7) |
| 1 | 7 | 8 | 3 | 6 | 3 | 18 | 49 | `r--` (since 8 \> 3) |
| 1 | 6 | 8 | 8 | 5 | 8 | 40 | 49 | `r--` (equal, else case) |
| 1 | 5 | 8 | 4 | 4 | 4 | 16 | 49 | `r--` (since 8 \> 4) |
| 1 | 4 | 8 | 5 | 3 | 5 | 15 | 49 | `r--` (since 8 \> 5) |
| 1 | 3 | 8 | 2 | 2 | 2 | 4 | 49 | `r--` (since 8 \> 2) |
| 1 | 2 | 8 | 6 | 1 | 6 | 6 | 49 | `r--` (since 8 \> 6) |

Now `l=1` and `r=1`. The condition `l < r` is false, and the loop terminates.

The function returns the final `mx` value, which is **49**.