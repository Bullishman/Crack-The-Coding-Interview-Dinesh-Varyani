# 142. Minimum Height Trees

**Difficulty**: Medium

**Topics**: Depth-First Search, Breadth-First Search, Graph, Topological Sort

**Link**: https://leetcode.com/problems/minimum-height-trees

Of course. Let's do a detailed, line-by-line demonstration of this clever algorithm for finding Minimum Height Trees (MHTs).

### The Logic: Topological Sort / Leaf Peeling

The problem asks for the node(s) that, if chosen as the root, would result in a tree of the minimum possible height. A brute-force approach (trying every node as a root) would be too slow.

This algorithm uses a much smarter approach, conceptually similar to peeling an onion layer by layer to find its core. The intuition is that the nodes that are furthest from the "center" of the graph (the leaves) can't possibly be the roots of an MHT.

1.  **Identify Leaves:** The algorithm starts by identifying all the initial "leaves" of the graph—nodes that have only one connection (a degree of 1).
2.  **Peel the Leaves:** It removes all of these leaves simultaneously. When a leaf is removed, the degree of its neighbor is reduced by one.
3.  **Find New Leaves:** This removal might turn some of the inner nodes into new leaves (because their degree is now 1).
4.  **Repeat:** The algorithm repeats this process—finding the new leaves and peeling them away—until only one or two nodes remain.
5.  **The Core:** These final one or two nodes are the "center" of the graph and are the roots of the Minimum Height Trees.

### The Example

Let's trace the execution with the following graph:

  * `n = 6`
  * `edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]`

This graph looks like a star centered at node `3`, with a tail (`4-5`) attached. The MHT root should be `3` or `4`. Let's see what the algorithm finds.

-----

### Code and Live Demonstration

#### Phase 1: Setup and Graph Building

```python
        if n <= 1:
            return [0]
        # n is 6, so we continue.
        
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
```

  * An adjacency list (`graph`) is built to represent the connections.
  * **After this loop, `graph` is:**
      * `{0: [3], 3: [0, 1, 2, 4], 1: [3], 2: [3], 4: [3, 5], 5: [4]}`

#### Phase 2: Finding the First Layer of Leaves

```python
        leaves = [i for i in range(n) if len(graph[i]) == 1]
```

  * This line iterates through all nodes from 0 to 5 and checks the length of their adjacency list in the `graph`.
  * `len(graph[0])` is 1.
  * `len(graph[1])` is 1.
  * `len(graph[2])` is 1.
  * `len(graph[3])` is 4.
  * `len(graph[4])` is 2.
  * `len(graph[5])` is 1.
  * **Initial `leaves` list**: `[0, 1, 2, 5]`

-----

#### Phase 3: The Peeling Loop (`while n > 2`)

This is the core of the algorithm. We will trace the state of `n`, `leaves`, and `graph` through each iteration.

**Live Trace Table Map**

| Iteration | `n` (start) | `leaves` to process | Inner Loop Actions (leaf -\> neighbor) | `new_leaves` | `n` (end) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 6 | `[0, 1, 2, 5]` | `0 -> 3` (degree 3), `1 -> 3` (degree 2), `2 -> 3` (degree 1 -\> new leaf\!), `5 -> 4` (degree 1 -\> new leaf\!) | `[3, 4]` | 2 |
| **2** | 2 | `[3, 4]` | `3 -> 4` (degree 0), `4 -> 3` (no neighbors left) | `[]` | 0 |

*Wait, there's a small error in the provided code.* The original code has `range(n + 1)`, which might include a non-existent node if `n` is the max node index. Let's assume it should be `range(n)`. Let's re-trace with the corrected logic and the example.

**Corrected Live Trace Table**

| Iteration | `n` (start) | `leaves` to process | Inner Loop Actions (leaf -\> neighbor) & `graph` changes | `new_leaves` |
| :--- | :--- | :--- | :--- | :--- |
| **Start** | 6 | `[0, 1, 2, 5]` | | |
| **1** | **`while 6 > 2`** | `[0, 1, 2, 5]` | | |
| | `n -= 4` -\> `n=2` | | | `[]` |
| | `for leaf in [0,1,2,5]`| `leaf=0`: `neighbor=3`. `graph[3]` becomes `[1,2,4]`. `graph[0]` empty. `len(graph[3])=3`. | |
| | | `leaf=1`: `neighbor=3`. `graph[3]` becomes `[2,4]`. `graph[1]` empty. `len(graph[3])=2`. | |
| | | `leaf=2`: `neighbor=3`. `graph[3]` becomes `[4]`. `graph[2]` empty. `len(graph[3])=1`. **`3` is a new leaf.** | `[3]` |
| | | `leaf=5`: `neighbor=4`. `graph[4]` becomes `[3]`. `graph[5]` empty. `len(graph[4])=1`. **`4` is a new leaf.** | `[3, 4]` |
| | `leaves` becomes `[3, 4]` | | | |
| **2** | **`while 2 > 2`** | (Condition is **False**) | Loop terminates. | |

-----

### **Detailed Line-by-Line Breakdown of the Loop**

#### Iteration 1

  * `while n > 2`: The condition `6 > 2` is **True**.
  * `n -= len(leaves)` -\> `n = 6 - 4` -\> `n` becomes `2`.
  * `new_leaves = []`
  * **Inner `for` loop begins, processing the `[0, 1, 2, 5]` leaves:**
      * **`leaf = 0`**:
          * `neighbor = graph[0].pop()` -\> `neighbor` is `3`. `graph` is now `{0: [], ...}`.
          * `graph[neighbor].remove(leaf)` -\> `graph[3].remove(0)`. `graph[3]` is now `[1, 2, 4]`.
          * `len(graph[3])` is `3`. It's not `1`, so `3` is not a new leaf yet.
      * **`leaf = 1`**:
          * `neighbor = graph[1].pop()` -\> `neighbor` is `3`.
          * `graph[3].remove(1)`. `graph[3]` is now `[2, 4]`.
          * `len(graph[3])` is `2`. Still not a new leaf.
      * **`leaf = 2`**:
          * `neighbor = graph[2].pop()` -\> `neighbor` is `3`.
          * `graph[3].remove(2)`. `graph[3]` is now `[4]`.
          * `len(graph[3])` is `1`. **Condition is met\!** `new_leaves.append(3)`.
          * `new_leaves` is now `[3]`.
      * **`leaf = 5`**:
          * `neighbor = graph[5].pop()` -\> `neighbor` is `4`.
          * `graph[4].remove(5)`. `graph[4]` is now `[3]`.
          * `len(graph[4])` is `1`. **Condition is met\!** `new_leaves.append(4)`.
          * `new_leaves` is now `[3, 4]`.
  * **End of Inner Loop**:
  * `leaves = new_leaves` -\> `leaves` is now `[3, 4]`.

#### Iteration 2

  * `while n > 2`: The condition `2 > 2` is **False**. The loop terminates.

-----

### 4\. Final Return

```python
        return leaves
```

  * The code exits the `while` loop.
  * The value of the `leaves` variable at this point is `[3, 4]`.
  * The function returns **`[3, 4]`**. These are the two central nodes that form the roots of the Minimum Height Trees.