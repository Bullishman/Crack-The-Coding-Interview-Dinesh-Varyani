# 148. Queue Reconstruction By Height

**Difficulty**: Medium

**Topics**: Array, Greedy, Sorting

**Link**: https://leetcode.com/problems/queue-reconstruction-by-height

Of course. Let's do a detailed, line-by-line breakdown of this very elegant greedy algorithm for reconstructing the queue.

### The Logic: A Greedy Approach (Tallest First)

This solution uses a clever greedy strategy that seems counterintuitive at first but is guaranteed to work. The core idea is to place the tallest people first. Why? Because taller people don't care about where shorter people are placed. A person `[h, k]` only counts people in front of them who are of height `h` or greater. By placing the tallest people first, we ensure that when we later insert a shorter person, it doesn't affect the `k` count of any of the taller people already in the queue.

The algorithm has two main phases:

1.  **Custom Sort:** The `people` list is sorted in a very specific order:
      * **Primary Sort Key:** Sort by height (`h`) in **descending** order (tallest to shortest).
      * **Secondary Sort Key (for ties):** If two people have the same height, sort them by their `k` value in **ascending** order (smallest `k` first).
2.  **Greedy Insertion:** Iterate through the now-sorted list of people. For each person `p = [h, k]`, insert them into the `result` list at the index specified by their `k` value. Since all the people already in `result` are taller than or equal to the current person, inserting at index `k` guarantees there will be exactly `k` taller people in front of them.

### The Example

Let's trace the execution with a classic example:

  * `people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]`

The expected result is `[[5,0], [7,0], [5,2], [6,1], [7,1], [4,4]]`.

-----

### Code and Live Demonstration

#### Phase 1: The Custom Sort

##### 1\. Initialization

```python
        result = []
```

  * We start with an empty `result` list, which will be our final reconstructed queue.

##### 2\. The Sort

```python
        people.sort(key=lambda x: (-x[0], x[1]))
```

  * This is the most critical line. The `key` tells the sort function how to order the elements.
  * `-x[0]`: We sort by the negative of the height. Sorting numbers in ascending order is the default, so sorting by the negative value effectively sorts the original values in **descending** order.
  * `x[1]`: If two heights are the same (meaning their negative heights are also the same), this secondary key is used. We sort by `k` in the standard **ascending** order.

**Live Trace Table: Sorting `people`**
| Original `people` List | Custom Sort Key `(-h, k)` |
| :--- | :--- |
| `[7,0]` | `(-7, 0)` |
| `[4,4]` | `(-4, 4)` |
| `[7,1]` | `(-7, 1)` |
| `[5,0]` | `(-5, 0)` |
| `[6,1]` | `(-6, 1)` |
| `[5,2]` | `(-5, 2)` |

After applying the sort key, Python arranges the list.

  * First by `-h`: `-7` comes before `-6`, which comes before `-5`, etc.
  * When `-h` values are the same (e.g., `(-7,0)` and `(-7,1)`), it sorts by `k`: `0` comes before `1`.

**The state of the `people` list after sorting is:**
`[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]`

-----

#### Phase 2: Greedy Insertion

##### 3\. The Loop (`for p in people:`)

Now we iterate through our newly sorted list and insert each person `p` into the `result` list.

**Live Trace Table: Building the `result` Queue**
| `p` (from sorted list) | `p[1]` (Insert Index) | Action: `result.insert(p[1], p)` | `result` (State after insertion) |
| :--- | :--- | :--- | :--- |
| **Start** | - | - | `[]` |
| **`[7,0]`** | 0 | `result.insert(0, [7,0])` | `[[7,0]]` |
| **`[7,1]`** | 1 | `result.insert(1, [7,1])` | `[[7,0], [7,1]]` |
| **`[6,1]`** | 1 | `result.insert(1, [6,1])` | `[[7,0], [6,1], [7,1]]` |
| **`[5,0]`** | 0 | `result.insert(0, [5,0])` | `[[5,0], [7,0], [6,1], [7,1]]` |
| **`[5,2]`** | 2 | `result.insert(2, [5,2])` | `[[5,0], [7,0], [5,2], [6,1], [7,1]]` |
| **`[4,4]`** | 4 | `result.insert(4, [4,4])` | `[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]` |

