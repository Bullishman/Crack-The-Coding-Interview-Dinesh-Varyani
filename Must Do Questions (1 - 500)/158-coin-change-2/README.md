# 158. Coin Change 2

**Difficulty**: Medium

**Topics**: Array, Dynamic Programming

**Link**: https://leetcode.com/problems/coin-change-2

Of course. Let's do a detailed, line-by-line breakdown of this classic dynamic programming solution for the "Coin Change 2" problem, which asks for the number of combinations to make up an amount.

### The Logic: Bottom-Up Dynamic Programming

This code uses a 1D array (a DP table) to solve the problem efficiently. The core idea is that `dp[i]` will store the number of unique combinations of coins that can sum up to the amount `i`.

1.  **Initialization:** The `dp` array is created with a size of `amount + 1`.
      * `dp[0]` is set to `1`. This is the crucial base case. It represents the idea that there is exactly **one** way to make an amount of 0: by choosing no coins.
      * All other `dp[i]` are initialized to `0`.
2.  **Outer Loop (Iterating through Coins):** The algorithm processes one coin at a time. This is very important. By building up the `dp` table using one coin before moving to the next, we prevent counting duplicate combinations (like `1+2` and `2+1`).
3.  **Inner Loop (Iterating through Amounts):** For the current `coin`, the inner loop updates the `dp` array. For each amount `i` from `coin` up to the total `amount`, it performs the update:
      * `dp[i] += dp[i - coin]`
      * **What this means:** The new number of ways to make amount `i` is the old number of ways to make `i` (using the *previous* coins) **plus** the number of ways to make the amount `i - coin`. Why? Because every combination that could make `i - coin` can now be turned into a combination that makes `i` by simply adding the current `coin`.

### The Example

Let's trace the execution with a standard example:

  * `amount = 5`
  * `coins = [1, 2, 5]`

The unique combinations are:

  * `1+1+1+1+1`
  * `1+1+1+2`
  * `1+2+2`
  * `5`

The expected result is **4**.

-----

### Code and Live Demonstration

#### 1\. Initialization

```python
        dp = [1] + [0] * amount
        # amount is 5
        # dp becomes [1, 0, 0, 0, 0, 0]
```

  * The `dp` array represents the number of combinations for amounts `0, 1, 2, 3, 4, 5`.

-----

#### 2\. Outer Loop: `for coin in coins:`

This is the main loop that will iterate three times, once for each coin.

-----

### **Live Trace Table Map**

This table shows the state of the `dp` array after each full pass of the outer loop (after each coin is processed).

| `dp` Array State | Index 0 | Index 1 | Index 2 | Index 3 | Index 4 | Index 5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Initial** | 1 | 0 | 0 | 0 | 0 | 0 |
| **After coin=1** | 1 | 1 | 1 | 1 | 1 | 1 |
| **After coin=2** | 1 | 1 | 2 | 2 | 3 | 3 |
| **After coin=5** | 1 | 1 | 2 | 2 | 3 | **4** |

-----

### **Detailed Line-by-Line Breakdown of Loops**

#### Outer Loop 1: `coin = 1`

  * The inner loop `for i in range(1, 6)` runs. The update rule is `dp[i] += dp[i - 1]`.

| `i` | `dp[i - 1]` | Calculation: `dp[i] = dp[i] + dp[i-1]` | `dp` Array State |
| :-- | :--- | :--- | :--- |
| **1** | `dp[0]=1` | `dp[1] = 0 + 1 = 1` | `[1, 1, 0, 0, 0, 0]` |
| **2** | `dp[1]=1` | `dp[2] = 0 + 1 = 1` | `[1, 1, 1, 0, 0, 0]` |
| **3** | `dp[2]=1` | `dp[3] = 0 + 1 = 1` | `[1, 1, 1, 1, 0, 0]` |
| **4** | `dp[3]=1` | `dp[4] = 0 + 1 = 1` | `[1, 1, 1, 1, 1, 0]` |
| **5** | `dp[4]=1` | `dp[5] = 0 + 1 = 1` | `[1, 1, 1, 1, 1, 1]` |

  * **End of Pass 1**: The `dp` array shows that using only the coin `1`, there is exactly one way to make any amount.

-----

#### Outer Loop 2: `coin = 2`

  * The inner loop `for i in range(2, 6)` runs. The update rule is `dp[i] += dp[i - 2]`.

| `i` | `dp[i - 2]` | Calculation: `dp[i] = dp[i] + dp[i-2]` | `dp` Array State |
| :-- | :--- | :--- | :--- |
| **2** | `dp[0]=1` | `dp[2] = 1 + 1 = 2` | `[1, 1, 2, 1, 1, 1]` |
| **3** | `dp[1]=1` | `dp[3] = 1 + 1 = 2` | `[1, 1, 2, 2, 1, 1]` |
| **4** | `dp[2]=2` | `dp[4] = 1 + 2 = 3` | `[1, 1, 2, 2, 3, 1]` |
| **5** | `dp[3]=2` | `dp[5] = 1 + 2 = 3` | `[1, 1, 2, 2, 3, 3]` |

  * **End of Pass 2**: The table is updated with new combinations that include the coin `2`. For example, `dp[4]` is now `3`. The 3 combinations are (`1+1+1+1`), (`1+1+2`), and (`2+2`).

-----

#### Outer Loop 3: `coin = 5`

  * The inner loop `for i in range(5, 6)` runs just once. The update rule is `dp[i] += dp[i - 5]`.

| `i` | `dp[i - 5]` | Calculation: `dp[i] = dp[i] + dp[i-5]` | `dp` Array State |
| :-- | :--- | :--- | :--- |
| **5** | `dp[0]=1` | `dp[5] = 3 + 1 = 4` | `[1, 1, 2, 2, 3, 4]` |

  * **End of Pass 3**: The final combination using the coin `5` is added. The `3` old ways to make `5` are (`1+1+1+1+1`), (`1+1+1+2`), (`1+2+2`). We add `dp[0]` which is `1` (representing the single combination "use a 5 coin and find ways to make 0"), giving us the 4th way.

-----

### 3\. Final Return

```python
        return dp[amount]
```

  * The loops are finished.
  * The function returns the value at the last index of the `dp` array, `dp[5]`.
  * The value is **4**, which is the correct number of combinations.