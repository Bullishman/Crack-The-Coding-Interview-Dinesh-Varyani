# 105. Palindromic Substrings

**Difficulty**: Medium

**Topics**: String, Dynamic Programming

**Link**: https://leetcode.com/problems/palindromic-substrings

Of course. Let's break down this Dynamic Programming (DP) solution for counting palindromic substrings. This approach is quite different from the "Expand from Center" method but achieves the same time complexity.

### High-Level Overview

This code uses a technique called **Dynamic Programming** to solve the problem. The core idea is to build a solution for a large problem by reusing solutions to smaller, overlapping subproblems.

Here's the strategy:

1.  **Create a Table:** A 2D table (a list of lists), named `dp`, is created. `dp[i][j]` will store a boolean value: `True` if the substring from index `i` to `j` (inclusive) is a palindrome, and `False` otherwise.
2.  **Define the Relationship:** A key insight is that a substring `s[i:j+1]` is a palindrome if and only if two conditions are met:
      * The outer characters are the same (`s[i] == s[j]`).
      * The *inner* substring `s[i+1 : j]` is *also* a palindrome.
3.  **Fill the Table:** The code uses nested loops to fill this `dp` table. By carefully choosing the order of iteration (starting from the end of the string backwards), it ensures that when it needs to know the answer for the "inner" substring (`dp[i+1][j-1]`), that value has already been calculated.
4.  **Count as We Go:** Every time it successfully determines that `dp[i][j]` is `True`, it increments a result counter.

-----

### Line-by-Line Code Explanation

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Line 1: n, res = len(s), 0
        # Store the length of the string in `n` and initialize the result counter `res` to 0.
        n, res = len(s), 0
        
        # Line 2: dp = [[False] * n for _ in range(n)]
        # Initialize an n x n 2D list (our DP table) with all values set to `False`.
        # `dp[i][j]` will eventually be True if s[i:j+1] is a palindrome.
        dp = [[False] * n for _ in range(n)]

        # Line 3: for i in range(n - 1, -1, -1):
        # Start the outer loop for the starting index `i`. It iterates BACKWARDS
        # from the end of the string (n-1) to the beginning (0). This order is
        # crucial for the DP approach to work.
        for i in range(n - 1, -1, -1):
            
            # Line 4: for j in range(i, n):
            # Start the inner loop for the ending index `j`. It iterates FORWARDS
            # from the current start index `i` to the end of the string.
            # This ensures we always have `j >= i`.
            for j in range(i, n):
                
                # Line 5: if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                # This is the core DP logic. A substring is a palindrome if:
                # 1. `s[i] == s[j]`: The first and last characters must match.
                # 2. AND one of the following is true:
                #    a) `j - i <= 2`: The substring has length 1, 2, or 3. If the outer
                #       characters match, these are always palindromes. This is our base case.
                #    b) `dp[i + 1][j - 1]`: The inner substring is already known to be a
                #       palindrome (we look up its value in our table).
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    
                    # Line 6: dp[i][j] = True
                    # If the conditions are met, we mark this substring in our table as a palindrome.
                    dp[i][j] = True
                    
                    # Line 7: res += 1
                    # And we increment our result counter.
                    res += 1

        # Line 8: return res
        # After filling the table, return the total count.
        return res
```

-----

### Example Walkthrough

Let's trace this with a great example: `s = "babad"`.
The palindromes are: "b", "a", "b", "a", "d", "bab", "aba". The total should be 7.

**Initial State:**

  * `n = 5`, `res = 0`
  * `dp` is a 5x5 grid of `False`.

#### Live Trace Table Map (Filling the `dp` Table)

We will show the state of the `dp` table after each full iteration of the outer loop (`i`). The loops fill the table diagonally from the bottom right to the top left.

**After `i = 4`** (`j` goes from 4 to 4)

  * `i=4, j=4`: `s[4]=='d'`. Substring is "d". `s[4]==s[4]` is True. `j-i = 0 <= 2` is True.
      * `dp[4][4]` becomes `True`. `res` becomes `1`.

<!-- end list -->

```
dp Table:
  j=0 1 2 3 4
