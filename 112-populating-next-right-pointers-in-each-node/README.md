# 112. Populating Next Right Pointers In Each Node

**Difficulty**: Medium

**Topics**: Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Link**: https://leetcode.com/problems/populating-next-right-pointers-in-each-node

Of course. Let's break down this elegant Python code for connecting nodes in a perfect binary tree.

### Algorithm Goal

The function `connect` takes a **perfect binary tree** as input. In a perfect binary tree, every level is completely filled, and all leaf nodes are at the same depth. The `Node` object has `left`, `right`, and `next` pointers. The goal of this function is to populate the `next` pointer for each node to point to its immediate right sibling on the same level. If a node is the rightmost node on its level, its `next` pointer should remain `None`.

The algorithm works by iterating through the tree level by level, using pointers to connect the children of the nodes on the current level. It achieves this without using a queue or recursion, making it very memory efficient (O(1) extra space).

### Line-by-Line Code Explanation

Here is a detailed explanation of each line.

```python
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
```

  * This defines a class `Solution` and a method `connect` that takes the `root` of the tree.
  * The `Node` has `val`, `left`, `right`, and `next` attributes.

<!-- end list -->

```python
        cur, nxt = root, root.left if root else None
```

  * **Purpose:** Initialize two pointers, `cur` (current) and `nxt` (next).
  * **`cur = root`**: The `cur` pointer is the main "worker" pointer. It starts at the root and traverses horizontally across the nodes of the current level we are processing.
  * **`nxt = root.left if root else None`**: The `nxt` pointer always points to the **start of the next level**. It acts as a "head" for the level below. We use it to know where to jump down to when `cur` finishes traversing its current level. The check `if root else None` handles the case of an empty tree.

<!-- end list -->

```python
        while cur and nxt:
```

  * **Purpose:** This is the main loop that controls the level-by-level traversal.
  * **`cur`**: Ensures we have a current node to work with.
  * **`nxt`**: Ensures that there is a next level to process. When `cur` is on the last level of the tree, `nxt` will become `None` (since the leaf nodes have no children), and the loop will terminate.

<!-- end list -->

```python
            cur.left.next = cur.right
```

  * **Purpose:** This is the first connection step. For the current node `cur`, it connects its left child to its right child. This handles connections within a single parent's children (e.g., node 4 points to node 5). Since it's a perfect binary tree, we are guaranteed that if `cur.left` exists, `cur.right` also exists.

<!-- end list -->

```python
            if cur.next:
```

  * **Purpose:** Check if the `cur` node has a sibling to its right on the same level.

<!-- end list -->

```python
                cur.right.next = cur.next.left
```

  * **Purpose:** This is the second and crucial connection step. If `cur` has a `next` node, it means we can connect `cur`'s right child to the left child of its sibling (`cur.next`). This handles connections *between* different parent's children (e.g., node 5 points to node 6).

<!-- end list -->

```python
            cur = cur.next
```

  * **Purpose:** Move the "worker" pointer one step to the right, to the next node on the same level.

<!-- end list -->

```python
            if not cur:
```

  * **Purpose:** This condition becomes true when `cur` has successfully traversed all the nodes on the current level and has become `None`.

<!-- end list -->

```python
                cur = nxt
```

  * **Purpose:** We have finished the current level. It's time to move down. We reset `cur` to the start of the *next* level, which we saved in the `nxt` pointer.

<!-- end list -->

```python
                nxt = cur.left
```

  * **Purpose:** Update `nxt` to point to the start of the level *below* the one we are about to process.

<!-- end list -->

```python
        return root
```

  * **Purpose:** After the loop finishes, all `next` pointers are set correctly. The function returns the modified root of the tree.

-----

### Live Trace Table Example

Let's trace the execution with this perfect binary tree:

```
       1 -> NULL
      / \
     2 -> 3 -> NULL
    / \  / \
   4->5->6->7 -> NULL
```

**Initial State:**

| Variable | Value | Notes |
| :--- | :--- | :--- |
| `root` | Node(1) | The root of the tree. |
| `cur` | Node(1) | `cur` starts at the root. |
| `nxt` | Node(2) | `nxt` is the start of the next level (`root.left`). |

**Trace Map:**

| `cur` (val) | `nxt` (val) | `while cur and nxt`? | Action | Tree State Change |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **2** | `True` | Start loop. `cur` is on Level 0. | |
| 1 | 2 | | `cur.left.next = cur.right` | `2.next` points to `3`. |
| 1 | 2 | | `if cur.next:` is `False`. `cur` (1) has no next. | |
| 1 | 2 | | `cur = cur.next` | `cur` becomes `None`. |
| `None` | 2 | | `if not cur:` is `True`. **Move down a level.** | |
| `None` | 2 | | `cur = nxt` | `cur` becomes `Node(2)`. |
| 2 | 2 | | `nxt = cur.left` | `nxt` becomes `Node(4)`. |
| **2** | **4** | `True` | Start next iteration. `cur` is on Level 1. | |
| 2 | 4 | | `cur.left.next = cur.right` | `4.next` points to `5`. |
| 2 | 4 | | `if cur.next:` is `True` (2 -\> 3). | |
| 2 | 4 | | `cur.right.next = cur.next.left` | `5.next` points to `6`. (Connects 2's right child to 3's left child). |
| 2 | 4 | | `cur = cur.next` | `cur` becomes `Node(3)`. |
| **3** | **4** | `True` | Continue iteration. | |
| 3 | 4 | | `cur.left.next = cur.right` | `6.next` points to `7`. |
| 3 | 4 | | `if cur.next:` is `False`. `cur` (3) is the last on its level. | |
| 3 | 4 | | `cur = cur.next` | `cur` becomes `None`. |
| `None` | 4 | | `if not cur:` is `True`. **Move down a level.** | |
| `None` | 4 | | `cur = nxt` | `cur` becomes `Node(4)`. |
| 4 | 4 | | `nxt = cur.left` | `nxt` becomes `None` (4 is a leaf). |
| **4** | **None** | `False` | Loop terminates because `nxt` is `None`. | |

**Final Step:**

1.  The `while` loop condition `while cur and nxt` is `False` because `nxt` is now `None`.
2.  The loop exits.
3.  The function executes `return root`.

The tree has been fully connected level by level, and the function returns the root of the now-modified tree.