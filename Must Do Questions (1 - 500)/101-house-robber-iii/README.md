# 101. House Robber Iii

**Difficulty**: Medium

**Topics**: Dynamic Programming, Tree, Depth-First Search, Binary Tree

**Link**: https://leetcode.com/problems/house-robber-iii

Of course. Let's break down this elegant solution for the "House Robber III" problem.

### High-Level Overview

This code solves a problem where houses are arranged in a binary tree. The goal is to "rob" houses to get the maximum amount of money, with one constraint: you cannot rob two directly connected houses (a parent and its immediate child).

The strategy is a classic example of **Dynamic Programming on a Tree**, using a **Depth-First Search (DFS)** traversal. For every node in the tree, we want to know two things:

1.  What is the maximum amount of money we can get from its subtree if we **rob this node**?
2.  What is the maximum amount of money we can get from its subtree if we **do not rob this node**?

The `dfs` helper function is designed to return exactly this information for any given node: a list of two values `[rob_this_node, skip_this_node]`. By solving this for the leaf nodes and working our way up to the root, we can determine the final answer.

-----

### Prerequisites: The TreeNode

The code operates on a binary tree, so we need the `TreeNode` class definition.

```python
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    
     # Helper method for easier visualization
     def __repr__(self):
        return f"Node({self.val})"
```

-----

### Line-by-Line Code Explanation

Here is the code with detailed comments.

```python
class Solution:
    # This is the main function called by the user.
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # Line 1: def dfs(root):
        # This defines a nested helper function that performs the core logic using DFS.
        # It processes the tree from the leaves up to the root (post-order traversal).
        def dfs(root):
            # Line 2: if not root:
            # This is the base case for the recursion. An empty node (or null)
            # contributes nothing to the total robbery.
            if not root:
                # Line 3: return [0, 0]
                # It returns [0, 0], representing:
                # [max_money_if_robbing_this_null_node, max_money_if_skipping_this_null_node]
                return [0, 0]
            
            # Line 4: left = dfs(root.left)
            # Recursively call dfs on the left child. The `left` variable will hold
            # a list: [max_if_robbing_left_child, max_if_skipping_left_child].
            left = dfs(root.left)
            
            # Line 5: right = dfs(root.right)
            # Similarly, recursively call dfs on the right child.
            right = dfs(root.right)
            
            # --- Now we calculate the two values for the CURRENT `root` ---
            
            # Line 6: withroot = root.val + left[1] + right[1]
            # Calculate the max money if we ROB the current node.
            # This is its value (`root.val`) plus the max money from its children's
            # subtrees under the condition that we CANNOT rob the children themselves.
            # So, we must take the "skip" values from the left (`left[1]`) and right (`right[1]`) children.
            withroot = root.val + left[1] + right[1]
            
            # Line 7: withoutroot = max(left) + max(right)
            # Calculate the max money if we SKIP the current node.
            # If we don't rob this node, we are free to either rob or skip its children.
            # We choose whichever option gives more money for each child's subtree.
            # So, we take the max of the left's values (`max(left)`) and the max of the right's values (`max(right)`).
            withoutroot = max(left) + max(right)
            
            # Line 8: return [withroot, withoutroot]
            # Return the calculated pair for the current node, which will be used
            # by its parent in the recursion.
            return [withroot, withoutroot]
        
        # Line 9: return max(dfs(root))
        # Kick off the recursion starting from the actual root of the tree.
        # `dfs(root)` will return the final pair for the entire tree:
        # [max_money_if_robbing_the_root, max_money_if_skipping_the_root].
        # We don't care which choice was made at the top, we just want the absolute max,
        # so we return the maximum of these two final values.
        return max(dfs(root))
```

-----

### Example Walkthrough

Let's trace the code with the following tree:

**Structure:**

```
    3
   / \
  2   3
   \   \
    3   1
```

The `dfs` function works in a "post-order" way. It first computes the results for the children before computing the result for the parent. So, our trace will start from the leaves and move up.

#### Live Trace Table Map (Post-order Evaluation)

