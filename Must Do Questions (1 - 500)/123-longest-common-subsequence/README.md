# 123. Longest Common Subsequence

**Difficulty**: Medium

**Topics**: String, Dynamic Programming

**Link**: https://leetcode.com/problems/longest-common-subsequence

Of course. This code also calculates the Longest Common Subsequence (LCS), but it uses a very different and less common approach than the standard DP method.

Let's break it down. The core idea is to first filter both strings to only keep characters that appear in both, and then run a specialized DP algorithm on these shorter, filtered lists.

### The Example

To properly demonstrate the logic, especially how it handles repeated characters, let's use a more complex example:

  * `text1 = "AGGTAB"`
  * `text2 = "GXTXAYB"`

The longest common subsequence is `"GTAB"`, and its length is **4**. We will trace how the code arrives at this answer.

-----

### Code and Live Demonstration

#### 1\. Find Character Intersection

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1 = "AGGTAB", text2 = "GXTXAYB"
        intersection = set(text1) & set(text2)
```

  * First, we convert both strings to sets to find their common characters.
  * `set(text1)` becomes `{'A', 'G', 'T', 'B'}`.
  * `set(text2)` becomes `{'G', 'X', 'T', 'A', 'Y', 'B'}`.
  * The intersection `&` of these two sets is calculated.
  * **Result:** `intersection` is `{'A', 'G', 'B', 'T'}`.

#### 2\. Handle Edge Case

```python
        if len(intersection) == 0:
            return 0
```

  * `len(intersection)` is 4.
  * The condition `4 == 0` is **false**.
  * **Action:** We proceed. This is an optimization for cases where no common characters exist.

#### 3\. Filter the Original Strings

```python
        lst_t1 = [char for char in text1 if char in intersection]
        lst_t2 = [char for char in text2 if char in intersection]
```

  * This is the most important pre-processing step. We create new lists from the original strings, keeping the original order but only including characters from our `intersection` set.
  * `text1` ("AGGTAB") becomes `['A', 'G', 'G', 'T', 'A', 'B']`.
  * `text2` ("GXTXAYB") becomes `['G', 'T', 'A', 'B']`.
  * The problem is now reduced to finding the LCS of these two new lists.

#### 4\. Initialize DP Array

```python
        dp = [0] * len(lst_t2)