**Step-by-Step Explanation of Insertion:**

  * **`p = [7,0]`**: Insert `[7,0]` at index `0`. Result is `[[7,0]]`.
  * **`p = [7,1]`**: Insert `[7,1]` at index `1`. Result is `[[7,0], [7,1]]`. So far, so good.
  * **`p = [6,1]` (Key Moment\!)**: Insert `[6,1]` at index `1`. The `[7,1]` that was at index 1 gets shifted to the right. The list becomes `[[7,0], [6,1], [7,1]]`. Notice that inserting the shorter person `[6,1]` did not change the fact that `[7,0]` has 0 taller people in front and `[7,1]` has 1 taller person (`[7,0]`) in front.
  * **`p = [5,0]`**: Insert `[5,0]` at index `0`. Everything gets shifted right. Result: `[[5,0], [7,0], [6,1], [7,1]]`.
  * **`p = [5,2]`**: Insert `[5,2]` at index `2`. The elements at index 2 and beyond get shifted right. Result: `[[5,0], [7,0], [5,2], [6,1], [7,1]]`.
  * **`p = [4,4]`**: Insert `[4,4]` at index `4`. The element `[7,1]` gets shifted right. Result: `[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]`.

Oops, I seem to have made a mistake in the final step of the trace table. Let's re-check the last insertion carefully.

  * Current `result`: `[[5,0], [7,0], [5,2], [6,1], [7,1]]`
  * Person `p`: `[4,4]`
  * Action: `result.insert(4, [4,4])`
  * The element at index `4` is `[7,1]`. This element will be shifted to index `5`.
  * Correct `result`: `[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]`

Ah, I see the error was in my expected output, not the trace. Let me re-verify the expected output.
`[[5,0], [7,0], [5,2], [6,1], [7,1], [4,4]]` is indeed the correct final queue. Let's check it:

  - `[5,0]`: 0 people \>= 5 in front. Correct.
  - `[7,0]`: 0 people \>= 7 in front. Correct.
  - `[5,2]`: 2 people (`[7,0]`, `[6,1]`... wait, `[7,0]` is taller but `[6,1]` is taller). Let's re-run the trace. My apologies, this is a tricky one to do manually.

**Let's re-trace the insertion phase with extreme care.**

| `p` (from sorted list) | `p[1]` (Insert Index) | `result` (State BEFORE insertion) | `result` (State AFTER insertion) |
| :--- | :--- | :--- | :--- |
| **`[7,0]`** | 0 | `[]` | `[[7,0]]` |
| **`[7,1]`** | 1 | `[[7,0]]` | `[[7,0], [7,1]]` |
| **`[6,1]`** | 1 | `[[7,0], [7,1]]` | `[[7,0], [6,1], [7,1]]` |
| **`[5,0]`** | 0 | `[[7,0], [6,1], [7,1]]` | `[[5,0], [7,0], [6,1], [7,1]]` |
| **`[5,2]`** | 2 | `[[5,0], [7,0], [6,1], [7,1]]` | `[[5,0], [7,0], [5,2], [6,1], [7,1]]` |
| **`[4,4]`** | 4 | `[[5,0], [7,0], [5,2], [6,1], [7,1]]` | `[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]` |

My apologies, my manual trace was correct, but I misread the expected output from memory. The final output from the algorithm is `[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]`. Let's verify *this* result:

  - `[5,0]`: 0 people taller or equal in front. **Correct.**
  - `[7,0]`: 0 people taller or equal in front. **Correct.**
  - `[5,2]`: 2 people taller or equal (`[7,0]`, `[6,1]`) in front. **Correct.**
  - `[6,1]`: 1 person taller or equal (`[7,0]`) in front. **Correct.**
  - `[4,4]`: 4 people taller or equal (`[5,0]`, `[7,0]`, `[5,2]`, `[6,1]`) in front. **Correct.**
  - `[7,1]`: 1 person taller or equal (`[7,0]`) in front. **Correct.**

The algorithm works perfectly. The trace demonstrates *how* it constructs this valid queue.

-----

#### 4\. Final Return

```python
        return result
```

  * The loop finishes, and the function returns the fully constructed `result` list.