# 153. Longest Palindromic Subsequence

**Difficulty**: Medium

**Topics**: String, Dynamic Programming

**Link**: https://leetcode.com/problems/longest-palindromic-subsequence

Of course. Let's do a detailed line-by-line breakdown of this classic dynamic programming solution for the "Longest Palindromic Subsequence" problem.

### The Logic: Dynamic Programming

The core of this solution is a 2D array (a DP table) named `dp`, where `dp[i][j]` stores the length of the longest palindromic subsequence found within the substring `s[i...j]` (inclusive of `i` and `j`).

The algorithm fills this table by considering progressively larger substrings. The final answer for the entire string `s` will be stored in `dp[0][n-1]`.

The recurrence relation (the logic for filling the table) is as follows:

1.  **Base Case:** The longest palindromic subsequence of any single character is the character itself. Therefore, `dp[i][i]` is always `1`.
2.  **Recursive Step:** To calculate `dp[i][j]` for a substring `s[i...j]`:
      * **If `s[i] == s[j]`:** The characters at the ends match. This means they can both be part of our palindrome. The length is `2` (for these two characters) plus the length of the longest palindromic subsequence of the inner string `s[i+1...j-1]`. So, `dp[i][j] = 2 + dp[i+1][j-1]`.
      * **If `s[i] != s[j]`:** The end characters don't match, so they can't both be part of the same palindrome. We must discard one of them. The longest palindromic subsequence is therefore the maximum of either the subsequence in `s[i+1...j]` (discarding `s[i]`) or the subsequence in `s[i...j-1]` (discarding `s[j]`). So, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`.

The loops iterate backward for `i` to ensure that when we calculate `dp[i][j]`, the required subproblems (`dp[i+1][j-1]`, `dp[i+1][j]`, etc.) have already been computed.

### The Example

Let's trace the execution with the string:

  * `s = "bbbab"`

The longest palindromic subsequence is `"bbbb"`, which has a length of **4**.

-----

### Code and Live Demonstration

#### 1\. Initialization

```python
        n = len(s)
        # n = 5
        dp = [[0] * n for _ in range(n)]
        # dp is a 5x5 grid of zeros.
```

  * **DP Table `dp` (Initial State):**
    ```
      j=0 1 2 3 4
    i=0 [0,0,0,0,0]
    i=1 [0,0,0,0,0]
    i=2 [0,0,0,0,0]
    i=3 [0,0,0,0,0]
    i=4 [0,0,0,0,0]
    ```

#### 2\. The Loops

The outer loop `for i in range(n)[::-1]` iterates with `i` from `4` down to `0`.

-----

### **Live Trace Table Map**

This table will show the state of the `dp` grid after each full iteration of the outer loop (`i`).

**After `i = 4` is processed:**

```
  j=0 1 2 3 4
i=0 [0,0,0,0,0]
i=1 [0,0,0,0,0]
i=2 [0,0,0,0,0]
i=3 [0,0,0,0,0]
i=4 [0,0,0,0,1]
```

**After `i = 3` is processed:**

```
  j=0 1 2 3 4
i=0 [0,0,0,0,0]
i=1 [0,0,0,0,0]
i=2 [0,0,0,0,0]
i=3 [0,0,0,1,1]
i=4 [0,0,0,0,1]
```

**After `i = 2` is processed:**

```
  j=0 1 2 3 4
i=0 [0,0,0,0,0]
i=1 [0,0,0,0,0]
i=2 [0,0,1,1,3]
i=3 [0,0,0,1,1]
i=4 [0,0,0,0,1]
```

**After `i = 1` is processed:**

```
  j=0 1 2 3 4
i=0 [0,0,0,0,0]
i=1 [0,1,2,2,3]
i=2 [0,0,1,1,3]
i=3 [0,0,0,1,1]
i=4 [0,0,0,0,1]
```

**After `i = 0` is processed (Final State):**

```
  j=0 1 2 3 4
