# 103. Find All Anagrams In A String

**Difficulty**: Medium

**Topics**: Hash Table, String, Sliding Window

**Link**: https://leetcode.com/problems/find-all-anagrams-in-a-string

Of course. Let's break down this Python code for finding all anagrams of a pattern string within a larger string.

### High-Level Overview

The code aims to find all the starting indices of substrings in a string `s` that are anagrams of another string `p`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

The strategy employed here is a **brute-force sliding window**. It works as follows:

1.  **Pre-computation:** It first computes the character frequency map of the pattern string `p`. This tells us exactly which characters and how many of each an anagram must contain.
2.  **Iteration:** It then slides a window of the same length as `p` across the larger string `s`, from left to right, one character at a time.
3.  **Comparison:** In each position, it computes a new character frequency map for the current window (substring) of `s`. It then compares this window's map to the pre-computed map of `p`.
4.  **Recording:** If the two frequency maps are identical, it means the window is an anagram of `p`, and the starting index of that window is recorded.

This approach is straightforward but not the most performant, as it re-computes the frequency map for every single window.

-----

### Prerequisites: `collections.Counter`

To fully understand the code, you need to know what `collections.Counter` does.
A `Counter` is a specialized dictionary subclass for counting hashable objects. You give it an iterable (like a string), and it returns a dictionary-like object where keys are the items and values are their counts.

**Example:**

```python
from collections import Counter
p = "abc"
p_counter = Counter(p)
print(p_counter)
# Output: Counter({'a': 1, 'b': 1, 'c': 1})

s_window = "cba"
window_counter = Counter(s_window)
print(window_counter)
# Output: Counter({'c': 1, 'b': 1, 'a': 1})

# Crucially, two Counters are considered equal if they have the same keys with the same counts.
print(p_counter == window_counter)
# Output: True
```

-----

### Line-by-Line Code Explanation

Here is the code with detailed comments explaining each line.

```python
from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # Line 1: p_counter = Counter(p)
        # Create a frequency map (a Counter object) of the pattern string `p`.
        # This is done only once and will be our reference for what an anagram should look like.
        p_counter = Counter(p)
        
        # Line 2: p_len = len(p)
        # Store the length of `p`. This is the size of our sliding window.
        p_len = len(p)
        
        # Line 3: l = []
        # Initialize an empty list `l` to store the starting indices of any anagrams we find.
        l = []

        # Line 4: for i in range(len(s) - p_len + 1):
        # Start a loop that iterates through the string `s`. The variable `i` will be the
        # starting index of each potential window. The loop stops at `len(s) - p_len`
        # which is the last possible index where a full-sized window can start.
        for i in range(len(s) - p_len + 1):
            
            # Line 5: if p_counter == Counter(s[i:i+p_len]):
            # This is the core logic. For each starting index `i`:
            # 1. `s[i:i+p_len]` creates a substring (the "window") of `s` that is the same size as `p`.
            # 2. `Counter(...)` creates a brand new frequency map for that window.
            # 3. `p_counter == ...` compares the reference counter with the new window counter.
            # This check is True only if the window is an exact anagram of `p`.
            if p_counter == Counter(s[i:i+p_len]):
                
                # Line 6: l.append(i)
                # If the counters match, it means we've found an anagram.
                # We append its starting index `i` to our results list `l`.
                l.append(i)
        
        # Line 7: return l
        # After the loop has checked all possible windows, return the list `l`
        # containing all the found indices.
        return l
```

-----

### Example Walkthrough

Let's trace the code with a classic example.

  * `s = "cbaebabacd"`
  * `p = "abc"`

**Initial State before the loop:**

  * **Line 1:** `p_counter` = `Counter({'a': 1, 'b': 1, 'c': 1})`
  * **Line 2:** `p_len` = `3`
  * **Line 3:** `l` = `[]`
  * **Line 4:** The loop for `i` will run from `0` to `len("cbaebabacd") - 3 + 1 = 10 - 3 + 1 = 8`. So `i` goes from 0 to 7.

#### Live Trace Table Map

| `i` | Window `s[i:i+3]` | `Counter(window)` created in loop | Condition Check: `p_counter == Counter(window)`? | Action / State of `l`         |
| :-: | :---------------- | :-------------------------------- | :-----------------------------------------------: | :---------------------------- |
| 0   | `"cba"`           | `Counter({'c':1, 'b':1, 'a':1})`  | `True`                                            | Append `0`. `l` is now `[0]`.   |
| 1   | `"bae"`           | `Counter({'b':1, 'a':1, 'e':1})`  | `False` (contains 'e')                          | No change. `l` is `[0]`.      |
| 2   | `"aeb"`           | `Counter({'a':1, 'e':1, 'b':1})`  | `False` (contains 'e')                          | No change. `l` is `[0]`.      |
| 3   | `"eba"`           | `Counter({'e':1, 'b':1, 'a':1})`  | `False` (contains 'e')                          | No change. `l` is `[0]`.      |
| 4   | `"bab"`           | `Counter({'b':2, 'a':1})`         | `False` (counts don't match)                    | No change. `l` is `[0]`.      |
| 5   | `"aba"`           | `Counter({'a':2, 'b':1})`         | `False` (counts don't match)                    | No change. `l` is `[0]`.      |
| 6   | `"bac"`           | `Counter({'b':1, 'a':1, 'c':1})`  | `True`                                            | Append `6`. `l` is now `[0, 6]`. |
| 7   | `"acd"`           | `Counter({'a':1, 'c':1, 'd':1})`  | `False` (contains 'd')                          | No change. `l` is `[0, 6]`. |

The loop finishes.

**Final Step:**

  * **Line 7:** The function returns the final list `l`.

**Final Result:** `[0, 6]`

-----

### Complexity Analysis

  * **Time Complexity:** $O((S - P) \\times P)$, where $S$ is the length of `s` and $P$ is the length of `p`.

      * The `for` loop runs $S - P + 1$ times, which is roughly $O(S)$.
      * Inside the loop, slicing the string `s[i:i+p_len]` takes $O(P)$ time.
      * Creating a `Counter` from this slice also takes $O(P)$ time.
      * Therefore, the total time is approximately $O(S \\times P)$. This can be slow if `p` is long.

  * **Space Complexity:** $O(P)$.

      * We store `p_counter`, which holds at most $P$ unique characters.
      * Inside the loop, a temporary counter for the window is created, which also takes $O(P)$ space, but this space is reused in each iteration.

**Note on Optimization:** A more advanced "sliding window" technique can optimize the time complexity to $O(S)$. Instead of re-creating the counter for every window, it would maintain one counter for the window and intelligently update it in $O(1)$ time by adding the new character that enters the window and removing the character that leaves it.