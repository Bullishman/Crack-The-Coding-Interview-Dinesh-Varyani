# 103. Find All Anagrams In A String

**Difficulty**: Medium

**Topics**: Hash Table, String, Sliding Window

**Link**: https://leetcode.com/problems/find-all-anagrams-in-a-string

Of course. Let's break down this highly optimized solution for finding anagrams. This version represents a significant improvement over the previous brute-force approach.

### High-Level Overview

This code implements an **Optimized Sliding Window** technique. It is much more efficient than the previous solution because it avoids re-calculating the character count for every single window.

The core idea is:

1.  **Initial Window:** Create two frequency maps (using fixed-size arrays), one for the pattern `p` and one for the very first window in `s`.
2.  **First Comparison:** Check if this initial window is an anagram.
3.  **Slide and Update:** Instead of creating a new frequency map for the next window, simply "slide" the existing window one position to the right. This involves two constant-time operations:
      * Decrementing the count of the character that is **leaving** the window from the left.
      * Incrementing the count of the character that is **entering** the window from the right.
4.  **Compare at Each Step:** After each slide, compare the updated window's frequency map with the pattern's map. If they match, record the starting index.

This approach ensures that each character in the string `s` is processed only a constant number of times, leading to a linear time complexity.

-----

### Prerequisites: Array as a Frequency Map

This code uses a simple array of size 26 as a frequency map for the 26 lowercase English letters. The key to this is the `ord()` function, which gives the ASCII/Unicode value of a character.

  * `ord('a')` is 97.
  * `ord('b')` is 98.
  * `ord('c')` is 99, and so on.

By calculating `ord(char) - ord('a')`, we can map each character to a unique array index:

  * `ord('a') - ord('a')` -\> `97 - 97` = `0`
  * `ord('b') - ord('a')` -\> `98 - 97` = `1`
  * `ord('c') - ord('a')` -\> `99 - 97` = `2`

So, `freq[0]` stores the count of 'a's, `freq[1]` stores the count of 'b's, and so on.

-----

### Line-by-Line Code Explanation

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Line 1: s_len, p_len = len(s), len(p)
        # Store the lengths of the strings for efficiency.
        s_len, p_len = len(s), len(p)

        # Line 2: if s_len < p_len:
        # An anagram is impossible if the main string is shorter than the pattern.
        if s_len < p_len:
            # Line 3: return []
            # Return an empty list immediately in this edge case.
            return []

        # Line 4: freq_p, freq_s = [0] * 26, [0] * 26
        # Initialize two frequency map arrays, one for `p` and one for the window in `s`.
        # Each is an array of 26 zeros, for 'a' through 'z'.
        freq_p, freq_s = [0] * 26, [0] * 26

        # This first loop populates the maps for the pattern `p` and the INITIAL window in `s`.
        # Line 5: for i in range(p_len):
        for i in range(p_len):
            # Line 6: freq_s[ord(s[i]) - ord('a')] += 1
            # Increment the count for the character s[i] in the window's frequency map.
            freq_s[ord(s[i]) - ord('a')] += 1
            # Line 7: freq_p[ord(p[i]) - ord('a')] += 1
            # Increment the count for the character p[i] in the pattern's frequency map.
            freq_p[ord(p[i]) - ord('a')] += 1

        # Line 8: ans = []
        # Initialize the list to store our results.
        ans = []
        
        # Line 9: if freq_p == freq_s:
        # Check if the very first window (from index 0 to p_len-1) is an anagram.
        if freq_p == freq_s:
            # Line 10: ans.append(0)
            # If so, its starting index is 0.
            ans.append(0)

        # This is the main sliding loop. It starts from where the first window ended.
        # Line 11: for i in range(p_len, s_len):
        # `i` represents the index of the NEW character ENTERING the window from the right.
        for i in range(p_len, s_len):
            # Line 12: freq_s[ord(s[i - p_len]) - ord('a')] -= 1
            # This is the "slide". Decrement the count of the character LEAVING the window
            # from the left. Its index is `i - p_len`.
            freq_s[ord(s[i - p_len]) - ord('a')] -= 1
            
            # Line 13: freq_s[ord(s[i]) - ord('a')] += 1
            # Increment the count of the new character ENTERING the window from the right.
            freq_s[ord(s[i]) - ord('a')] += 1

            # Line 14: if freq_p == freq_s:
            # After sliding, check if the new window's frequency map matches the pattern's.
            if freq_p == freq_s:
                # Line 15: ans.append(i - p_len + 1)
                # If they match, the current window is an anagram. Its starting index
                # is `i - p_len + 1`. Append this index to the answer.
                ans.append(i - p_len + 1)

        # Line 16: return ans
        # Return the final list of indices.
        return ans