We trace the **return value** of each `dfs` call, from the bottom of the tree to the top.

Of course. Here is a detailed live trace table map for the execution flow you provided.

For a recursive function like this, the trace is best understood by looking at the "call stack" and how each function call resolves and returns a value to its caller. The process happens in a **post-order traversal** (left child, right child, then the node itself).

We will trace the provided example with this tree structure:

```
    3 (root)
   / \
  2   3
   \   \
    3   1
```

### Trace Map: From Leaves to Root

The execution dives to the deepest leaves first, calculates their values, and returns them upwards.

#### 1\. Call on Leaf: `dfs(Node(3))` (child of Node 2)

This is the first call that completes and returns a meaningful value.

| Current Call        | Line \# | Code Executed                   | `left` Variable | `right` Variable | Calculation Detail                    | Return Value |
| :------------------ | :----: | :------------------------------ | :-------------- | :--------------- | :------------------------------------ | :----------- |
| `dfs(Node(3))`      | 4      | `left = dfs(root.left)`         | `[0, 0]`        | -                | `dfs(None)` is called and returns `[0, 0]` | -            |
|                     | 5      | `right = dfs(root.right)`       | `[0, 0]`        | `[0, 0]`         | `dfs(None)` is called and returns `[0, 0]` | -            |
|                     | 6      | `withroot = root.val + ...`     | `[0, 0]`        | `[0, 0]`         | `withroot = 3 + 0 + 0 = 3`            | -            |
|                     | 7      | `withoutroot = max(left) + ...` | `[0, 0]`        | `[0, 0]`         | `withoutroot = max(0,0) + max(0,0) = 0` | -            |
|                     | 8      | `return [withroot, withoutroot]`| `[0, 0]`        | `[0, 0]`         | Returns the computed pair.            | **`[3, 0]`** |

#### 2\. Call on Leaf: `dfs(Node(1))` (child of Node 3)

This is the next leaf to be resolved.

| Current Call        | Line \# | Code Executed                   | `left` Variable | `right` Variable | Calculation Detail                    | Return Value |
| :------------------ | :----: | :------------------------------ | :-------------- | :--------------- | :------------------------------------ | :----------- |
| `dfs(Node(1))`      | 4      | `left = dfs(root.left)`         | `[0, 0]`        | -                | `dfs(None)` is called and returns `[0, 0]` | -            |
|                     | 5      | `right = dfs(root.right)`       | `[0, 0]`        | `[0, 0]`         | `dfs(None)` is called and returns `[0, 0]` | -            |
|                     | 6      | `withroot = root.val + ...`     | `[0, 0]`        | `[0, 0]`         | `withroot = 1 + 0 + 0 = 1`            | -            |
|                     | 7      | `withoutroot = max(left) + ...` | `[0, 0]`        | `[0, 0]`         | `withoutroot = max(0,0) + max(0,0) = 0` | -            |
|                     | 8      | `return [withroot, withoutroot]`| `[0, 0]`        | `[0, 0]`         | Returns the computed pair.            | **`[1, 0]`** |

#### 3\. Call on Intermediate Node: `dfs(Node(2))`

This call uses the result from the `dfs(Node(3))` leaf call.

| Current Call        | Line \# | Code Executed                   | `left` Variable | `right` Variable | Calculation Detail                           | Return Value |
| :------------------ | :----: | :------------------------------ | :-------------- | :--------------- | :------------------------------------------- | :----------- |
| `dfs(Node(2))`      | 4      | `left = dfs(root.left)`         | `[0, 0]`        | -                | `dfs(None)` is called and returns `[0, 0]`      | -            |
|                     | 5      | `right = dfs(root.right)`       | `[0, 0]`        | `[3, 0]`         | `dfs(Node(3))` is called, returns **`[3, 0]`** from Table 1. | -            |
|                     | 6      | `withroot = root.val + ...`     | `[0, 0]`        | `[3, 0]`         | `withroot = 2 + left[1] + right[1] = 2 + 0 + 0 = 2` | -            |
|                     | 7      | `withoutroot = max(left) + ...` | `[0, 0]`        | `[3, 0]`         | `withoutroot = max(0,0) + max(3,0) = 0 + 3 = 3` | -            |
|                     | 8      | `return [withroot, withoutroot]`| `[0, 0]`        | `[3, 0]`         | Returns the computed pair.                   | **`[2, 3]`** |

