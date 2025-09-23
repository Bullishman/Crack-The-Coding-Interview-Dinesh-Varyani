# 128. Palindrome Partitioning

**Difficulty**: Medium

**Topics**: String, Dynamic Programming, Backtracking

**Link**: https://leetcode.com/problems/palindrome-partitioning

Of course. Let's break down this code for the "Palindrome Partitioning" problem.

### The Logic: Iterative Backtracking (DFS)

This code finds all possible ways to partition a string such that every substring in the partition is a palindrome. Instead of using recursion, which is a common way to solve this, this implementation uses an explicit **stack** (`lst`) to perform an iterative Depth-First Search (DFS).

The core idea is to build partitions step-by-step. The stack stores the "state" of our search, which consists of two things:

1.  The list of palindromes found so far for the current path (e.g., `["a", "a"]`).
2.  The starting index in the original string for finding the *next* palindrome.

### The Example

We will use the string `s = "aab"` to trace the execution. The expected output is `[["a", "a", "b"], ["aa", "b"]]`. Let's see how the code finds these two valid partitions.

-----

### Code and Live Demonstration

#### 1\. Initialization

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # s = "aab"
        partitions, lst, l = [], [([], 0)], len(s)
```

  * `partitions = []`: This list will store our final results (the complete, valid partitions).
  * `lst = [([], 0)]`: This is our stack. We initialize it with one tuple: `([], 0)`. This represents our starting state: "We have an empty partition `[]`, and we need to start looking for palindromes from index `0` of the string `s`."
  * `l = len(s)`: `l` becomes `3`.

-----

### **Live Trace Table Map**

This table will track the state of our stack (`lst`) and our final `partitions` list throughout the execution.

| Loop Iteration | Action on `lst` (Stack) | Current `pals` & `i` | `j` | `sub = s[i:j]` | `sub` is Palindrome? | Action on `lst` / `partitions` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | `[ ([], 0) ]` | | | | | |
| **1** | **Pop** `([], 0)` | `pals = []`, `i = 0`| | | | Stack is now empty. |
| | | | 1 | `"a"` | **Yes** | **Push** `(["a"], 1)` onto stack. |
| | | | 2 | `"aa"`| **Yes** | **Push** `(["aa"], 2)` onto stack. |
| | | | 3 | `"aab"`| No | Do nothing. |
| | **End of Iter. 1** | `lst` is `[ (["a"], 1), (["aa"], 2) ]` | | | | |
| **2** | **Pop** `(["aa"], 2)` | `pals=["aa"]`, `i=2`| | | | Stack is now `[(["a"], 1)]`. |
| | | | 3 | `"b"` | **Yes** | `j == l`. A full partition found\! **Add `["aa", "b"]` to `partitions`**. |
| | **End of Iter. 2** | `partitions` is `[ ["aa", "b"] ]` | | | | |
| **3** | **Pop** `(["a"], 1)` | `pals=["a"]`, `i=1` | | | | Stack is now empty. |
| | | | 2 | `"a"` | **Yes** | **Push** `(["a", "a"], 2)` onto stack. |
| | | | 3 | `"ab"` | No | Do nothing. |
| | **End of Iter. 3** | `lst` is `[ (["a", "a"], 2) ]` | | | | |
| **4** | **Pop** `(["a", "a"], 2)` | `pals=["a","a"]`, `i=2`| | | | Stack is now empty. |
| | | | 3 | `"b"` | **Yes** | `j == l`. A full partition found\! **Add `["a", "a", "b"]` to `partitions`**. |
| | **End of Iter. 4** | `partitions` is `[ ["aa", "b"], ["a", "a", "b"] ]` | | | | |
| **5** | Stack is empty. | `while lst:` condition is false. Loop terminates. | | | | |

-----

### **Detailed Line-by-Line Breakdown**

#### Main Loop (`while lst:`)

The loop runs as long as there are potential partitions to explore in our stack.

**Iteration 1:**

  * `pals, i = lst.pop()` -\> `pals` is `[]`, `i` is `0`. The stack is now empty.
  * **Inner loop** `for j in range(1, 4)`:
      * `j=1`: `sub = s[0:1]` is `"a"`. It's a palindrome. `j != l`, so we **push a new state** onto the stack: `lst.append((["a"], 1))`. This means "we found `a`, now find more palindromes starting from index 1".
      * `j=2`: `sub = s[0:2]` is `"aa"`. It's a palindrome. `j != l`, so we **push another state**: `lst.append((["aa"], 2))`. This means "we found `aa`, now find more palindromes starting from index 2".
      * `j=3`: `sub = s[0:3]` is `"aab"`. Not a palindrome.
  * At the end of this iteration, the stack is `[(["a"], 1), (["aa"], 2)]`.

**Iteration 2:**

  * `pals, i = lst.pop()` -\> `pals` is `["aa"]`, `i` is `2`. (Stacks are Last-In, First-Out).
  * **Inner loop** `for j in range(3, 4)`:
      * `j=3`: `sub = s[2:3]` is `"b"`. It's a palindrome. Now, `j == l` (3 == 3) is **true**. This means we have successfully partitioned the entire string.
      * We append the complete partition to our results: `partitions.append(["aa"] + ["b"])`.
      * `partitions` is now `[["aa", "b"]]`.

**Iteration 3:**

  * `pals, i = lst.pop()` -\> `pals` is `["a"]`, `i` is `1`.
  * **Inner loop** `for j in range(2, 4)`:
      * `j=2`: `sub = s[1:2]` is `"a"`. It's a palindrome. `j != l`, so we push `lst.append((["a", "a"], 2))`.
      * `j=3`: `sub = s[1:3]` is `"ab"`. Not a palindrome.

**Iteration 4:**

  * `pals, i = lst.pop()` -\> `pals` is `["a", "a"]`, `i` is `2`.
  * **Inner loop** `for j in range(3, 4)`:
      * `j=3`: `sub = s[2:3]` is `"b"`. It's a palindrome. `j == l` is **true**. Another complete partition.
      * We append it: `partitions.append(["a", "a"] + ["b"])`.
      * `partitions` is now `[["aa", "b"], ["a", "a", "b"]]`.

**Termination:**

  * The `while` loop checks `lst` again. It's empty. The condition `while lst:` is false, and the loop terminates.

-----

### 2\. Final Return

```python
        return partitions
```

  * The function returns the final list: `[["aa", "b"], ["a", "a", "b"]]`. (Note: The order might differ, but the contents are correct).