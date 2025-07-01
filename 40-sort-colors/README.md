This code implements a classic one-pass sorting algorithm known as the **Dutch National Flag problem**, attributed to Edsger W. Dijkstra. The goal is to sort an array containing only three distinct elements (in this case, 0, 1, and 2) in-place.

The algorithm works by partitioning the array into four conceptual sections using three pointers: `left`, `cur` (current), and `right`.

* **`0`s section:** `nums[0...left-1]`
* **`1`s section:** `nums[left...cur-1]`
* **Unknown section:** `nums[cur...right]` (this is the part we are actively processing)
* **`2`s section:** `nums[right+1...n-1]`

The main `while` loop shrinks the "Unknown" section until it's empty, at which point the array is sorted.

Let's break it down line by line with a detailed example.
**Example:** `nums = [2, 0, 2, 1, 1, 0]`

---

### **Initial Setup**

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur, left, right = 0, 0, len(nums) - 1
```
This initializes the three pointers:
* `left = 0`: The pointer for the boundary of the `0`s section. It starts at the beginning.
* `right = len(nums) - 1`: The pointer for the boundary of the `2`s section. It starts at the end. For our example, `right = 5`.
* `cur = 0`: The pointer that iterates through the array, examining each element. It also starts at the beginning.

**Initial State:**
`nums = [2, 0, 2, 1, 1, 0]`
`left = 0`, `cur = 0`, `right = 5`

---

### **The Main Loop**

```python
        while cur <= right:
```
The loop continues as long as our current pointer `cur` has not yet passed the right boundary `right`. This means there are still elements in the "Unknown" section to be processed.

### **Inside the Loop: The Three Cases**

#### **Case 1: `nums[cur]` is a 0**
```python
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
                cur += 1
```
* If the element at the `cur` pointer is a `0`, it belongs in the `0`s section.
* We swap it with the element at the `left` pointer.
* We then increment both `left` and `cur`. We increment `left` because we've just expanded the `0`s section. We can safely increment `cur` because we know the element we just swapped from the `left` position must be a `0` or a `1` (it can't be a `2`), and we are done with it.

#### **Case 2: `nums[cur]` is a 2**
```python
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
```
* If the element at the `cur` pointer is a `2`, it belongs at the end of the array.
* We swap it with the element at the `right` pointer.
* We then decrement `right` because we've just expanded the `2`s section.
* **Crucially, we DO NOT increment `cur`**. The element we just moved from the `right` side to the `cur` position is "unknown" and needs to be processed in the next iteration of the loop.

#### **Case 3: `nums[cur]` is a 1**
```python
            else: # This means nums[cur] == 1
                cur += 1
```
* If the element at `cur` is a `1`, it is already in its correct potential place (between the `0`s and `2`s).
* We don't need to do any swaps. We simply move on to the next element by incrementing `cur`.

---

### **Live Trace with `nums = [2, 0, 2, 1, 1, 0]`**

| Step | `cur` | `left` | `right` | `nums`                | Action (`nums[cur]` is...) |
| :--- | :---- | :----- | :------ | :-------------------- | :------------------------- |
| **Initial** | 0     | 0      | 5       | `[2, 0, 2, 1, 1, 0]`  | `nums[0]` is 2. **Case 2**.   |
| **1** | 0     | 0      | 4       | `[0, 0, 2, 1, 1, 2]`  | Swap `nums[0]` with `nums[5]`. Dec `right`. **Don't inc `cur`**. |
| **2** | 0     | 0      | 4       | `[0, 0, 2, 1, 1, 2]`  | `nums[0]` is 0. **Case 1**.   |
| **3** | 1     | 1      | 4       | `[0, 0, 2, 1, 1, 2]`  | Swap `nums[0]` with `nums[0]`. Inc `left`, `cur`. |
| **4** | 1     | 1      | 4       | `[0, 0, 2, 1, 1, 2]`  | `nums[1]` is 0. **Case 1**.   |
| **5** | 2     | 2      | 4       | `[0, 0, 2, 1, 1, 2]`  | Swap `nums[1]` with `nums[1]`. Inc `left`, `cur`. |
| **6** | 2     | 2      | 4       | `[0, 0, 2, 1, 1, 2]`  | `nums[2]` is 2. **Case 2**.   |
| **7** | 2     | 2      | 3       | `[0, 0, 1, 1, 2, 2]`  | Swap `nums[2]` with `nums[4]`. Dec `right`. **Don't inc `cur`**. |
| **8** | 2     | 2      | 3       | `[0, 0, 1, 1, 2, 2]`  | `nums[2]` is 1. **Case 3**.   |
| **9** | 3     | 2      | 3       | `[0, 0, 1, 1, 2, 2]`  | Inc `cur`.                 |
| **10** | 3     | 2      | 3       | `[0, 0, 1, 1, 2, 2]`  | `nums[3]` is 1. **Case 3**.   |
| **11** | 4     | 2      | 3       | `[0, 0, 1, 1, 2, 2]`  | Inc `cur`.                 |

Now `cur` is `4` and `right` is `3`. The condition `cur <= right` is **false**, so the loop terminates.

**Final Result:** `nums` is `[0, 0, 1, 1, 2, 2]`. The array is successfully sorted in-place.