```

-----

### Example Walkthrough

Let's use the same example to highlight the difference in approach.

  * `s = "cbaebabacd"`
  * `p = "abc"`

**Initial State:**

  * `s_len = 10`, `p_len = 3`
  * `freq_p` = `[0, 0, ..., 0]` (26 zeros)
  * `freq_s` = `[0, 0, ..., 0]` (26 zeros)

#### Live Trace Table Map

**Phase 1: Populating the Initial Window** (Lines 5-7)

This loop runs for `i` in `range(3)`, so `i = 0, 1, 2`.

| `i` | `s[i]` | `p[i]` | Action on `freq_s` | Action on `freq_p` |
| :-: | :----: | :----: | :----------------- | :----------------- |
| 0   | 'c'    | 'a'    | `freq_s[2]` becomes 1 | `freq_p[0]` becomes 1 |
| 1   | 'b'    | 'b'    | `freq_s[1]` becomes 1 | `freq_p[1]` becomes 1 |
| 2   | 'a'    | 'c'    | `freq_s[0]` becomes 1 | `freq_p[2]` becomes 1 |

**State after Phase 1:**

  * `freq_p` represents `{'a':1, 'b':1, 'c':1}`. The array is `[1, 1, 1, 0, ..., 0]`.
  * `freq_s` represents `{'c':1, 'b':1, 'a':1}`. The array is `[1, 1, 1, 0, ..., 0]`.
  * `ans` = `[]`

**Phase 2: Initial Check** (Lines 9-10)

| Line \# | Condition `freq_p == freq_s` | Action / State of `ans` |
| :----: | :--------------------------- | :---------------------- |
| 9      | `True`                       | Append `0`. `ans` is `[0]`. |

**Phase 3: Sliding the Window** (Lines 11-15)

This loop runs for `i` in `range(3, 10)`, so `i = 3, 4, ..., 9`.

| `i` | Entering Char `s[i]` | Leaving Char `s[i-3]` | Action on `freq_s`                      | `freq_s` (Conceptual)           | `freq_p == freq_s`? | State of `ans` |
| :-: | :------------------- | :-------------------- | :-------------------------------------- | :------------------------------ | :------------------ | :------------- |
| 3   | 'e'                  | 'c'                   | Decrement 'c', Increment 'e'            | `{'a':1, 'b':1, 'e':1}`         | `False`             | `[0]`          |
| 4   | 'b'                  | 'b'                   | Decrement 'b', Increment 'b' (no change) | `{'a':1, 'b':1, 'e':1}`         | `False`             | `[0]`          |
| 5   | 'a'                  | 'a'                   | Decrement 'a', Increment 'a' (no change) | `{'a':1, 'b':1, 'e':1}`         | `False`             | `[0]`          |
| 6   | 'b'                  | 'e'                   | Decrement 'e', Increment 'b'            | `{'a':1, 'b':2}`                | `False`             | `[0]`          |
| 7   | 'a'                  | 'b'                   | Decrement 'b', Increment 'a'            | `{'a':2, 'b':1}`                | `False`             | `[0]`          |
| 8   | 'c'                  | 'a'                   | Decrement 'a', Increment 'c'            | `{'a':1, 'b':1, 'c':1}`         | `True`              | `[0, 6]`       |
| 9   | 'd'                  | 'b'                   | Decrement 'b', Increment 'd'            | `{'a':1, 'c':1, 'd':1}`         | `False`             | `[0, 6]`       |

The loop finishes.

**Final Step:**

  * **Line 16:** The function returns the final list `ans`.

**Final Result:** `[0, 6]`

### Complexity Analysis

  * **Time Complexity:** $O(S+P)$, where $S$ is the length of `s` and $P$ is the length of `p`. This is simplified to $O(S)$ since $S \\ge P$.
      * The initial population of the frequency maps takes $O(P)$ time.
      * The sliding window loop runs $S - P$ times, and each step inside the loop is $O(1)$ (just two array modifications and a comparison). This part takes $O(S-P)$ time.
      * The total is $O(P + S - P) = O(S)$, which is linear time and a major improvement.
  * **Space Complexity:** $O(1)$.
      * The space used by `freq_p` and `freq_s` is constant because the size is fixed at 26, regardless of the input string lengths. This is highly efficient.