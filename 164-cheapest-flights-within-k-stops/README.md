# 164. Cheapest Flights Within K Stops

**Difficulty**: Medium

**Topics**: Dynamic Programming, Depth-First Search, Breadth-First Search, Graph, Heap (Priority Queue), Shortest Path

**Link**: https://leetcode.com/problems/cheapest-flights-within-k-stops

Of course. Let's do a detailed, line-by-line breakdown of this code for finding the cheapest flight with at most `k` stops.

### The Logic: Modified Bellman-Ford Algorithm

The code uses a dynamic programming approach that is a variation of the **Bellman-Ford algorithm**. The standard Bellman-Ford algorithm finds the shortest path from a source to all other nodes. This version is specifically adapted to handle the constraint of a maximum number of stops.

1.  **Cost Initialization:** We use a dictionary (or an array) called `cost` to store the cheapest price found *so far* to reach each city from the source. We initialize the cost to our starting city (`src`) as `0` and all others to infinity.

2.  **Iterating by Stops:** The main idea is to build up the solution level by level. The outer loop `for _ in range(k + 1):` is the key. It iterates `k + 1` times.

      * The first iteration (`_ = 0`) finds the cheapest prices you can get with **at most 0 stops**.
      * The second iteration (`_ = 1`) finds the cheapest prices with **at most 1 stop**, using the results from the 0-stop iteration.
      * ...and so on, up to `k` stops.

3.  **The "Relaxation" Step:** Inside the loop, we iterate through every flight (`frm, to, price`). This is called the "relaxation" step. For each flight, we check:

    > "Is the cost to get to the starting city (`frm`) of this flight, plus the `price` of this flight, cheaper than the currently known cheapest cost to get to the destination city (`to`)?"

4.  **Using a Temporary Copy:** It's crucial that we use `temp_cost` to store the new prices for the current iteration. Why? Because all calculations for paths with `i` stops must be based *only* on the results from paths with `i-1` stops. If we updated the main `cost` array directly, a cheaper path found in the current iteration could improperly influence other calculations within the *same* iteration, effectively giving us more stops than allowed for that step.

### The Example

Let's trace the execution with the following scenario:

  * `n = 4` (cities 0, 1, 2, 3)
  * `flights = [[0,1,100], [1,2,100], [0,2,500], [2,3,100]]`
  * `src = 0`
  * `dst = 3`
  * `k = 1` (meaning we can make at most one stop)

**The Graph:**

```
      100
(0) -----> (1)
 | \         | 100
 |  \        |
500  \       v
 |    `>----(2)
 |           | 100
 v           v
...         (3)
```

The goal is to get from city `0` to `3` with at most `1` stop. The only such path is `0 -> 2 -> 3` with a total cost of `500 + 100 = 600`.

-----

### Code and Live Demonstration

#### 1\. Initialization

```python
        # (Assuming necessary imports: collections, math)
        cost = collections.defaultdict(lambda: math.inf)
        cost[src] = 0
```

  * **Initial `cost` state:** `{0: 0}` (All other cities implicitly have a cost of `inf`).

#### 2\. The Main Loop (`for _ in range(k + 1)`)

Since `k=1`, this loop will run for `_ = 0` and `_ = 1`.

-----

### **Live Trace Table Map**

#### **Iteration 1: `_ = 0` (Finding cheapest price with at most 0 stops)**

  * `temp_cost` is created as a copy of `cost`: `{0: 0}`.
  * The inner loop iterates through all flights.

| Flight `(frm, to, price)` | `cost[frm]` | `cost[frm] + price` | `temp_cost[to]` (before) | `cost[frm] + price < temp_cost[to]`? | `temp_cost[to]` (after) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `(0, 1, 100)` | 0 | 100 | `inf` | **True** | **100** |
| `(1, 2, 100)` | `inf`| `inf`| `inf` | False | `inf` |
| `(0, 2, 500)` | 0 | 500 | `inf` | **True** | **500** |
| `(2, 3, 100)` | `inf`| `inf`| `inf` | False | `inf` |

  * After the inner loop, we update `cost`:
    ```python
    cost = temp_cost
    ```
  * **State of `cost` after 0 stops:** `{0: 0, 1: 100, 2: 500}`. This means from `src=0`, we can reach city 1 for 100 and city 2 for 500 with no stops.

-----

#### **Iteration 2: `_ = 1` (Finding cheapest price with at most 1 stop)**

  * `temp_cost` is a copy of the current `cost`: `{0: 0, 1: 100, 2: 500}`.
  * The inner loop iterates through all flights again.

| Flight `(frm, to, price)` | `cost[frm]` | `cost[frm] + price` | `temp_cost[to]` (before) | `cost[frm] + price < temp_cost[to]`? | `temp_cost[to]` (after) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `(0, 1, 100)` | 0 | 100 | 100 | False | 100 |
| `(1, 2, 100)` | 100 | **200** | 500 | **True** | **200** |
| `(0, 2, 500)` | 0 | 500 | 200 | False | 200 |
| `(2, 3, 100)` | 500 | **600** | `inf` | **True** | **600** |

  * After the inner loop, we update `cost`:
    ```python
    cost = temp_cost
    ```
  * **Final state of `cost` after 1 stop:** `{0: 0, 1: 100, 2: 200, 3: 600}`. This now reflects the cheapest prices with at most one stop. For example, to get to city 2, it's now cheaper to go `0 -> 1 -> 2` for a cost of 200. To get to city 3, we can now go `0 -> 2 -> 3` for a cost of 600.

The outer loop finishes.

-----

### 3\. Final Return

```python
        return cost[dst] if cost[dst] != math.inf else -1
```

  * `dst` is `3`. We look up `cost[3]`.
  * The value is `600`.
  * The condition `600 != math.inf` is **True**.
  * The function returns **600**, which is the correct cheapest price.