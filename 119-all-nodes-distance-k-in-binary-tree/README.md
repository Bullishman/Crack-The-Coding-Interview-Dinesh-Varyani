# 119. All Nodes Distance K In Binary Tree

**Difficulty**: Medium

**Topics**: Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Link**: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

Of course. Let's break down this powerful Python code for finding nodes at a specific distance in a binary tree.

### Algorithm Goal

The function `distanceK` is designed to find all nodes in a binary tree that are exactly at a distance `k` from a given `target` node.

A simple tree traversal (like DFS or BFS) only allows you to move downwards from a node. However, the distance `k` can be measured by going up towards the parent and then down into other subtrees. To solve this, the algorithm treats the tree like a graph. It uses a two-pass approach:

1.  **Pass 1: Annotate Parents:** It first traverses the tree to build a `parentMap`. This map allows us to travel "upwards" from any node to its parent, which is not normally possible.
2.  **Pass 2: Graph Traversal (DFS):** Starting from the `target` node, it performs a search (like DFS) outwards. From any given node, it explores its left child, its right child, and its parent, effectively moving in all directions. It keeps track of visited nodes to avoid infinite loops and stops once the distance from the target reaches `k`.

-----

### Line-by-Line Code Explanation

The code is structured with two helper functions inside the main function. Let's analyze it piece by piece.

#### Main Function Body

```python
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Helper functions getParent and getNodes are defined here...

        parentMap = {}
        seen = set()
        res = []
        getParent(root, None)
        getNodes(target, 0)

        return res
```

  * **`parentMap = {}`**: Initializes an empty dictionary to store the `child -> parent` mappings.
  * **`seen = set()`**: Initializes an empty set to keep track of nodes we have already visited during the search. This is crucial to prevent the search from going in circles (e.g., node -\> parent -\> node).
  * **`res = []`**: Initializes the list that will store the values of the result nodes.
  * **`getParent(root, None)`**: This is the first main call. It starts the process of building the `parentMap` by traversing the entire tree, starting from the `root`. The root's parent is `None`.
  * **`getNodes(target, 0)`**: This is the second main call. After the `parentMap` is built, it starts the distance-based search from the `target` node. The initial distance from the target to itself is `0`.
  * **`return res`**: Returns the final list of node values.

#### Helper Function 1: `getParent`

```python
        def getParent(node, parent):
            if node is None:
                return

            parentMap[node] = parent
            getParent(node.left, node)
            getParent(node.right, node)
```

  * **Purpose:** To recursively traverse the tree and populate the `parentMap`.
  * **`if node is None: return`**: The base case for the recursion. If we reach a null node, we stop.
  * **`parentMap[node] = parent`**: The core logic. It maps the current `node` to its `parent`.
  * **`getParent(node.left, node)`** and **`getParent(node.right, node)`**: Recursive calls. It continues the process for the left and right children. For these children, the current `node` becomes their parent.

#### Helper Function 2: `getNodes`

```python
        def getNodes(node, cnt):
            if not node or node in seen or cnt > k:
                return

            seen.add(node)
            if cnt == k:
                res.append(node.val)

            getNodes(node.left, cnt + 1)
            getNodes(node.right, cnt + 1)
            getNodes(parentMap[node], cnt + 1)
```

  * **Purpose:** To perform a DFS-like search from the target node to find all nodes at distance `k`.
  * **`if not node or node in seen or cnt > k: return`**: These are the base cases or stopping conditions for this search.
      * `not node`: Don't explore null nodes.
      * `node in seen`: Don't explore a node we've already visited.
      * `cnt > k`: Stop going down a path if we have already moved further than distance `k`.
  * **`seen.add(node)`**: Mark the current `node` as visited.
  * **`if cnt == k: res.append(node.val)`**: If the current distance `cnt` is exactly `k`, we've found a valid node. Add its value to the results.
  * **`getNodes(node.left, cnt + 1)`**: Explore the left child, increasing the distance count by 1.
  * **`getNodes(node.right, cnt + 1)`**: Explore the right child, increasing the distance count by 1.
  * **`getNodes(parentMap[node], cnt + 1)`**: Explore the parent (moving up\!), increasing the distance count by 1. This is where the `parentMap` is used.

-----

### Live Trace Table Example

Let's trace the execution with the following tree:

  * **Tree:**
    ```
           3
          / \
         5   1
        / \ / \
       6  2 0  8
          / \
         7   4
    ```
  * **`target`**: Node with value `5`
  * **`k`**: `2`

#### Pass 1: `getParent(root, None)` call

After this function completes, the `parentMap` will look like this:

| Key (Node) | Value (Parent Node) |
| :--- | :--- |
| Node(3) | `None` |
| Node(5) | Node(3) |
| Node(1) | Node(3) |
| Node(6) | Node(5) |
| Node(2) | Node(5) |
| Node(0) | Node(1) |
| Node(8) | Node(1) |
| Node(7) | Node(2) |
| Node(4) | Node(2) |

#### Pass 2: `getNodes(target, 0)` call

This is the main search. We'll trace the recursive calls.

**Initial State:** `res = []`, `seen = set()`

**Trace Map:**

| Call `getNodes(node.val, cnt)` | `cnt > k`? | `node in seen`? | Action | Recursive Calls Made (node.val, cnt) |
| :--- | :--- | :--- | :--- | :--- |
| **(5, 0)** | No | No | `seen.add(5)` | `(6, 1)`, `(2, 1)`, `(3, 1)` |
| ➞ **(6, 1)** | No | No | `seen.add(6)` | `(None, 2)`, `(None, 2)`, `(5, 2)` |
| ➞ ➞ **(5, 2)** | No | **Yes** | **Return** | - |
| ➞ **(2, 1)** | No | No | `seen.add(2)` | `(7, 2)`, `(4, 2)`, `(5, 2)` |
| ➞ ➞ **(7, 2)** | No | No | `seen.add(7)`. **`cnt == k` -\> `res.append(7)`** | `(None, 3)`, `(None, 3)`, `(2, 3)` |
| ➞ ➞ ➞ **(2, 3)** | **Yes** | - | **Return** | - |
| ➞ ➞ **(4, 2)** | No | No | `seen.add(4)`. **`cnt == k` -\> `res.append(4)`** | `(None, 3)`, `(None, 3)`, `(2, 3)` |
| ➞ ➞ ➞ **(2, 3)** | **Yes** | - | **Return** | - |
| ➞ ➞ **(5, 2)** | No | **Yes** | **Return** | - |
| ➞ **(3, 1)** | No | No | `seen.add(3)` | `(5, 2)`, `(1, 2)`, `(None, 2)` |
| ➞ ➞ **(5, 2)** | No | **Yes** | **Return** | - |
| ➞ ➞ **(1, 2)** | No | No | `seen.add(1)`. **`cnt == k` -\> `res.append(1)`** | `(0, 3)`, `(8, 3)`, `(3, 3)` |
| ➞ ➞ ➞ **(0, 3)** | **Yes** | - | **Return** | - |
| ➞ ➞ ➞ **(8, 3)** | **Yes** | - | **Return** | - |
| ➞ ➞ ➞ **(3, 3)** | **Yes** | - | **Return** | - |

**Final Step:**

1.  All recursive calls from `getNodes(target, 0)` are finished.
2.  The final state of `res` is `[7, 4, 1]`.
3.  The function returns `[7, 4, 1]`.