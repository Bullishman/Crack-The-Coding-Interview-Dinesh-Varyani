# 29. Word Break

**Difficulty**: Medium

**Topics**: Hash Table, String, Dynamic Programming, Trie, Memoization

**Link**: https://leetcode.com/problems/word-break

Let's map this out visually. The best way to think about this code is as a **growing window**. We look at a prefix of the string, and try to see if it can be split into a "valid left part" (already solved) and a "valid right word" (in the dictionary).

### The Setup

* **Input:** `s = "catsand"`, `wordDict = ["cats", "dog", "sand", "and", "cat"]`
* **Initialization:** `dp` array of size 8 (length of "catsand" + 1).

| Index (i) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Char** | Ø | c | a | t | s | a | n | d |
| **dp[i]** | **T** | F | F | F | F | F | F | F |

---

### Step-by-Step Execution Map

| `i` (End) | `j` (Split) | Substring `s[j:i]` | Is `dp[j]` True? | In `word_set`? | Result |
| --- | --- | --- | --- | --- | --- |
| **1-2** | 0 | "c", "ca" | Yes | No | `dp[1], dp[2]` stay `False` |
| **3** | 0 | "cat" | **Yes** | **Yes** | `dp[3] = True` |
| **4** | 0 | "cats" | **Yes** | **Yes** | `dp[4] = True` |
| **5** | 0-4 | "catsa", "atsa"... | - | No | `dp[5]` stays `False` |
| **6** | 0-5 | ... | - | No | `dp[6]` stays `False` |
| **7** | **3** | "sand" | **Yes** (`dp[3]`) | **Yes** | **`dp[7] = True`** |
| **7** | **4** | "and" | **Yes** (`dp[4]`) | **Yes** | (Already True, breaks) |

---

### Line-by-Line Logic Breakdown

1. **`word_set = set(wordDict)`**
* **Why:** If you search a list of 1,000 words, it takes 1,000 steps. In a set, it takes 1 step. This line ensures the `in word_set` check doesn't slow us down.


2. **`dp = [False] * (s_len + 1)`**
* **Why:** `dp[i]` represents "Can we successfully break the string from index 0 up to index ?".


3. **`dp[0] = True`**
* **Why:** This is the "seed." To find the first word (like "cat"), we check `dp[0]` and the substring `s[0:3]`. Since `dp[0]` is True, the first word is allowed to "start."


4. **`for i in range(1, s_len + 1):`**
* We are slowly extending our view of the string, character by character.


5. **`for j in range(i):`**
* For every new length `i`, we look backward at all previous successful "break points" `j`.


6. **`if dp[j] and s[j:i] in word_set:`**
* **The logic:** "If I can successfully form a word up to point `j`, AND the remaining piece from `j` to `i` is a dictionary word, then the whole string up to `i` is valid."


7. **`dp[i] = True` then `break**`
* Once we find *one* way to make `dp[i]` valid, we stop looking at other `j` values for that `i` and move to the next character.


8. **`return dp[s_len]`**
* Our final answer is the very last cell, representing the full length of the string.



### The Final "Table Map" for "catsand":

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **String** |  | c | a | t | s | a | n | d |
| **DP Value** | **T** | F | F | **T** | **T** | F | F | **T** |

The result is **True** because `dp[7]` is True.

Would you like to see how this logic changes if we wanted to return the actual list of words used (Word Break II)?