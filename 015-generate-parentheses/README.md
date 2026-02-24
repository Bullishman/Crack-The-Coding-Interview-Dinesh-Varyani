# 15. Generate Parentheses

**Difficulty**: Medium

**Topics**: String, Dynamic Programming, Backtracking

**Link**: https://leetcode.com/problems/generate-parentheses

Of course. Let's do a detailed, line-by-line breakdown of this classic backtracking algorithm for generating valid parentheses.

### The Logic: Recursive Backtracking (DFS)

The code uses a recursive helper function, `dfs` (Depth-First Search), to build the parenthesis strings. This approach is a form of **backtracking**. We try to build a solution step-by-step, and if we hit a dead end or an invalid state, we "backtrack" and try a different path.

The state of our recursion is tracked by three variables:

  * `l`: The number of **left** (opening) parentheses `(` we have used so far.
  * `r`: The number of **right** (closing) parentheses `)` we have used so far.
  * `s`: The string we have built so far.

The algorithm works by exploring possibilities based on two fundamental rules for creating a well-formed string of parentheses:

1.  **The Open Parenthesis Rule:** We can add an opening parenthesis `(` at any time, as long as we haven't exceeded our total limit (`n`).
2.  **The Close Parenthesis Rule:** We can only add a closing parenthesis `)` if there is a corresponding open parenthesis that needs closing. This means the count of left parentheses used (`l`) must be strictly greater than the count of right parentheses used (`r`).

The recursion stops (this is the **base case**) when the string reaches its full length (`n * 2`).

### The Example

Let's trace the execution for `n = 3`.
The expected result is a list of 5 valid combinations: `["((()))", "(()())", "(())()", "()(())", "()()()"]`.

-----

### Code and Live Demonstration

#### 1\. Initialization in `generateParenthesis`

```python
        res = []
        dfs(0, 0, '')
```

  * `res = []`: An empty list is created to store the final, valid combinations.
  * `dfs(0, 0, '')`: The initial call to the recursive helper is made. This starts the process with:
      * `l = 0` (0 left parentheses used)
      * `r = 0` (0 right parentheses used)
      * `s = ''` (an empty string to build upon)

#### 2\. The `dfs` Call Tree

A simple table can't capture the flow of recursion well. A "call tree" is a much better way to visualize the process. Let's trace the path of all the recursive calls.

-----

### **Live Trace: Call Tree Map (`n=3`)**

```
dfs(l=0, r=0, s='')
|
+-- Add '(': (l < 3 is true) -> dfs(l=1, r=0, s='(')
    |
    +-- Add '(': (l < 3 is true) -> dfs(l=2, r=0, s='((')
    |   |
    |   +-- Add '(': (l < 3 is true) -> dfs(l=3, r=0, s='(((')
    |   |   |
    |   |   +-- Add '(': (l < 3 is false) -> Path pruned.
    |   |   |
    |   |   +-- Add ')': (l > r is true) -> dfs(l=3, r=1, s='((()')
    |   |       |
    |   |       +-- Add ')': (l > r is true) -> dfs(l=3, r=2, s='((())')
    |   |           |
    |   |           +-- Add ')': (l > r is true) -> dfs(l=3, r=3, s='((()))')
    |   |               |
    |   |               +-- len(s) is 6. Base Case! Add '((()))' to res. Return.
    |   |
    |   +-- Add ')': (l > r is true) -> dfs(l=2, r=1, s='(()')
    |       |
    |       +-- Add '(': (l < 3 is true) -> dfs(l=3, r=1, s='(()(')
    |       |   |
    |       |   +-- Add ')': (l > r is true) -> dfs(l=3, r=2, s='(()()')
    |       |       |
    |       |       +-- Add ')': (l > r is true) -> dfs(l=3, r=3, s='(()())')
    |       |           |
    |       |           +-- len(s) is 6. Base Case! Add '(()())' to res. Return.
    |       |
    |       +-- Add ')': (l > r is true) -> dfs(l=2, r=2, s='(())')
    |           |
    |           +-- Add '(': (l < 3 is true) -> dfs(l=3, r=2, s='(())(')
    |           |   |
    |           |   +-- Add ')': (l > r is true) -> dfs(l=3, r=3, s='(())()')
    |           |       |
    |           |       +-- len(s) is 6. Base Case! Add '(())()' to res. Return.
    |           |
    |           +-- Add ')': (l > r is false) -> Path pruned.
    |
    +-- Add ')': (l > r is true) -> dfs(l=1, r=1, s='()')
        |
        +-- Add '(': (l < 3 is true) -> dfs(l=2, r=1, s='()(')
            |
            +-- Add '(': (l < 3 is true) -> dfs(l=3, r=1, s='()((')
            |   |
            |   +-- Add ')': (l > r is true) -> dfs(l=3, r=2, s='()(()')
            |       |
            |       +-- Add ')': (l > r is true) -> dfs(l=3, r=3, s='()(())')
            |           |
            |           +-- len(s) is 6. Base Case! Add '()(())' to res. Return.
            |
            +-- Add ')': (l > r is true) -> dfs(l=2, r=2, s='()()')
                |
                +-- Add '(': (l < 3 is true) -> dfs(l=3, r=2, s='()()(')
                |   |
                |   +-- Add ')': (l > r is true) -> dfs(l=3, r=3, s='()()()')
                |       |
                |       +-- len(s) is 6. Base Case! Add '()()()' to res. Return.
                |
                +-- Add ')': (l > r is false) -> Path pruned.

```

-----

### **Detailed Line-by-Line Breakdown of a Single Path**

Let's trace the path that generates `"()()()"`.

1.  **`dfs(0, 0, '')`**:

      * `if l < n` (0 \< 3) is true. Call `dfs(1, 0, '(')`.

2.  **`dfs(1, 0, '(')`**:

      * `if l < n` (1 \< 3) is true. It *could* call `dfs(2, 0, '((')` (this path leads to other answers).
      * `if l > r` (1 \> 0) is true. It also calls `dfs(1, 1, '()')`. Let's follow this one.

3.  **`dfs(1, 1, '()')`**:

      * `if l < n` (1 \< 3) is true. Call `dfs(2, 1, '()(')`.
      * `if l > r` (1 \> 1) is false. This path is pruned.

4.  **`dfs(2, 1, '()(')`**:

      * `if l < n` (2 \< 3) is true. It *could* call `dfs(3, 1, '()((')`.
      * `if l > r` (2 \> 1) is true. It also calls `dfs(2, 2, '()()')`. Let's follow this one.

5.  **`dfs(2, 2, '()()')`**:

      * `if l < n` (2 \< 3) is true. Call `dfs(3, 2, '()()(')`.
      * `if l > r` (2 \> 2) is false. This path is pruned.

6.  **`dfs(3, 2, '()()(')`**:

      * `if l < n` (3 \< 3) is false. This path is pruned.
      * `if l > r` (3 \> 2) is true. Call `dfs(3, 3, '()()()')`.

7.  **`dfs(3, 3, '()()()')`**:

      * `if len(s) == n * 2` (length of "()()()" is 6) is **true**. This is our **base case**.
      * `res.append("()()()")`. `res` now contains one of our answers.
      * `return`. This call finishes and control goes back up the call stack.

The algorithm continues this process, exploring every possible valid path until all branches have either hit the base case or been pruned.

-----

### 3\. Final Return

After the initial `dfs(0, 0, '')` call and all its recursive children have completed, the `res` list will be fully populated.

```python
        return res
```

  * The function returns the `res` list, which now contains `["((()))", "(()())", "(())()", "()(())", "()()()"]`.