i=0[F,F,F,F,F]
i=1[F,F,F,F,F]
i=2[F,F,F,F,F]
i=3[F,F,F,F,F]
i=4[F,F,F,F,T]   res = 1
```

**After `i = 3`** (`j` goes from 3 to 4)

  * `i=3, j=3`: Substring "a". `s[3]==s[3]`. Length 1 (`j-i=0`). `dp[3][3]=True`. `res=2`.
  * `i=3, j=4`: Substring "ad". `s[3]!=s[4]`. `dp[3][4]=False`.

<!-- end list -->

```
dp Table:
  j=0 1 2 3 4
i=0[F,F,F,F,F]
i=1[F,F,F,F,F]
i=2[F,F,F,F,F]
i=3[F,F,F,T,F]
i=4[F,F,F,F,T]   res = 2
```

**After `i = 2`** (`j` goes from 2 to 4)

  * `i=2, j=2`: Substring "b". Length 1. `dp[2][2]=True`. `res=3`.
  * `i=2, j=3`: Substring "ba". `s[2]!=s[3]`. `dp[2][3]=False`.
  * `i=2, j=4`: Substring "bad". `s[2]!=s[4]`. `dp[2][4]=False`.

<!-- end list -->

```
dp Table:
  j=0 1 2 3 4
i=0[F,F,F,F,F]
i=1[F,F,F,F,F]
i=2[F,F,T,F,F]
i=3[F,F,F,T,F]
i=4[F,F,F,F,T]   res = 3
```

**After `i = 1`** (`j` goes from 1 to 4)

  * `i=1, j=1`: Substring "a". Length 1. `dp[1][1]=True`. `res=4`.
  * `i=1, j=2`: Substring "ab". `s[1]!=s[2]`. `dp[1][2]=False`.
  * `i=1, j=3`: Substring "aba". `s[1]==s[3]`. Inner substring is `s[2:3]` ("b"), which is `dp[2][2]`. We look up `dp[2][2]`, it's `True`. So, `dp[1][3]=True`. `res=5`.
  * `i=1, j=4`: Substring "abad". `s[1]!=s[4]`. `dp[1][4]=False`.

<!-- end list -->

```
dp Table:
  j=0 1 2 3 4
i=0[F,F,F,F,F]
i=1[F,T,F,T,F]
i=2[F,F,T,F,F]
i=3[F,F,F,T,F]
i=4[F,F,F,F,T]   res = 5
```

**After `i = 0`** (`j` goes from 0 to 4)

  * `i=0, j=0`: Substring "b". Length 1. `dp[0][0]=True`. `res=6`.
  * `i=0, j=1`: Substring "ba". `s[0]!=s[1]`. `dp[0][1]=False`.
  * `i=0, j=2`: Substring "bab". `s[0]==s[2]`. Inner substring is `s[1:2]` ("a"), which is `dp[1][1]`. We look up `dp[1][1]`, it's `True`. So, `dp[0][2]=True`. `res=7`.
  * `i=0, j=3`: Substring "baba". `s[0]!=s[3]`. `dp[0][3]=False`.
  * `i=0, j=4`: Substring "babad". `s[0]!=s[4]`. `dp[0][4]=False`.

<!-- end list -->

```
Final dp Table:
  j=0 1 2 3 4
i=0[T,F,T,F,F]
i=1[F,T,F,T,F]
i=2[F,F,T,F,F]
i=3[F,F,F,T,F]
i=4[F,F,F,F,T]   res = 7
```

**Final Result:** The function returns `res`, which is `7`.

### Complexity Analysis

  * **Time Complexity:** $O(N^2)$, where $N$ is the length of the string `s`.
      * We have two nested loops that together iterate over the upper triangle of an $N \\times N$ grid. This results in approximately $N^2/2$ iterations.
      * The work inside each loop is $O(1)$ (a few comparisons and a table lookup).
      * Therefore, the total time complexity is $O(N^2)$.
  * **Space Complexity:** $O(N^2)$.
      * The primary space usage comes from the `dp` table, which is an $N \\times N$ grid. This makes it more space-intensive than the "Expand from Center" method, which uses $O(1)$ space.