```

  * The DP array is sized based on the filtered `lst_t2`. `len(lst_t2)` is 4.
  * **Initial State:** `dp` is `[0, 0, 0, 0]`.

-----

### **Live Trace Table Map**

This algorithm is more complex to trace. The variable `cnt` is reset for each character in `lst_t1`. It keeps track of the length of a subsequence we could "extend" from.

#### **`i = 0`** (Processing `lst_t1[0]`, which is `'A'`)

  * `cnt` is reset to `0`.

| j | `lst_t2[j]` | `dp[j] > cnt`? | Update `cnt`? | `lst_t1[i] == lst_t2[j]`? | Update `dp[j]`? | `dp` State |
|---|---|---|---|---|---|---|
| 0 | `'G'` | `0 > 0` (F) | No | `'A'=='G'` (F) | No | `[0,0,0,0]` |
| 1 | `'T'` | `0 > 0` (F) | No | `'A'=='T'` (F) | No | `[0,0,0,0]` |
| 2 | `'A'` | `0 > 0` (F) | No | `'A'=='A'` (T) | `dp[2] = cnt + 1 = 1` | `[0,0,1,0]` |
| 3 | `'B'` | `0 > 0` (F) | No | `'A'=='B'` (F) | No | `[0,0,1,0]` |

End of outer loop for `i=0`. `dp` is `[0, 0, 1, 0]`.

-----

#### **`i = 1`** (Processing `lst_t1[1]`, which is `'G'`)

  * `cnt` is reset to `0`.

| j | `lst_t2[j]` | `dp[j] > cnt`? | Update `cnt`? | `lst_t1[i] == lst_t2[j]`? | Update `dp[j]`? | `dp` State |
|---|---|---|---|---|---|---|
| 0 | `'G'` | `0 > 0` (F) | No | `'G'=='G'` (T) | `dp[0] = cnt + 1 = 1` | `[1,0,1,0]` |
| 1 | `'T'` | `0 > 0` (F) | No | `'G'=='T'` (F) | No | `[1,0,1,0]` |
| 2 | `'A'` | `1 > 0` (T) | `cnt = dp[2] = 1` | `'G'=='A'` (F) | No | `[1,0,1,0]` |
| 3 | `'B'` | `0 > 1` (F) | No | `'G'=='B'` (F) | No | `[1,0,1,0]` |

End of outer loop for `i=1`. `dp` is `[1, 0, 1, 0]`.

-----

#### **`i = 2`** (Processing `lst_t1[2]`, which is `'G'`)

  * `cnt` is reset to `0`.

| j | `lst_t2[j]` | `dp[j] > cnt`? | Update `cnt`? | `lst_t1[i] == lst_t2[j]`? | Update `dp[j]`? | `dp` State |
|---|---|---|---|---|---|---|
| 0 | `'G'` | `1 > 0` (T) | `cnt = dp[0] = 1` | `'G'=='G'` (T) | `dp[0] = cnt + 1 = 2` (Incorrect logic) | `[1,0,1,0]` |

Wait, there's a subtlety here. The conditions are `if... elif`. Let's re-trace `i=2, j=0` carefully.

  * `lst_t1[2]` is `'G'`, `lst_t2[0]` is `'G'`. `cnt` is `0`.
  * Check `if dp[0] > cnt`: `1 > 0` is **True**.
  * **Action:** `cnt` becomes `1`. The `elif` is **skipped**.
  * Let's refine the table to show the logic more accurately.

**Corrected Trace for `i = 2`**:

  * `cnt` is reset to `0`.

| j | `lst_t2[j]` | Logic Step-by-Step | `cnt` State | `dp` State |
|---|---|---|---|---|
| 0 | `'G'` | `if dp[0] > cnt` (`1 > 0`) is **True**, so `cnt` becomes `1`. The `elif` is skipped. | `1` | `[1,0,1,0]` |
| 1 | `'T'` | `if dp[1] > cnt` (`0 > 1`) is False. `elif 'G'=='T'` is False. No change. | `1` | `[1,0,1,0]` |
| 2 | `'A'` | `if dp[2] > cnt` (`1 > 1`) is False. `elif 'G'=='A'` is False. No change. | `1` | `[1,0,1,0]` |
| 3 | `'B'` | `if dp[3] > cnt` (`0 > 1`) is False. `elif 'G'=='B'` is False. No change. | `1` | `[1,0,1,0]` |

End of outer loop for `i=2`. `dp` is `[1, 0, 1, 0]`. (No change this round).

-----

#### **`i = 3`** (Processing `lst_t1[3]`, which is `'T'`)

  * `cnt` is reset to `0`.

| j | `lst_t2[j]` | Logic Step-by-Step | `cnt` State | `dp` State |
|---|---|---|---|---|
| 0 | `'G'` | `if dp[0] > cnt` (`1 > 0`) is **True**, so `cnt` becomes `1`. `elif` skipped. | `1` | `[1,0,1,0]` |
| 1 | `'T'` | `if dp[1] > cnt` (`0 > 1`) is False. `elif 'T'=='T'` is **True**, so `dp[1] = cnt + 1 = 2`. | `1` | `[1,2,1,0]` |
| 2 | `'A'` | `if dp[2] > cnt` (`1 > 1`) is False. `elif 'T'=='A'` is False. No change. | `1` | `[1,2,1,0]` |
| 3 | `'B'` | `if dp[3] > cnt` (`0 > 1`) is False. `elif 'T'=='B'` is False. No change. | `1` | `[1,2,1,0]` |

End of outer loop for `i=3`. `dp` is `[1, 2, 1, 0]`.

-----

#### **`i = 4`** (Processing `lst_t1[4]`, which is `'A'`)

  * `cnt` is reset to `0`.

| j | `lst_t2[j]` | Logic Step-by-Step | `cnt` State | `dp` State |
|---|---|---|---|---|
| 0 | `'G'` | `if dp[0] > cnt` (`1 > 0`) is **True**, so `cnt` becomes `1`. `elif` skipped. | `1` | `[1,2,1,0]` |
| 1 | `'T'` | `if dp[1] > cnt` (`2 > 1`) is **True**, so `cnt` becomes `2`. `elif` skipped. | `2` | `[1,2,1,0]` |
| 2 | `'A'` | `if dp[2] > cnt` (`1 > 2`) is False. `elif 'A'=='A'` is **True**, so `dp[2] = cnt + 1 = 3`. | `2` | `[1,2,3,0]` |
| 3 | `'B'` | `if dp[3] > cnt` (`0 > 2`) is False. `elif 'A'=='B'` is False. No change. | `2` | `[1,2,3,0]` |

End of outer loop for `i=4`. `dp` is `[1, 2, 3, 0]`.

-----

#### **`i = 5`** (Processing `lst_t1[5]`, which is `'B'`)

  * `cnt` is reset to `0`.

| j | `lst_t2[j]` | Logic Step-by-Step | `cnt` State | `dp` State |
|---|---|---|---|---|
| 0 | `'G'` | `if dp[0] > cnt` (`1 > 0`) is **True**, so `cnt` becomes `1`. `elif` skipped. | `1` | `[1,2,3,0]` |
| 1 | `'T'` | `if dp[1] > cnt` (`2 > 1`) is **True**, so `cnt` becomes `2`. `elif` skipped. | `2` | `[1,2,3,0]` |
| 2 | `'A'` | `if dp[2] > cnt` (`3 > 2`) is **True**, so `cnt` becomes `3`. `elif` skipped. | `3` | `[1,2,3,0]` |
| 3 | `'B'` | `if dp[3] > cnt` (`0 > 3`) is False. `elif 'B'=='B'` is **True**, so `dp[3] = cnt + 1 = 4`. | `3` | `[1,2,3,4]` |

End of outer loop for `i=5`. `dp` is `[1, 2, 3, 4]`.

-----

#### 5\. Return Value

The loops have finished.

```python
        return max(dp)
```

  * The final state of `dp` is `[1, 2, 3, 4]`.
  * The `max()` function finds the largest value in the list.
  * The function returns **4**, which is the correct length of the longest common subsequence (`"GTAB"`).