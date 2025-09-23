# 114. Kth Smallest Element In A Bst

**Difficulty**: Medium

**Topics**: Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Link**: https://leetcode.com/problems/kth-smallest-element-in-a-bst

Of course. Let's break down this concise and elegant Python code for finding the k-th smallest element in a Binary Search Tree (BST).

### Algorithm Goal

The function `kthSmallest` is designed to find the k-th smallest value in a Binary Search Tree (BST). A key property of a BST is that an **in-order traversal** of the tree visits the nodes in ascending sorted order. This code cleverly leverages that property. It performs a full in-order traversal to get a sorted list of all node values and then simply picks the element at the k-th position.

### Line-by-Line Code Explanation

Here's a detailed breakdown of each line.

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
```

  * This defines the `Solution` class and the `kthSmallest` method.
  * It takes the `root` of the tree and an integer `k` as input.

<!-- end list -->

```python
        def inorder(r):
```

  * **Purpose:** This defines a helper function `inorder` inside `kthSmallest`. This is a common pattern in Python for functions that are only needed by the main method.
  * `r` is the parameter representing the current node being visited.

<!-- end list -->

```python
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
```

  * **Purpose:** This is a recursive, one-line implementation of an in-order traversal. Let's break down the `if r` part first.
  * **`if r`**: This is the main condition. The traversal logic only runs if the current node `r` is not `None`.
  * **`else []`**: This is the **base case** for the recursion. If `r` is `None` (meaning we've hit a dead end, like `root.left` of a leaf node), the function returns an empty list `[]`. This stops the recursion from going on forever.
  * **`inorder(r.left)`**: This is the first recursive call. The function calls itself on the left child of the current node. This ensures we go all the way down the left side of a subtree first.
  * **`+ [r.val]`**: After the left subtree has been fully traversed and its sorted list of values has been returned, we append the current node's value (`r.val`). It's wrapped in `[]` to make it a list so it can be concatenated.
  * **`+ inorder(r.right)`**: Finally, the function makes a recursive call on the right child. This ensures we visit the right subtree only after visiting the left subtree and the current node.
  * The `+` operators concatenate the lists returned from the recursive calls, building up the final sorted list.

<!-- end list -->

```python
        return inorder(root)[k - 1]
```

  * **Purpose:** This line executes the logic and returns the final answer.
  * **`inorder(root)`**: It kicks off the recursive traversal starting from the `root` of the entire tree. The result will be a sorted list of all values in the BST.
  * **`[k - 1]`**: It accesses the element at index `k - 1` of the sorted list. We use `k - 1` because `k` is 1-based (e.g., 1st smallest, 2nd smallest), while list indices are 0-based.

-----

### Live Trace Table Example

Let's trace the execution with this example BST and `k = 3`.

**Input:**

  * `root` of the tree:
    ```
           3
          / \
         1   4
          \
           2
    ```
  * `k = 3`

**Goal:** Find the 3rd smallest element.

The main call is `kthSmallest(Node(3), 3)`, which in turn calls `inorder(Node(3))`. Let's trace the `inorder` calls.

**Trace Map of `inorder` Function Calls:**

| Call Stack (Current `r`) | Action | Return Value | Notes |
| :--- | :--- | :--- | :--- |
| `inorder(Node(3))` | Calls `inorder(Node(1))` | `[1, 2, 3, 4]` | Main call |
| ➞ `inorder(Node(1))`| Calls `inorder(None)` | `[1, 2]` | |
| ➞ ➞ `inorder(None)`| `r` is `None` | `[]` | Base case (left of 1) |
| ➞ `inorder(Node(1))`| Returns `[] + [1] + inorder(Node(2))` | `[1, 2]` | |
| ➞ ➞ `inorder(Node(2))`| Calls `inorder(None)` | `[2]` | |
| ➞ ➞ ➞ `inorder(None)`| `r` is `None` | `[]` | Base case (left of 2) |
| ➞ ➞ `inorder(Node(2))`| Returns `[] + [2] + inorder(None)` | `[2]` | |
| ➞ ➞ ➞ `inorder(None)`| `r` is `None` | `[]` | Base case (right of 2) |
| `inorder(Node(3))` | Returns `[1, 2] + [3] + inorder(Node(4))` | `[1, 2, 3, 4]`| |
| ➞ `inorder(Node(4))`| Calls `inorder(None)` | `[4]` | |
| ➞ ➞ `inorder(None)`| `r` is `None` | `[]` | Base case (left of 4) |
| ➞ `inorder(Node(4))`| Returns `[] + [4] + inorder(None)` | `[4]` | |
| ➞ ➞ `inorder(None)`| `r` is `None` | `[]` | Base case (right of 4) |

**Summary of the `inorder` execution:**

1.  `inorder(3)` calls `inorder(1)`.
2.  `inorder(1)` calls `inorder(None)` (left), which returns `[]`.
3.  `inorder(1)` processes itself, adding `[1]`.
4.  `inorder(1)` calls `inorder(2)` (right).
5.  `inorder(2)` calls `inorder(None)` (left), returns `[]`.
6.  `inorder(2)` processes itself, adding `[2]`.
7.  `inorder(2)` calls `inorder(None)` (right), returns `[]`.
8.  The call to `inorder(2)` returns `[] + [2] + []` -\> `[2]`.
9.  The call to `inorder(1)` returns `[] + [1] + [2]` -\> `[1, 2]`.
10. `inorder(3)` processes itself, adding `[3]`.
11. `inorder(3)` calls `inorder(4)` (right).
12. `inorder(4)` returns `[4]`.
13. The final result from `inorder(3)` is `[1, 2] + [3] + [4]` -\> `[1, 2, 3, 4]`.

**Final Step:**

1.  The `inorder(root)` call completes and returns the list `[1, 2, 3, 4]`.
2.  The final line of the `kthSmallest` function executes: `return [1, 2, 3, 4][k - 1]`.
3.  Since `k` is `3`, this becomes `return [1, 2, 3, 4][2]`.
4.  The value at index 2 is **3**.

The code correctly returns **3** as the 3rd smallest element.