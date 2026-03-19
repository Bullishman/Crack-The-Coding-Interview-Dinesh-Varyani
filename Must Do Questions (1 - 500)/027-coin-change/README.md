# 27. Climbing Stairs

**Difficulty**: Medium

**Topics**: Math, Dynamic Programming, Memoization

**Link**: https://leetcode.com/problems/coin-change

This code solves the **Coin Change** problem using **Dynamic Programming**. The goal is to find the fewest number of coins needed to make up a specific `amount`. If that amount cannot be reached, it returns -1.

---

### Line-by-Line Breakdown

| Line | Code | Explanation |
| --- | --- | --- |
| **1** | `dp = [0] + [amount + 1] * amount` | **Initialization:** Creates a list `dp` of size `amount + 1`. <br>

<br>• `dp[0] = 0` (0 coins to make amount 0). <br>

<br>• Other indices are set to `amount + 1` (a value larger than any possible answer, representing "infinity"). |
| **2** | `for coin in coins:` | **Outer Loop:** We pick each available coin denomination one by one to see how it can contribute to making various amounts. |
| **3** | `for i in range(coin, amount + 1):` | **Inner Loop:** Iterates through every possible sub-amount `i` that is at least as large as the current `coin` value. |
| **4** | `dp[i] = min(dp[i], dp[i - coin] + 1)` | **The Update Rule:** To make amount `i`, we can either:<br>

<br>1. Use the previous best way (`dp[i]`).<br>

<br>2. Use the current `coin` + however many coins it took to make `i - coin` (`dp[i - coin] + 1`). |
| **5** | `return -1 if dp[amount] == amount + 1 else dp[amount]` | **Final Result:** If `dp[amount]` is still the initial "infinity" value, it means the amount is impossible to make. Otherwise, return the calculated minimum. |

---

### Execution Trace Table

**Input:** `coins = [1, 2, 5]`, `amount = 5`

| Step | Current Coin | Amount `i` | Calculation: `min(dp[i], dp[i - coin] + 1)` | `dp` Array State |
| --- | --- | --- | --- | --- |
| **Init** | - | - | - | `[0, 6, 6, 6, 6, 6]` |
| **1** | **1** | 1 to 5 | `dp[1] = min(6, dp[0]+1) = 1` ... etc. | `[0, 1, 2, 3, 4, 5]` |
| **2** | **2** | 2 | `dp[2] = min(2, dp[0]+1) = 1` | `[0, 1, 1, 3, 4, 5]` |
| **3** | **2** | 3 | `dp[3] = min(3, dp[1]+1) = 2` | `[0, 1, 1, 2, 4, 5]` |
| **4** | **2** | 4 | `dp[4] = min(4, dp[2]+1) = 2` | `[0, 1, 1, 2, 2, 5]` |
| **5** | **2** | 5 | `dp[5] = min(5, dp[3]+1) = 3` | `[0, 1, 1, 2, 2, 3]` |
| **6** | **5** | 5 | `dp[5] = min(3, dp[0]+1) = 1` | `[0, 1, 1, 2, 2, 1]` |

**Final Result:** `dp[5] = 1` (Using one 5-cent coin).

---

### Key Logic: `dp[i - coin] + 1`

This is the heart of the algorithm. It says: "If I use this current coin, the total number of coins I need is **1** (for the coin I just picked) plus **however many coins it took to make the remaining balance** (`i - coin`)." By doing this for every coin, we guarantee we find the absolute minimum.

Would you like to see how this logic changes if we wanted to find the **total number of ways** to make the amount instead of the minimum number of coins?