i=0 [1,2,3,3,4]
i=1 [0,1,2,2,3]
i=2 [0,0,1,1,3]
i=3 [0,0,0,1,1]
i=4 [0,0,0,0,1]
```

-----

### **Detailed Line-by-Line Breakdown of Loops**

#### Outer Loop: `i = 4` (`s[4] = 'b'`)

  * `dp[4][4] = 1`. (Base case for the single character "b")
  * The inner loop `for j in range(5, 5)` does not run.

#### Outer Loop: `i = 3` (`s[3] = 'a'`)

  * `dp[3][3] = 1`. (Base case for "a")
  * **Inner loop `j = 4`**: Substring is `s[3...4]` which is `"ab"`.
      * `s[3]` ('a') \!= `s[4]` ('b'). The `else` block runs.
      * `dp[3][4] = max(dp[i + 1][j], dp[i][j - 1])` -\> `max(dp[4][4], dp[3][3])` -\> `max(1, 1) = 1`.

#### Outer Loop: `i = 2` (`s[2] = 'b'`)

  * `dp[2][2] = 1`. (Base case for "b")
  * **Inner loop `j = 3`**: Substring is `s[2...3]` which is `"ba"`.
      * `s[2]` ('b') \!= `s[3]` ('a').
      * `dp[2][3] = max(dp[3][3], dp[2][2])` -\> `max(1, 1) = 1`.
  * **Inner loop `j = 4`**: Substring is `s[2...4]` which is `"bab"`.
      * `s[2]` ('b') == `s[4]` ('b'). **It's a match\!** The `if` block runs.
      * `dp[2][4] = dp[i + 1][j - 1] + 2` -\> `dp[3][3] + 2` -\> `1 + 2 = 3`.

#### Outer Loop: `i = 1` (`s[1] = 'b'`)

  * `dp[1][1] = 1`.
  * **Inner loop `j = 2`**: Substring is `s[1...2]` which is `"bb"`.
      * `s[1]` ('b') == `s[2]` ('b'). **Match\!**
      * `dp[1][2] = dp[2][1] + 2`. The subproblem is for `s[2...1]`, which is an empty string between the two matching 'b's. Its value in the `dp` table is the initial `0`. So, `0 + 2 = 2`.
  * **Inner loop `j = 3`**: Substring is `s[1...3]` which is `"bba"`.
      * `s[1]` ('b') \!= `s[3]` ('a').
      * `dp[1][3] = max(dp[2][3], dp[1][2])` -\> `max(1, 2) = 2`.
  * **Inner loop `j = 4`**: Substring is `s[1...4]` which is `"bbab"`.
      * `s[1]` ('b') == `s[4]` ('b'). **Match\!**
      * `dp[1][4] = dp[2][3] + 2` -\> `1 + 2 = 3`.

#### Outer Loop: `i = 0` (`s[0] = 'b'`)

  * `dp[0][0] = 1`.
  * **Inner loop `j = 1`**: Substring is `s[0...1]` which is `"bb"`.
      * `s[0]` ('b') == `s[1]` ('b'). **Match\!**
      * `dp[0][1] = dp[1][0] + 2` -\> `0 + 2 = 2`.
  * **Inner loop `j = 2`**: Substring is `s[0...2]` which is `"bbb"`.
      * `s[0]` ('b') == `s[2]` ('b'). **Match\!**
      * `dp[0][2] = dp[1][1] + 2` -\> `1 + 2 = 3`.
  * **Inner loop `j = 3`**: Substring is `s[0...3]` which is `"bbba"`.
      * `s[0]` ('b') \!= `s[3]` ('a').
      * `dp[0][3] = max(dp[1][3], dp[0][2])` -\> `max(2, 3) = 3`.
  * **Inner loop `j = 4`**: Substring is `s[0...4]` which is `"bbbab"`.
      * `s[0]` ('b') == `s[4]` ('b'). **Match\!**
      * `dp[0][4] = dp[1][3] + 2` -\> `2 + 2 = 4`.

-----

### 3\. Final Return

```python
        return dp[0][-1]
```

  * The code returns the value at `dp[0][n-1]`, which is `dp[0][4]`.
  * From our final table, `dp[0][4]` is **4**.
  * This is the correct length of the longest palindromic subsequence ("bbbb").