# 134. Binary Tree Zigzag Level Order Traversal

**Difficulty**: Medium

**Topics**: Tree, Breadth-First Search, Binary Tree

**Link**: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

Of course. Let's do a detailed line-by-line breakdown of this code for Zigzag Level Order Traversal.

### The Logic: Two-Phase DFS Approach

This solution cleverly solves the problem in two distinct phases:

1.  **Phase 1: Standard Level Order Collection (DFS):**

      * A Depth-First Search (`dfs`) function traverses the entire tree.
      * It uses a dictionary (`dic`) to group all node values by their level (`lvl`).
      * Crucially, in this phase, it performs a standard preorder traversal (`Node -> Left -> Right`), so all nodes at a given level are collected in a simple left-to-right order, ignoring the zigzag requirement for now.

2.  **Phase 2: Post-Processing for Zigzag:**

      * After the DFS has visited every node and the dictionary is fully populated, the code iterates through the dictionary's items (`level, values`).
      * It checks if the level number (`idx`) is odd.
      * If the level is **odd**, it reverses the list of values for that level.
      * If the level is **even**, it leaves the list as is.
      * Finally, it assembles these (now correctly ordered) lists into the final result.

### The Example

Let's trace the execution with a classic tree example:

  * **Tree Structure**:
    ```
          3
         / \
        9   20
           /  \
          15   7
    ```
  * **Expected Zigzag Output**: `[[3], [20, 9], [15, 7]]`

-----

### Code and Live Demonstration

#### 1\. Setup

```python
        # We need defaultdict from collections, but the code assumes it's available.
        from collections import defaultdict

        dic = defaultdict(list)
```

  * `dic` is a dictionary that will store lists. If we access a key (a level number) that doesn't exist yet, `defaultdict(list)` will automatically create an empty list for it. This is a convenient way to avoid checking if a key exists before appending.

#### 2\. Phase 1: The DFS Traversal

The main code starts the process by calling the `dfs` helper function on the root.

```python
        dfs(root, 0)  # Start traversal at the root (node 3) at level 0
```

-----

### **Live Trace Table Map (Phase 1: Populating the Dictionary)**

This trace shows the sequence of recursive calls and how the `dic` is built.

| DFS Call (Node, Level) | `node.val` | `lvl` | Action on `dic` | Resulting `dic` State | Next DFS Calls |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`dfs(root, 0)`** | **3** | **0** | `dic[0].append(3)` | `{0: [3]}` | `dfs(left=9, 1)`, `dfs(right=20, 1)` |
|   ↳ **`dfs(node 9, 1)`** | **9** | **1** | `dic[1].append(9)` | `{0: [3], 1: [9]}` | (None, returns) |
|   ↳ **`dfs(node 20, 1)`** | **20**| **1** | `dic[1].append(20)`| `{0: [3], 1: [9, 20]}` | `dfs(left=15, 2)`, `dfs(right=7, 2)`|
|     ↳ **`dfs(node 15, 2)`**| **15**| **2** | `dic[2].append(15)`| `{0: [3], 1: [9, 20], 2: [15]}` | (None, returns) |
|     ↳ **`dfs(node 7, 2)`** | **7** | **2** | `dic[2].append(7)` | `{0: [3], 1: [9, 20], 2: [15, 7]}` | (None, returns) |

  * After the initial `dfs(root, 0)` call completes, the DFS traversal is finished.
  * The `dic` is now fully populated with all nodes grouped by level, in a standard left-to-right order.
      * **Final `dic` state**: `{0: [3], 1: [9, 20], 2: [15, 7]}`

-----

#### 3\. Phase 2: Post-Processing and Final Return

Now, the final line of code executes. It's a list comprehension that builds the result.

```python
        return [values[::-1] if idx % 2 != 0 else values for idx, values in dic.items()]
```

Let's trace this list comprehension step-by-step as it iterates through `dic.items()`:

| `(idx, values)` from `dic.items()` | Condition: `idx % 2 != 0`? | Action | List Added to Final Result |
| :--- | :--- | :--- | :--- |
| `(0, [3])` | `0 % 2 != 0` is **False** | Use `values` as-is. | `[3]` |
| `(1, [9, 20])` | `1 % 2 != 0` is **True** | Reverse `values`. `[9, 20][::-1]` becomes `[20, 9]`. | `[20, 9]` |
| `(2, [15, 7])`| `2 % 2 != 0` is **False** | Use `values` as-is. | `[15, 7]` |

  * The list comprehension assembles these generated lists into the final return value.

#### 4\. Final Result

The function returns the assembled list: `[[3], [20, 9], [15, 7]]`.