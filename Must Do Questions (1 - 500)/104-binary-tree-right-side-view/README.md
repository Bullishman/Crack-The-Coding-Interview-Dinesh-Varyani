# 104. Binary Tree Right Side View

**Difficulty**: Medium

**Topics**: Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Link**: https://leetcode.com/problems/binary-tree-right-side-view

Of course. Let's break down this Python code for finding the "Right Side View" of a binary tree.

### High-Level Overview

The goal is to collect the values of the nodes you can see when looking at a binary tree from the right side. This means finding the rightmost node at each level of the tree.

The strategy used in this code is a clever application of a **Depth-First Search (DFS)**.

1.  **Group by Level:** It performs a full traversal of the tree. It uses a dictionary (`dic`) to group all node values by their level (or depth). The dictionary keys are the level numbers (0 for the root, 1 for its children, etc.), and the values are lists of node values found at that level.
2.  **Pre-order Traversal:** The `dfs` function visits nodes in a "pre-order" (Node, Left, Right) sequence. This means for any given level, it will always process nodes from left to right.
3.  **Extract Rightmost:** After the entire tree has been traversed and the dictionary is populated, the code iterates through the dictionary. For each level's list of node values, it simply picks the **last element**. Because of the left-to-right traversal order, the last element added to the list for any level is guaranteed to be the rightmost node at that level.

-----

### Prerequisites

1.  **`TreeNode` Class:** The code operates on a standard binary tree node.

    ```python
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    ```

2.  **`collections.defaultdict`:** This is a dictionary-like object that provides a default value for a key that has not been set yet. `defaultdict(list)` means that if you try to access or modify a key that doesn't exist, it will automatically create an empty list `[]` for that key first. This is very convenient for grouping items.

    ```python
    from collections import defaultdict
    d = defaultdict(list)
    d[0].append(10) # Key 0 doesn't exist, so an empty list is created first.
    print(d)        # Output: defaultdict(<class 'list'>, {0: [10]})
    ```

-----

### Line-by-Line Code Explanation

```python
from collections import defaultdict
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Line 1: dic = defaultdict(list)
        # Initialize a defaultdict. The keys will be integer level numbers, and the
        # values will be lists of node values at that level.
        dic = defaultdict(list)
        
        # Line 2: def dfs(node: Optional[TreeNode], lvl: int) -> None:
        # Define a nested helper function to perform the Depth-First Search.
        # It takes the current `node` and its level `lvl` as input.
        def dfs(node: Optional[TreeNode], lvl: int) -> None:
            # Line 3: if not node:
            # This is the base case for the recursion. If the node is None,
            # we've reached the end of a branch, so we do nothing.
            if not node:
                # Line 4: return None
                return None
            
            # Line 5: dic[lvl].append(node.val)
            # This is the core logic. It appends the current node's value
            # to the list associated with its level (`lvl`).
            dic[lvl].append(node.val)
            
            # Line 6: dfs(node.left, lvl+1)
            # Recursively call `dfs` on the left child, incrementing the level by 1.
            dfs(node.left, lvl + 1)
            
            # Line 7: dfs(node.right, lvl+1)
            # After the entire left subtree is processed, recursively call `dfs` on the
            # right child, also incrementing the level by 1.
            dfs(node.right, lvl + 1)
        
        # Line 8: dfs(root, 0)
        # Kick off the traversal by calling the `dfs` function on the
        # root node, which is at level 0.
        dfs(root, 0)
        
        # Line 9: return [values[-1] for values in dic.values()]
        # This is the final result construction using a list comprehension.
        # 1. `dic.values()`: Gets all the lists of node values (e.g., [[1], [2, 3], [5, 4]]).
        # 2. `for values in ...`: Iterates through each of these lists.
        # 3. `values[-1]`: For each list, it takes the very last element.
        # The result is a new list containing only the rightmost values.
        return [values[-1] for values in dic.values()]
```

-----

### Example Walkthrough

Let's trace the code with the following tree. This example is good because the rightmost node at level 2 (`Node(5)`) is in the left subtree.

**Tree Structure:**

```
    1
   / \
  2   3
   \   \
    5   4
```

#### Live Trace Table Map (Call Stack Simulation)

The trace shows the sequence of `dfs` calls and the state of `dic` as it's being built.

| Call Stack (Indentation shows depth) | Action                             | State of `dic` after Action                |
| :----------------------------------- | :--------------------------------- | :----------------------------------------- |
| `dfs(Node(1), lvl=0)`                | `dic[0].append(1)`                 | `{0: [1]}`                                 |
| `   dfs(Node(2), lvl=1) `              | `dic[1].append(2)`                 | `{0: [1], 1: [2]}`                         |
| `     dfs(None, lvl=2) `               | `return`                           | `{0: [1], 1: [2]}`                         |
| `     dfs(Node(5), lvl=2) `            | `dic[2].append(5)`                 | `{0: [1], 1: [2], 2: [5]}`                 |
| `       dfs(None, lvl=3) `             | `return`                           | `{0: [1], 1: [2], 2: [5]}`                 |
| `       dfs(None, lvl=3) `             | `return`                           | `{0: [1], 1: [2], 2: [5]}`                 |
| `   dfs(Node(2), lvl=1) ` returns      | -                                  | -                                          |
| `dfs(Node(1), lvl=0)` continues      | -                                  | -                                          |
| `   dfs(Node(3), lvl=1) `              | `dic[1].append(3)`                 | `{0: [1], 1: [2, 3]}`                      |
| `     dfs(None, lvl=2) `               | `return`                           | `{0: [1], 1: [2, 3]}`                      |
| `     dfs(Node(4), lvl=2) `            | `dic[2].append(4)`                 | `{0: [1], 1: [2, 3], 2: [5, 4]}`           |
| `       dfs(None, lvl=3) `             | `return`                           | `{0: [1], 1: [2, 3], 2: [5, 4]}`           |
| `       dfs(None, lvl=3) `             | `return`                           | `{0: [1], 1: [2, 3], 2: [5, 4]}`           |
| `   dfs(Node(3), lvl=1) ` returns      | -                                  | -                                          |
| `dfs(Node(1), lvl=0)` returns        | -                                  | -                                          |
| **DFS Traversal Complete** | -                                  | **Final `dic`: `{0: [1], 1: [2, 3], 2: [5, 4]}`** |

**Final Step: Result Extraction** (Line 9)

| Code Executed                                | Explanation                                                              | Result    |
| :------------------------------------------- | :----------------------------------------------------------------------- | :-------- |
| `[values[-1] for values in dic.values()]`    | The code iterates through the values of the final `dic`.                 |           |
| - `values` is `[1]`                          | `values[-1]` is `1`                                                       | `[1]`     |
| - `values` is `[2, 3]`                       | `values[-1]` is `3`                                                       | `[1, 3]`  |
| - `values` is `[5, 4]`                       | `values[-1]` is `4`                                                       | `[1, 3, 4]`|

**Final Result:** The function returns `[1, 3, 4]`.

-----

### Complexity Analysis

  * **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. The DFS algorithm visits every node exactly once.

  * **Space Complexity:** $O(N)$ in the worst case.

      * The `dic` stores every node in the tree, so it takes $O(N)$ space.
      * The recursion call stack depth will be $O(H)$, where $H$ is the height of the tree. In the worst case (a skewed tree), $H$ can be $N$. The space for the dictionary is the dominant factor.

    *(Note: This problem can be solved with $O(H)$ space using a more optimized DFS or $O(W)$ space (max width of tree) using a Breadth-First Search, but this solution is valued for its clarity.)*