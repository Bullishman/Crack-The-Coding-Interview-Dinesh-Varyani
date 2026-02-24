# 166. Remove K Digits

**Difficulty**: Medium

**Topics**: String, Stack, Greedy, Monotonic Stack

**Link**: https://leetcode.com/problems/remove-k-digits

This code uses a **Monotonic Stack** pattern. The core idea is greedy: to get the smallest possible number, we want the most significant digits (the ones on the left) to be as small as possible. If we see a smaller digit that can replace a larger digit to its left, we drop the larger digit.

Here is the line-by-line breakdown, followed by the execution map.

### Line-by-Line Breakdown

* **`class Solution:`** Standard wrapper class for LeetCode problems.
* **`def removeKdigits(self, num: str, k: int) -> str:`** The main function taking the numeric string `num` and the integer `k` (digits to remove).
* **`res = []`** Initializes an empty list that will act as our **stack**. We will build our final number here, digit by digit.
* **`counter = 0`** Initializes a variable. *(Note: This variable is actually never used in the rest of the code! It can be safely deleted).*
* **`n = len(num)`** Stores the total number of digits in the original string.
* **`if n == k: return "0"`** **Edge Case:** If we are asked to remove exactly as many digits as there are in the string, the result is empty, which represents `"0"`.
* **`for i in range(n):`** Starts a loop to process every single digit in the string `num` from left to right.
* **`while k and res and res[-1] > num[i]:`** The core logic. It runs as long as:
1. We still have digits left to remove (`k > 0`).
2. The stack is not empty (`res`).
3. The *last* digit we put in the stack (`res[-1]`) is strictly *greater* than the current digit (`num[i]`).


* **`res.pop()`** If the while condition is met, we remove the larger digit from the top of the stack.
* **`k -= 1`** We successfully removed a digit, so we decrement `k`. (The `while` loop will keep popping until it finds a smaller digit or runs out of `k`).
* **`res.append(num[i])`** After dropping any larger preceding digits, we push the current digit onto the stack.
* **`while k:`** After the `for` loop finishes, what if we *still* need to remove digits? (e.g., The input was already sorted like `"12345"`, so the first `while` loop never triggered).
* **`res.pop()` / `k -= 1**` We just chop off the remaining `k` digits from the end (the largest digits).
* **`return "".join(res).lstrip('0') or "0"`** * `"".join(res)`: Converts the stack list back into a single string.
* `.lstrip('0')`: Strips away any leading zeros (e.g., `"0200"` becomes `"200"`).
* `or "0"`: If stripping zeros leaves us with an empty string (e.g., the answer was `"000"`), Python evaluates it as falsy, and returns `"0"` instead.



---

### Step-by-Step Execution Map

Let's trace this with a classic example:
**Input:** `num = "1432219"`, `k = 3`

| Loop `i` | Digit `num[i]` | Stack Before | `res[-1] > num[i]`? | Action (Inside `while`) | Stack After | `k` Left |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | `'1'` | `[]` | No (Stack empty) | - | `['1']` | 3 |
| 1 | `'4'` | `['1']` | `'1' > '4'` (False) | - | `['1', '4']` | 3 |
| 2 | `'3'` | `['1', '4']` | `'4' > '3'` (**True**) | **Pop `'4'`, `k-1**` | `['1']` | 2 |
|  |  | `['1']` | `'1' > '3'` (False) | Push `'3'` | `['1', '3']` | 2 |
| 3 | `'2'` | `['1', '3']` | `'3' > '2'` (**True**) | **Pop `'3'`, `k-1**` | `['1']` | 1 |
|  |  | `['1']` | `'1' > '2'` (False) | Push `'2'` | `['1', '2']` | 1 |
| 4 | `'2'` | `['1', '2']` | `'2' > '2'` (False) | Push `'2'` | `['1', '2', '2']` | 1 |
| 5 | `'1'` | `['1', '2', '2']` | `'2' > '1'` (**True**) | **Pop `'2'`, `k-1**` | `['1', '2']` | 0 |
|  |  | `['1', '2']` | `k` is 0 (Stop loop) | Push `'1'` | `['1', '2', '1']` | 0 |
| 6 | `'9'` | `['1', '2', '1']` | `k` is 0 (Stop loop) | Push `'9'` | `['1', '2', '1', '9']` | 0 |

**Final Cleanup Steps:**

* `while k:` evaluates to False (since `k=0`), so no extra popping from the end is needed.
* `"".join(res)` becomes `"1219"`.
* `.lstrip('0')` leaves it as `"1219"`.

---

Would you like to trace a tricky edge case using this table format, such as an input with leading zeros (like `num = "10200", k = 1`) or an already sorted input (like `num = "12345", k = 2`)?