# 127. Best Time To Buy And Sell Stock With Cooldown

**Difficulty**: Medium

**Topics**: Array, Dynamic Programming

**Link**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

Of course. Let's break down this clever dynamic programming solution for the "Best Time to Buy and Sell Stock with Cooldown" problem.

### The Logic: State Machine

This code uses a state machine approach with three key states, tracked by variables, representing the maximum profit you could have at the end of any given day:

  * `hold`: The maximum profit if, at the end of today, you are **holding** a stock.
  * `sell`: The maximum profit if, at the end of today, you are **not holding** a stock (and are free to buy tomorrow, or are in a "cooldown" period).
  * `prev`: The previous `sell` state. This is crucial because if you want to buy today, you must have been in the `sell` state *yesterday*. But to calculate that, you need the profit from *before* yesterday due to the one-day cooldown period after selling.

The algorithm iterates through the prices day by day, calculating the best possible profit for each state.

### The Example

Let's trace the code with the classic example for this problem:

  * `prices = [1, 2, 3, 0, 2]`

The optimal strategy here is:

1.  Buy at `1`.
2.  Sell at `2` (Profit: +1).
3.  Cooldown on day 3 (price `3`).
4.  Buy at `0`.
5.  Sell at `2` (Profit: +2).
6.  Total Profit = `1 + 2 = 3`.

Let's see how the code arrives at this.

-----

### Code and Live Demonstration

#### 1\. Initialization

```python
        # Initial state before day 1
        prev, sell, hold = 0, 0, -float('inf')
```

  * `sell = 0`: Before we start, our profit from not holding stock is 0.
  * `hold = -float('inf')`: We set `hold` to negative infinity because it's impossible to be holding a stock before the first day. This prevents us from selling a stock we don't own.
  * `prev = 0`: This tracks the `sell` state from the day *before* the previous day. Initially, it's also 0.

-----

### **Live Trace Table Map**

We will now trace the state of our variables as we loop through each price.

| Day | `price` | Initial `prev` | Initial `sell` | Initial `hold` | `temp` | New `sell` Calculation | New `hold` Calculation | New `prev` | Final `sell` | Final `hold` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | - | 0 | 0 | -inf | - | - | - | - | 0 | -inf |
| **1** | **1** | 0 | 0 | -inf | 0 | `max(0, -inf + 1)` = 0 | `max(-inf, 0 - 1)` = -1 | 0 | **0** | **-1** |
| **2** | **2** | 0 | 0 | -1 | 0 | `max(0, -1 + 2)` = 1 | `max(-1, 0 - 2)` = -1 | 0 | **1** | **-1** |
| **3** | **3** | 0 | 1 | -1 | 1 | `max(1, -1 + 3)` = 2 | `max(-1, 0 - 3)` = -1 | 1 | **2** | **-1** |
| **4** | **0** | 1 | 2 | -1 | 2 | `max(2, -1 + 0)` = 2 | `max(-1, 1 - 0)` = 1 | 2 | **2** | **1** |
| **5** | **2** | 2 | 2 | 1 | 2 | `max(2, 1 + 2)` = 3 | `max(1, 2 - 2)` = 1 | 2 | **3** | **1** |

-----

### **Detailed Line-by-Line Breakdown**

#### Day 1: `price = 1`

  * `temp = sell` -\> `temp` becomes `0`.
  * `sell = max(sell, hold + price)` -\> `max(0, -inf + 1)` -\> `sell` remains `0`. (We can't sell, so we do nothing).
  * `hold = max(hold, prev - price)` -\> `max(-inf, 0 - 1)` -\> `hold` becomes `-1`. (We buy the stock for 1, so our "profit" is -1).
  * `prev = temp` -\> `prev` becomes `0`.
  * **End of Day 1**: Max profit if holding is -1. Max profit if not holding is 0.

#### Day 2: `price = 2`

  * `temp = sell` -\> `temp` becomes `0`.
  * `sell = max(sell, hold + price)` -\> `max(0, -1 + 2)` -\> `sell` becomes `1`. (Selling is better than doing nothing. Profit is 1).
  * `hold = max(hold, prev - price)` -\> `max(-1, 0 - 2)` -\> `hold` remains `-1`. (Continuing to hold from yesterday is better than buying again at price 2).
  * `prev = temp` -\> `prev` becomes `0`.
  * **End of Day 2**: Max profit if holding is -1. Max profit if not holding (because we sold) is 1.

#### Day 3: `price = 3`

  * `temp = sell` -\> `temp` becomes `1`.
  * `sell = max(sell, hold + price)` -\> `max(1, -1 + 3)` -\> `sell` becomes `2`. (Selling is better than resting. Our profit would be 2).
  * `hold = max(hold, prev - price)` -\> `max(-1, 0 - 3)` -\> `hold` remains `-1`. (Continuing to hold is better than buying).
  * `prev = temp` -\> `prev` becomes `1`.
  * **End of Day 3**: The best `sell` state is now 2. `prev` is now 1, storing the `sell` state from Day 2.

#### Day 4: `price = 0`

  * `temp = sell` -\> `temp` becomes `2`.
  * `sell = max(sell, hold + price)` -\> `max(2, -1 + 0)` -\> `sell` remains `2`. (We are in cooldown from selling yesterday, so we rest).
  * `hold = max(hold, prev - price)` -\> `max(-1, 1 - 0)` -\> `hold` becomes `1`. (It's optimal to buy. `prev` was 1, so our profit after buying for 0 is `1 - 0 = 1`).
  * `prev = temp` -\> `prev` becomes `2`.
  * **End of Day 4**: We bought at 0. Max profit if holding is 1.

#### Day 5: `price = 2`

  * `temp = sell` -\> `temp` becomes `2`.
  * `sell = max(sell, hold + price)` -\> `max(2, 1 + 2)` -\> `sell` becomes `3`. (We sell the stock we bought for 0 at price 2. Our total profit is `1 + 2 = 3`).
  * `hold = max(hold, prev - price)` -\> `max(1, 2 - 2)` -\> `hold` remains `1`. (Continuing to hold is better than buying again).
  * `prev = temp` -\> `prev` becomes `2`.
  * **End of Day 5**: The maximum profit we can achieve is 3, by being in the `sell` state.

-----

#### 2\. Final Return

```python
        return sell
```

  * The loop finishes. The final value of `sell` is `3`.
  * The maximum profit must come from a state where we are not holding any stock (i.e., we have sold everything).
  * The function returns **3**.