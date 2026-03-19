# 7. Longest Palindromic Substring

**Difficulty**: Medium

**Topics**: String, Dynamic Programming

**Link**: https://leetcode.com/problems/longest-palindromic-substring

Of course. This code solves the "Longest Palindromic Substring" problem using the efficient and intuitive **"Expand Around Center"** algorithm.

### The Core Idea

A palindrome is a string that is symmetrical around its center. The center can be a single character (for odd-length palindromes like "r**a**cecar") or the space between two identical characters (for even-length palindromes like "a**bb**a").

This algorithm iterates through every possible center in the string and "expands" outwards to find the longest palindrome for that center. It keeps track of the longest one found overall.

Let's break down the code line by line with an example.

**Example:** `s = "babad"`
**Expected Result:** `"bab"` (or `"aba"`, which is also a valid longest palindrome).

-----

### The `expand` Helper Function

This function is the engine of the algorithm. It finds the longest palindrome for a given center.

```python
        # Helper function to expand from a center and find the longest palindrome.
        def expand(l: int, r: int) -> str:
```

  * **What it does:** Defines a helper function that takes a left (`l`) and right (`r`) pointer. These pointers define the starting "center". For an odd-length palindrome, `l` and `r` will be the same. For an even-length one, `r` will be `l + 1`.

<!-- end list -->

```python
            # Expand as long as pointers are in bounds and characters match.
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
```

  * This `while` loop is the expansion step. It continues as long as:
    1.  The pointers have not gone off the edges of the string (`0 <= l and r < len(s)`).
    2.  The characters at the left and right pointers are the same (`s[l] == s[r]`).
  * `l -= 1` and `r += 1`: The window expands outwards.

<!-- end list -->

```python
            # When the loop ends, l and r are one position outside the palindrome.
            # Return the slice s[l+1:r] to get the actual palindrome.
            return s[l + 1:r]
```

  * When the loop breaks, `l` and `r` are one step *past* the boundaries of the actual palindrome.
  * **For example:** If we expand around the 'a' in "b**a**bad", the loop will stop when `l = -1` and `r = 3`. The palindrome is `"bab"`, which is the slice `s[l+1 : r]` or `s[0:3]`. This return statement correctly extracts the found palindrome.

-----

### The `longestPalindrome` (Outer) Function

```python
        # A quick optimization: if the string is short or already a palindrome, return it.
        if len(s) < 2 or s == s[::-1]:
            return s
```

  * This is a simple optimization. If the string is too short to have a palindrome of length \> 1, or if the whole string is already a palindrome, we can return the answer immediately. Our example `"babad"` doesn't trigger this.

<!-- end list -->

```python
        result = ''
```

  * Initializes an empty string `result` which will be updated to always hold the longest palindrome we've found so far.

<!-- end list -->

```python
        # Iterate through every character of the string.
        for i in range(len(s)):
```

  * This is the main loop that iterates through every index `i`. We will treat each `i` as a potential center point.

<!-- end list -->

```python
            # Find the longest odd-length palindrome with center at i.
            # Find the longest even-length palindrome with center between i and i+1.
            odd_palindrome = expand(i, i)
            even_palindrome = expand(i, i + 1)
```

  * For each index `i`, we check **both** possibilities:
    1.  `odd_palindrome = expand(i, i)`: Checks for an odd-length palindrome centered on the character `s[i]`.
    2.  `even_palindrome = expand(i, i + 1)`: Checks for an even-length palindrome centered between `s[i]` and `s[i+1]`.

<!-- end list -->

```python
            # Keep the longest string found so far.
            # max() with a key=len correctly compares the strings by their length.
            result = max(result, odd_palindrome, even_palindrome, key=len)
```

  * This is a concise way to update our answer. It finds the longest string among the three candidates: our `result` so far, the new `odd_palindrome`, and the new `even_palindrome`.
  * `key=len`: This special argument tells the `max()` function to compare the items based on their **length**, not their alphabetical value.

<!-- end list -->

```python
        return result
```

  * After the loop has checked all possible centers, `result` holds the longest palindromic substring, which is returned.

-----

### Live Trace Table Map for `s = "babad"`

| `i` | Center Index | `odd_palindrome` (`expand(i, i)`) | `even_palindrome` (`expand(i, i+1)`) | `result` (before `max`) | `result` (after `max`) |
|:---:|:---|:---|:---|:---|:---|
| - | Initial State | - | - | - | `''` |
| **0** | `b` (index 0) | `"b"` | `""` | `''` | `"b"` |
| **1** | `a` (index 1) | `"bab"` | `"aba"` | `"b"` | `"bab"` |
| **2** | `b` (index 2) | `"b"` | `""` | `"bab"` | `"bab"` |
| **3** | `a` (index 3) | `"a"` | `""` | `"bab"` | `"bab"` |
| **4** | `d` (index 4) | `"d"` | `""` (out of bounds) | `"bab"` | `"bab"` |

The loop finishes. The final returned value is **`"bab"`**.