#### 4\. Call on Intermediate Node: `dfs(Node(3))` (right child of root)

This call uses the result from the `dfs(Node(1))` leaf call.

| Current Call        | Line \# | Code Executed                   | `left` Variable | `right` Variable | Calculation Detail                           | Return Value |
| :------------------ | :----: | :------------------------------ | :-------------- | :--------------- | :------------------------------------------- | :----------- |
| `dfs(Node(3))`      | 4      | `left = dfs(root.left)`         | `[0, 0]`        | -                | `dfs(None)` is called and returns `[0, 0]`      | -            |
|                     | 5      | `right = dfs(root.right)`       | `[0, 0]`        | `[1, 0]`         | `dfs(Node(1))` is called, returns **`[1, 0]`** from Table 2. | -            |
|                     | 6      | `withroot = root.val + ...`     | `[0, 0]`        | `[1, 0]`         | `withroot = 3 + left[1] + right[1] = 3 + 0 + 0 = 3` | -            |
|                     | 7      | `withoutroot = max(left) + ...` | `[0, 0]`        | `[1, 0]`         | `withoutroot = max(0,0) + max(1,0) = 0 + 1 = 1` | -            |
|                     | 8      | `return [withroot, withoutroot]`| `[0, 0]`        | `[1, 0]`         | Returns the computed pair.                   | **`[3, 1]`** |

#### 5\. Call on Root Node: `dfs(Node(3))` (The Root)

This is the top-level call within the `rob` function. It uses the results from Tables 3 and 4.

| Current Call        | Line \# | Code Executed                   | `left` Variable | `right` Variable | Calculation Detail                           | Return Value |
| :------------------ | :----: | :------------------------------ | :-------------- | :--------------- | :------------------------------------------- | :----------- |
| `dfs(root)`         | 4      | `left = dfs(root.left)`         | `[2, 3]`        | -                | `dfs(Node(2))` is called, returns **`[2, 3]`** from Table 3. | -            |
|                     | 5      | `right = dfs(root.right)`       | `[2, 3]`        | `[3, 1]`         | `dfs(Node(3))` is called, returns **`[3, 1]`** from Table 4. | -            |
|                     | 6      | `withroot = root.val + ...`     | `[2, 3]`        | `[3, 1]`         | `withroot = 3 + left[1] + right[1] = 3 + 3 + 1 = 7` | -            |
|                     | 7      | `withoutroot = max(left) + ...` | `[2, 3]`        | `[3, 1]`         | `withoutroot = max(2,3) + max(3,1) = 3 + 3 = 6` | -            |
|                     | 8      | `return [withroot, withoutroot]`| `[2, 3]`        | `[3, 1]`         | Returns the computed pair.                   | **`[7, 6]`** |

#### 6\. Final Calculation in `rob` function

This is the final step outside the recursion.

| Function | Line \# | Code Executed          | `dfs(root)` Result | Calculation Detail | Final Return |
| :------- | :----: | :--------------------- | :----------------- | :----------------- | :----------- |
| `rob`    | 9      | `return max(dfs(root))`| `[7, 6]`           | `max(7, 6)`        | **`7`** |

The maximum amount of money that can be robbed is **7**. This corresponds to robbing the root (3), the leaf node 3 (value 3), and the leaf node 1 (value 1). Notice that no two are directly connected.

### Complexity Analysis

  * **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. The DFS algorithm visits each node exactly once.
  * **Space Complexity:** $O(H)$, where $H$ is the height of the tree. This space is used by the recursion call stack. In the worst case of a completely unbalanced (skewed) tree, the height is $N$, making the space complexity $O(N)$. For a balanced tree, it would be $O(\\log N)$.