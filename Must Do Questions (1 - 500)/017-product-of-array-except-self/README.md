# 17. Product Of Array Except Self

**Difficulty**: Medium

**Topics**: Array, Prefix Sum

**Link**: https://leetcode.com/problems/product-of-array-except-self

Of course. Let's do a detailed, line-by-line breakdown of this classic and highly efficient solution for the "Product of Array Except Self" problem.

### The Logic: Two-Pass Prefix and Postfix Products

The challenge is to solve this without using division and in O(n) time. A brute-force approach would be O(n²), which is too slow. This solution cleverly uses a **two-pass approach**.

1.  **Phase 1 (Left-to-Right Pass): Calculate Prefix Products**

      * The first loop iterates from the beginning to the end of the array.
      * It calculates the product of all elements to the *left* of the current index `i`.
      * The `result` array is populated such that `result[i]` will hold the product of `nums[0] * nums[1] * ... * nums[i-1]`.

2.  **Phase 2 (Right-to-Left Pass): Calculate Postfix Products and Combine**

      * The second loop iterates from the end to the beginning.
      * It calculates the product of all elements to the *right* of the current index `j`.
      * It then multiplies this "postfix product" with the "prefix product" already stored in `result[j]`.

After both passes, `result[i]` will contain the product of everything to its left multiplied by the product of everything to its right, which is the desired answer.

### The Example

Let's trace the execution with a standard example:

  * `nums = [1, 2, 3, 4]`

The expected result is `[24, 12, 8, 6]`.

-----

### Code and Live Demonstration

#### Phase 1: Left-to-Right Pass (Calculating Prefixes)

##### 1\. Initialization

```python
        p = 1
        result = []
```

  * `p`: A variable to keep track of the running product (the prefix product). It starts at `1` because the product of "nothing" (for the first element) is 1.
  * `result`: An empty list that will be populated.

##### 2\. The First Loop (`for i in range(len(nums)):`)

**Live Trace Table: Pass 1**
| `i` | `nums[i]` | `result` (before append) | `p` (before multiply) | Action on `result` | Action on `p` | `result` (end of loop) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | 1 | `[]` | 1 | `result.append(1)` | `p = 1 * 1 = 1` | `[1]` |
| **1** | 2 | `[1]` | 1 | `result.append(1)` | `p = 1 * 2 = 2` | `[1, 1]` |
| **2** | 3 | `[1, 1]` | 2 | `result.append(2)` | `p = 2 * 3 = 6` | `[1, 1, 2]` |
| **3** | 4 | `[1, 1, 2]` | 6 | `result.append(6)` | `p = 6 * 4 = 24`| `[1, 1, 2, 6]` |

**Step-by-Step Explanation:**

  * **`i = 0`**: `result.append(p)` appends `1`. `p` is updated to `p * nums[0]` (`1 * 1 = 1`).
  * **`i = 1`**: `result.append(p)` appends `1`. `p` is updated to `p * nums[1]` (`1 * 2 = 2`).
  * **`i = 2`**: `result.append(p)` appends `2`. `p` is updated to `p * nums[2]` (`2 * 3 = 6`).
  * **`i = 3`**: `result.append(p)` appends `6`. `p` is updated to `p * nums[3]` (`6 * 4 = 24`).

At the end of Phase 1, the `result` array is `[1, 1, 2, 6]`. Each element is the product of the numbers to its left in the original `nums` array.

-----

#### Phase 2: Right-to-Left Pass (Calculating Postfixes and Finalizing)

##### 3\. Re-initialization

```python
        p = 1
```

  * `p` is reset to `1` to now be used for the running postfix product.

##### 4\. The Second Loop (`for j in range(len(nums) - 1, -1, -1):`)

**Live Trace Table: Pass 2**
| `j` | `nums[j]` | `result[j]` (before) | `p` (before multiply) | Action on `result[j]` | Action on `p` | `result` (end of loop) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **3** | 4 | 6 | 1 | `result[3] = 6 * 1 = 6` | `p = 1 * 4 = 4` | `[1, 1, 2, 6]` |
| **2** | 3 | 2 | 4 | `result[2] = 2 * 4 = 8` | `p = 4 * 3 = 12` | `[1, 1, 8, 6]` |
| **1** | 2 | 1 | 12 | `result[1] = 1 * 12 = 12`| `p = 12 * 2 = 24`| `[1, 12, 8, 6]` |
| **0** | 1 | 1 | 24 | `result[0] = 1 * 24 = 24`| `p = 24 * 1 = 24`| `[24, 12, 8, 6]` |

**Step-by-Step Explanation:**

  * **`j = 3`**: `result[3]` (`6`) is multiplied by `p` (`1`). `result[3]` remains `6`. `p` is updated to `p * nums[3]` (`1 * 4 = 4`).
  * **`j = 2`**: `result[2]` (`2`) is multiplied by `p` (`4`). `result[2]` becomes `8`. `p` is updated to `p * nums[2]` (`4 * 3 = 12`).
  * **`j = 1`**: `result[1]` (`1`) is multiplied by `p` (`12`). `result[1]` becomes `12`. `p` is updated to `p * nums[1]` (`12 * 2 = 24`).
  * **`j = 0`**: `result[0]` (`1`) is multiplied by `p` (`24`). `result[0]` becomes `24`. `p` is updated to `p * nums[0]` (`24 * 1 = 24`).

The loop has finished.

-----

### 5\. Final Return

```python
        return result
```

  * The function returns the final `result` list.
  * The return value is `[24, 12, 8, 6]`, which is the correct answer.