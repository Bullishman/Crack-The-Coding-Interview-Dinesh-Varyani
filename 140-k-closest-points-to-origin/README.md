# 140. K Closest Points To Origin

**Difficulty**: Medium

**Topics**: Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect

**Link**: https://leetcode.com/problems/k-closest-points-to-origin

Of course. Let's do a detailed line-by-line breakdown of this code, which uses a **Min-Heap** to find the `k` closest points to the origin.

### The Logic: Min-Heap for Sorting by Distance

The core idea is to use a min-heap, a data structure that always keeps the element with the smallest value at the "top," making it very efficient to access.

1.  **Calculate Distances:** The code iterates through every point. For each point, it calculates its distance from the origin `(0,0)`.
2.  **Populate the Heap:** It pushes each point's information—its distance, x-coordinate, and y-coordinate—onto a min-heap. Since the distance is the first item in the tuple `(dist, x, y)`, the heap will automatically be ordered by the smallest distance.
3.  **Extract the Smallest:** After all points are in the heap, the code simply pops the `k` smallest elements from the top of the heap. Because it's a min-heap, these will be the `k` points with the smallest distances.

#### The Distance Trick (An Important Optimization)

The distance from the origin is calculated using the formula `sqrt(x² + y²)`. However, calculating square roots is computationally slow.

The code cleverly uses `dist = x**2 + y**2` (the *squared* distance). This is a valid and common optimization because the order is preserved: if `A > B`, then `sqrt(A) > sqrt(B)`. By comparing the squared distances, we avoid the slow `sqrt` calculation but still correctly identify which points are closer.

### The Example

Let's trace the execution with the following inputs:

  * `points = [[3, 3], [5, -1], [-2, 4]]`
  * `k = 2`

The squared distances are:

  * `[3, 3]`: `3² + 3² = 9 + 9 = 18`
  * `[5, -1]`: `5² + (-1)² = 25 + 1 = 26`
  * `[-2, 4]`: `(-2)² + 4² = 4 + 16 = 20`

The two points with the smallest distances are `[3, 3]` (dist 18) and `[-2, 4]` (dist 20). The expected result is `[[3, 3], [-2, 4]]` (the order doesn't matter).

-----

### Code and Live Demonstration

#### Phase 1: Building the Heap

##### 1\. Initialization

```python
        heap = []
```

  * We start with an empty list which will be treated as a min-heap by the `heapq` module.

##### 2\. The Loop (`for x, y in points:`)

-----

**Live Trace Table: Populating the Heap**
| Action | Point `(x, y)` | Distance `(dist)` | State of `heap` (conceptual order, smallest on top) |
| :--- | :--- | :--- | :--- |
| **Start** | - | - | `[]` |
| **Loop 1** | `[3, 3]` | `3² + 3² = 18` | `[(18, 3, 3)]` |
| **Loop 2** | `[5, -1]` | `5² + (-1)² = 26` | `[(18, 3, 3), (26, 5, -1)]` |
| **Loop 3** | `[-2, 4]` | `(-2)² + 4² = 20` | `[(18, 3, 3), (20, -2, 4), (26, 5, -1)]` |

  * **Line-by-line for Loop 3 (`x=-2, y=4`):**
    ```python
    dist = x**2 + y**2           # dist = (-2)**2 + 4**2 = 4 + 16 = 20
    heapq.heappush(heap, (dist, x, y)) # Pushes (20, -2, 4). The heapq module ensures
                                      # the smallest element (18, 3, 3) remains at the top.
    ```
  * After the loop finishes, the heap contains all the points, correctly ordered internally by their distance to the origin.

-----

#### Phase 2: Extracting the `k` Closest Points

##### 3\. Initialization

```python
        result = []
```

  * An empty list to store our final answer.

##### 4\. The Loop (`for _ in range(k):`)

Since `k=2`, this loop will run twice.

-----

**Live Trace Table: Extracting from the Heap**
| Loop Iteration | Action (`heappop`) | Popped Value `(dist, x, y)` | State of `heap` (after pop) | State of `result` |
| :--- | :--- | :--- | :--- | :--- |
| **Start** | - | - | `[(18, 3, 3), (20, -2, 4), (26, 5, -1)]`| `[]` |
| **1** (`_ = 0`) | `heapq.heappop(heap)`| `(18, 3, 3)` | `[(20, -2, 4), (26, 5, -1)]` | `[[3, 3]]` |
| **2** (`_ = 1`) | `heapq.heappop(heap)`| `(20, -2, 4)` | `[(26, 5, -1)]` | `[[3, 3], [-2, 4]]` |

  * **Line-by-line for Loop 1 (`_ = 0`):**

    ```python
    dist, x, y = heapq.heappop(heap) # Pops the smallest item: (18, 3, 3)
                                     # dist=18, x=3, y=3
    result.append((x, y))            # Appends (3, 3) to result.
    ```

  * **Line-by-line for Loop 2 (`_ = 1`):**

    ```python
    dist, x, y = heapq.heappop(heap) # Pops the new smallest item: (20, -2, 4)
                                     # dist=20, x=-2, y=4
    result.append((x, y))            # Appends (-2, 4) to result.
    ```

  * The loop finishes after two iterations.

-----

#### 5\. Final Return

```python
        return result
```

  * The function returns the final `result` list, which is `[[3, 3], [-2, 4]]`. This is the correct answer.