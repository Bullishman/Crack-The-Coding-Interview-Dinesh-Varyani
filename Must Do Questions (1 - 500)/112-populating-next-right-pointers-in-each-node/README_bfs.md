# 112. Populating Next Right Pointers In Each Node

**Difficulty**: Medium

**Topics**: Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Link**: https://leetcode.com/problems/populating-next-right-pointers-in-each-node

Of course. Let's break down this version of the `connect` function.

This code uses a classic Breadth-First Search (BFS) approach, also known as level-order traversal, with a queue to solve the problem. This method is very intuitive and has the advantage of working for **any** binary tree, not just perfect ones.

### Algorithm Goal

The function's goal is the same: to populate the `next` pointer for each node to point to its immediate right sibling on the same level. It does this by processing the tree level by level. It uses a queue to keep track of the nodes for the next level to be processed.

### Line-by-Line Code Explanation

Here's a detailed explanation of each line, assuming `collections` has been imported.

```python
import collections

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
```

  * This sets up the class and the `connect` method.

<!-- end list -->

```python
        if not root:
            return None
```

  * **Purpose:** A base case check. If the tree is empty (`root` is `None`), there's nothing to connect, so it returns `None` immediately.

<!-- end list -->

```python
        queue = collections.deque([root])
```

  * **Purpose:** Initialize the data structure for the BFS traversal.
  * **`collections.deque`**: This creates a double-ended queue, which is highly efficient for adding (`append`) to the right and removing (`popleft`) from the left.
  * **`[root]`**: The traversal starts at the root, so it's the first and only item added to the queue initially.

<!-- end list -->

```python
        while queue:
```

  * **Purpose:** This is the main loop for the BFS. It will continue to run as long as there are nodes in the queue to be processed, effectively running until all levels of the tree have been visited.

<!-- end list -->

```python
            size = len(queue)
```

  * **Purpose:** This is a key step for level-order traversal. Before processing a level, we get the current number of items in the queue. This `size` represents the number of nodes on the **current level**.

<!-- end list -->

```python
            for i in range(size):
```

  * **Purpose:** This inner loop iterates exactly `size` times. This ensures that we only process the nodes that were present at the start of the level and don't accidentally start processing their children (which are added to the queue within this loop).

<!-- end list -->

```python
                node = queue.popleft()
```

  * **Purpose:** Dequeue (remove from the left) the next node in the level for processing.

<!-- end list -->

```python
                if i < size - 1:
```

  * **Purpose:** This is the core connection logic. It checks if the current node is **not** the last node on its level.
  * **`i`** is the index of the current node in the level (from 0 to `size - 1`).
  * **`size - 1`** is the index of the last node in the level.
  * If `i` is less than `size - 1`, it means there's at least one more node to its right on this level.

<!-- end list -->

```python
                    node.next = queue[0]
```

  * **Purpose:** If the condition is true, we set the `next` pointer of the current `node`.
  * **`queue[0]`**: After `popleft()`, the node at the front of the queue (`queue[0]`) is precisely the immediate right sibling of the `node` we just popped.

<!-- end list -->

```python
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
```

  * **Purpose:** Add the children of the current `node` to the queue.
  * These children will be processed in the next iteration of the outer `while` loop, as they belong to the next level down.

<!-- end list -->

```python
        return root
```

  * **Purpose:** After the `while` loop finishes, all nodes have been processed and their `next` pointers are correctly set. The function returns the modified root.

-----

### Live Trace Table Example

Let's trace the execution with the same perfect binary tree example:

```
       1
      / \
     2   3
    / \ / \
   4  5 6  7
```

**Trace Map:**

| `while queue`? | `queue` (before inner loop) | `size` | `i` | `node` (val) | Action & `queue` (after action) |
| :--- | :--- | :-: | :-: | :--- | :--- |
| **Start** | `[1]` | - | - | - | - |
| `True` | `[1]` | 1 | 0 | 1 | **Pop 1**. `i < 0` is `False`. **Append 2, 3**. `queue` -\> `[2, 3]`. |
| `True` | `[2, 3]` | 2 | 0 | 2 | **Pop 2**. `i < 1` is `True`. **Set `2.next = 3`**. **Append 4, 5**. `queue` -\> `[3, 4, 5]`. |
| | | | 1 | 3 | **Pop 3**. `i < 1` is `False`. **Append 6, 7**. `queue` -\> `[4, 5, 6, 7]`. |
| `True` | `[4, 5, 6, 7]` | 4 | 0 | 4 | **Pop 4**. `i < 3` is `True`. **Set `4.next = 5`**. (No children). `queue` -\> `[5, 6, 7]`.|
| | | | 1 | 5 | **Pop 5**. `i < 3` is `True`. **Set `5.next = 6`**. (No children). `queue` -\> `[6, 7]`.|
| | | | 2 | 6 | **Pop 6**. `i < 3` is `True`. **Set `6.next = 7`**. (No children). `queue` -\> `[7]`.|
| | | | 3 | 7 | **Pop 7**. `i < 3` is `False`. (No children). `queue` -\> `[]`. |
| `False` | `[]` | - | - | - | Loop terminates. |

**Final State of `next` Pointers:**

  * `1.next` -\> `NULL`
  * `2.next` -\> `3`
  * `3.next` -\> `NULL`
  * `4.next` -\> `5`
  * `5.next` -\> `6`
  * `6.next` -\> `7`
  * `7.next` -\> `NULL`

The function correctly connects all nodes and returns the `root`.