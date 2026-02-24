# 19. Subarray Sum Equals K

**Difficulty**: Medium

**Topics**: Array, Hash Table, Prefix Sum

**Link**: https://leetcode.com/problems/subarray-sum-equals-k

Of course. Let's do a detailed, line-by-line breakdown of this brilliant solution for the "Subarray Sum Equals K" problem.

### The Logic: Prefix Sums and a Hash Map

A brute-force approach (checking every possible subarray) would be too slow (O(n²)). This code uses a highly efficient O(n) approach that combines the concepts of **prefix sums** and a **hash map**.

The core mathematical idea is this: if the sum of elements from index 0 to `j` is `prefix_sum_j`, and the sum from 0 to `i` (where `i < j`) is `prefix_sum_i`, then the sum of the subarray between `i+1` and `j` is simply `prefix_sum_j - prefix_sum_i`.

We are looking for subarrays that sum to `k`. So, for any given point `j`, we can say:
`k = prefix_sum_j - prefix_sum_i`

Rearranging this, we get:
`prefix_sum_i = prefix_sum_j - k`

This is the key insight\! As we iterate through the array and calculate the current `prefix_sum` (let's call it `current_sum`), we don't need to look back at the array. We only need to ask: **"How many times have we previously seen a prefix sum that equals `current_sum - k`?"**

The hash map (`count` dictionary) is used to store the frequencies of all the prefix sums we have encountered so far.

1.  **Initialization**:
      * `count = {0: 1}`: We initialize the map with a prefix sum of `0` having been seen once. This is the crucial base case. It handles subarrays that start from the very beginning of the array (index 0).
      * `prefix_sum = 0`, `res = 0`: Initialize our running sum and final result count.
2.  **Iteration**: For each number in the array:
      * Update the `prefix_sum`.
      * Look in our `count` map for `prefix_sum - k`. The number of times this value has occurred is the number of new subarrays we just found that end at the current position. Add this to our result `res`.
      * Update the `count` map with the *current* `prefix_sum`, either incrementing its count or adding it to the map for the first time.

### The Example

Let's trace the execution with an example that shows the logic clearly:

  * `nums = [1, 2, 1, 2, 1]`
  * `k = 3`

The subarrays that sum to `3` are `[1, 2]`, `[2, 1]`, `[1, 2]`, `[2, 1]`. The expected result is **4**.

-----

### Code and Live Demonstration

#### 1\. Initialization

```python
        count = {0: 1}
        prefix_sum = res = 0
```

  * `count`: `{0: 1}`. A prefix sum of 0 has been seen once (the "empty" prefix before the array).
  * `prefix_sum`: `0`
  * `res`: `0`

#### 2\. The Main Loop (`for num in nums:`)

-----

### **Live Trace Table Map**

| `num` | `prefix_sum` (after `+=num`) | `prefix_sum - k` (Target) | `count` (before lookup) | `count.get(Target, 0)` | `res` (after `+=`) | `count` (after update) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | 0 | - | `{0: 1}` | - | 0 | `{0: 1}` |
| **1** | 1 | `1 - 3 = -2` | `{0: 1}` | 0 | **0** | `{0: 1, 1: 1}` |
| **2** | 3 | `3 - 3 = 0` | `{0: 1, 1: 1}` | 1 | **1** | `{0: 1, 1: 1, 3: 1}` |
| **1** | 4 | `4 - 3 = 1` | `{0: 1, 1: 1, 3: 1}` | 1 | **2** | `{0: 1, 1: 1, 3: 1, 4: 1}` |
| **2** | 6 | `6 - 3 = 3` | `{0: 1, 1: 1, 3: 1, 4: 1}` | 1 | **3** | `{0: 1, 1: 1, 3: 2, 4: 1}` |
| **1** | 7 | `7 - 3 = 4` | `{0: 1, 1: 1, 3: 2, 4: 1}` | 1 | **4** | `{0: 1, 1: 1, 3: 2, 4: 1, 7: 1}` |

-----

### **Detailed Line-by-Line Breakdown**

#### Iteration 1: `num = 1`

  * `prefix_sum += num`: `prefix_sum` becomes `0 + 1 = 1`.
  * `res += count.get(prefix_sum - k, 0)`:
      * We look for `1 - 3 = -2` in the `count` map.
      * `count.get(-2, 0)` returns `0`.
      * `res` becomes `0 + 0 = 0`.
  * `count[prefix_sum] = count.get(prefix_sum, 0) + 1`:
      * `count.get(1, 0)` is `0`.
      * `count[1]` is set to `0 + 1 = 1`. `count` is now `{0: 1, 1: 1}`.

#### Iteration 2: `num = 2`

  * `prefix_sum += num`: `prefix_sum` becomes `1 + 2 = 3`.
  * `res += count.get(prefix_sum - k, 0)`:
      * We look for `3 - 3 = 0`.
      * `count.get(0, 0)` returns **`1`**. This is our first match\! It corresponds to the subarray `[1, 2]`.
      * `res` becomes `0 + 1 = 1`.
  * `count[prefix_sum] = count.get(prefix_sum, 0) + 1`:
      * `count.get(3, 0)` is `0`.
      * `count[3]` is set to `0 + 1 = 1`. `count` is now `{0: 1, 1: 1, 3: 1}`.

#### Iteration 3: `num = 1`

  * `prefix_sum += num`: `prefix_sum` becomes `3 + 1 = 4`.
  * `res += count.get(prefix_sum - k, 0)`:
      * We look for `4 - 3 = 1`.
      * `count.get(1, 0)` returns **`1`**. This match corresponds to the subarray `[2, 1]`.
      * `res` becomes `1 + 1 = 2`.
  * `count[prefix_sum] = count.get(prefix_sum, 0) + 1`:
      * `count[4]` is set to `1`. `count` is now `{0: 1, 1: 1, 3: 1, 4: 1}`.

#### Iteration 4: `num = 2`

  * `prefix_sum += num`: `prefix_sum` becomes `4 + 2 = 6`.
  * `res += count.get(prefix_sum - k, 0)`:
      * We look for `6 - 3 = 3`.
      * `count.get(3, 0)` returns **`1`**. This match corresponds to the subarray `[1, 2]`.
      * `res` becomes `2 + 1 = 3`.
  * `count[prefix_sum] = count.get(prefix_sum, 0) + 1`:
      * `count.get(6, 0)` is `0`. We are about to update `count[prefix_sum]`. Oops, `prefix_sum` is `6`. The `count` key should be `6`. The value we look up is `3`.
      * Let's re-read the code. `count[prefix_sum]`. Ah, we update the count for the *current* prefix sum.
      * `count.get(3, 0)` is `1`. `count[3]` becomes `1 + 1 = 2`. `count` is now `{0: 1, 1: 1, 3: 2, 4: 1}`.

My apologies, let me correct the trace table. I was updating the wrong key in the last column.

**Corrected Live Trace Table Map**
| `num` | `prefix_sum` (after `+=num`) | `prefix_sum - k` (Target) | `count` (before lookup) | `count.get(Target, 0)` | `res` (after `+=`) | `count` (after update) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | 0 | - | `{0: 1}` | - | 0 | `{0: 1}` |
| **1** | 1 | -2 | `{0: 1}` | 0 | 0 | `{0:1, 1:1}` |
| **2** | 3 | 0 | `{0:1, 1:1}` | 1 | 1 | `{0:1, 1:1, 3:1}` |
| **1** | 4 | 1 | `{0:1, 1:1, 3:1}` | 1 | 2 | `{0:1, 1:1, 3:1, 4:1}` |
| **2** | 6 | 3 | `{0:1, 1:1, 3:1, 4:1}` | 1 | 3 | `{0:1, 1:1, 3:1, 4:1, 6:1}` |
| **1** | 7 | 4 | `{0:1, 1:1, 3:1, 4:1, 6:1}` | 1 | 4 | `{0:1, 1:1, 3:1, 4:1, 6:1, 7:1}` |

My previous manual trace of the `count` map update was incorrect. The logic of the code is sound. Let's re-verify the last two steps with the correct `count` update.

  * **Iteration 4 (Corrected): `num = 2`**

      * `prefix_sum` is `6`. Target is `3`. `count.get(3, 0)` is `1`. `res` becomes `3`.
      * `count[6] = count.get(6, 0) + 1` -\> `count[6]` becomes `1`.

  * **Iteration 5 (Corrected): `num = 1`**

      * `prefix_sum` is `7`. Target is `4`. `count.get(4, 0)` is `1`. `res` becomes `4`.
      * `count[7] = count.get(7, 0) + 1` -\> `count[7]` becomes `1`.

The final result is indeed `4`.

-----

### 3\. Final Return

```python
        return res
```

  * The loop finishes.
  * The final value of `res` is **4**, which is the correct number of subarrays.