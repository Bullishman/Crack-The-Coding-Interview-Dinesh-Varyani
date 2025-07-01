# 2. Longest Substring Without Repeating Characters

**Difficulty**: Medium

**Topics**: Hash Table, String, Sliding Window

**Link**: https://leetcode.com/problems/longest-substring-without-repeating-characters

Of course. This code solves the "Longest Substring Without Repeating Characters" problem using an efficient algorithm known as the **Sliding Window** technique, optimized with a hash map (a dictionary).

### The Core Idea

The algorithm maintains a "window" (a substring) defined by a `left` pointer (`l`) and a `right` pointer (`r`).

1.  The `right` pointer (`r`) expands the window by moving forward through the string one character at a time.
2.  A `seen` dictionary is used to keep track of the most recent index of each character we have encountered.
3.  If we encounter a character that is already in our `seen` map (a duplicate), it means we have a repeat. To fix this, we must shrink our window from the left by moving the `l` pointer forward to just after the previous occurrence of that character.
4.  At each step, we calculate the size of the current valid window and update our maximum length found so far.

Let's break down the code line by line with an example.

**Example:** `s = "tmmzuxt"`
**Expected Result:** `5` (The longest substring without repeating characters is `"mzuxt"`).

-----

### **Initial Setup**

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
```

This defines the main function.

```python
        seen = {}
        l, mx = 0, 0
```

  * `seen = {}`: An empty dictionary is created. It will store `character -> last_seen_index` mappings.
  * `l = 0`: The `left` pointer of our sliding window. It starts at the beginning of the string.
  * `mx = 0`: The `max` length found so far. It starts at 0.

-----

### **The Main Loop (Expanding the Window)**

```python
        for r, c in enumerate(s):
```

  * This loop iterates through the string `s`, giving us both the index `r` (our **right pointer**) and the character `c` at that position. This loop is responsible for expanding our window to the right.

-----

### **Inside the Loop**

#### **Step 1: Check for Duplicates and Shrink the Window**

```python
            if c in seen:
                l = max(l, seen[c] + 1)
```

  * **`if c in seen:`**: This checks if the current character `c` has been seen before. If it has, we have a repeat.
  * **`l = max(l, seen[c] + 1)`**: This is the crucial window-shrinking logic.
      * `seen[c]`: This gives us the index where we *last* saw the character `c`.
      * `seen[c] + 1`: To form a valid window, our new `left` boundary must be *after* this last occurrence.
      * `max(l, ...)`: This is a subtle but important part. We only want to move our left pointer `l` forward. It's possible we've already moved `l` past the last occurrence of `c` due to another, more recent duplicate. This `max` ensures `l` never moves backward.

#### **Step 2: Update the Character's Last Seen Position**

```python
            seen[c] = r
```

  * Regardless of whether the character was a duplicate or not, we now update its entry in the `seen` map to the current index `r`. This ensures the map always holds the most recent position of each character.

#### **Step 3: Update the Maximum Length**

```python
            mx = max(mx, r - l + 1)
```

  * `r - l + 1`: This calculates the length of the current valid window.
  * `max(mx, ...)`: We compare the length of the current window to our overall maximum `mx` and keep the larger one.

-----

### **Final Return**

```python
        return mx
```

After the loop has processed the entire string, `mx` will hold the length of the longest substring found, and we return it.

-----

### **Live Trace Table Map for `s = "tmmzuxt"`**

| `r` | `c` | `seen` (at start of loop) | `c` in `seen`? | Action on `l` | `l` | `Window s[l:r+1]` | `Length r-l+1` | `mx` |
|:---:|:---:|:--- |:---:|:---|:---:|:---|:---:|:---:|
| 0 | 't' | `{}` | No | - | 0 | `"t"` | 1 | 1 |
| 1 | 'm' | `{'t': 0}` | No | - | 0 | `"tm"` | 2 | 2 |
| 2 | 'm' | `{'t': 0, 'm': 1}` | Yes | `l = max(0, seen['m']+1) = max(0, 2) = 2` | 2 | `"m"` | 1 | 2 |
| 3 | 'z' | `{'t': 0, 'm': 2}` | No | - | 2 | `"mz"` | 2 | 2 |
| 4 | 'u' | `{..., 'z': 3}` | No | - | 2 | `"mzu"` | 3 | 3 |
| 5 | 'x' | `{..., 'u': 4}` | No | - | 2 | `"mzux"` | 4 | 4 |
| 6 | 't' | `{..., 'x': 5}` | Yes | `l = max(2, seen['t']+1) = max(2, 1) = 2` | 2 | `"mzuxt"`| 5 | **5** |

**Final `seen` map:** `{'t': 6, 'm': 2, 'z': 3, 'u': 4, 'x': 5}`
The function returns `mx`, which is **5**.