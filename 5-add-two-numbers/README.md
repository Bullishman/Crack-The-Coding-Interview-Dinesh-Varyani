# 5. Add Two Numbers

**Difficulty**: Medium

**Topics**: Linked List, Math, Recursion

**Link**: https://leetcode.com/problems/add-two-numbers

Of course. This code solves the "Add Two Numbers" problem where the numbers are represented by linked lists with digits in reverse order.

### The Core Idea

The strategy used in this specific code is to:

1.  Convert each linked list into a standard integer.
2.  Add the two integers together using normal arithmetic.
3.  Convert the resulting sum back into a new linked list in the required reverse-digit format.

**Note:** While this approach is intuitive, it can be problematic in languages with fixed-size integers, as the linked lists can represent numbers too large to fit. Python's arbitrary-precision integers handle this, but the standard solution for this problem usually involves a digit-by-digit sum with a `carry`.

Let's break down this code line by line with an example.

**Example:**

  * `l1` represents `342`: `2 -> 4 -> 3 -> None`
  * `l2` represents `465`: `5 -> 6 -> 4 -> None`
  * **Expected Result:** `342 + 465 = 807`, which should be a linked list: `7 -> 0 -> 8 -> None`.

-----

### **The `addTwoNumbers` (Outer) Function**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
```

This defines the main function which takes the heads of the two linked lists, `l1` and `l2`.

#### **Part 1: The `toint` Helper Function**

```python
        def toint(node: ListNode) -> int:
            return node.val + (10 * toint(node.next)) if node else 0
```

  * **What it does:** This is a recursive helper function that converts a reversed-digit linked list into a regular integer.
  * **`if node else 0`**: This is the base case. If the function receives a `None` node (the end of a list), it returns 0.
  * **`node.val + (10 * toint(node.next))`**: This is the recursive step. It takes the current node's value and adds it to 10 times the value of the rest of the list.

**Tracing `toint(l1)` where `l1` is `2 -> 4 -> 3`:**

1.  `toint(Node(2))` calls `toint(Node(4))`
2.  `toint(Node(4))` calls `toint(Node(3))`
3.  `toint(Node(3))` calls `toint(None)`
4.  `toint(None)` hits the base case and returns `0`.
5.  `toint(Node(3))` returns `3 + (10 * 0) = 3`.
6.  `toint(Node(4))` returns `4 + (10 * 3) = 34`.
7.  `toint(Node(2))` returns `2 + (10 * 34) = 342`.

#### **Part 2: Summing the Numbers**

```python
        n = toint(l1) + toint(l2)
```

  * **What it does:** This line calls the `toint` helper on both input lists and adds the results.
  * **For our example:**
      * `toint(l1)` returns `342`.
      * `toint(l2)` returns `465`.
      * `n` becomes `342 + 465 = 807`.

#### **Part 3: Creating the Result List**

```python
        root = head = ListNode(n % 10)
```

  * **`n % 10`**: The modulo operator gets the last digit of the sum (`807 % 10` is `7`). This is the first node of our result list.
  * `ListNode(...)`: A new node is created with this value.
  * `root = head = ...`: Two pointers, `root` and `head`, are set to this new node. `root` will always point to the start of our new list so we can return it later. `head` will be used as a moving pointer to build the rest of the list.

**After this line:**

  * `n = 807`
  * `root` -\> `Node(7)`
  * `head` -\> `Node(7)`

<!-- end list -->

```python
        while n > 9:
```

This loop continues as long as there are more digits left in our sum `n` (i.e., `n` is 10 or greater).

```python
            n //= 10
```

  * Integer division by 10 effectively "chops off" the last digit of `n`.
  * **First iteration:** `n = 807 // 10` becomes `80`.

<!-- end list -->

```python
            head.next = head = ListNode(n % 10)
```

  * This is a chained assignment that does three things in order from right to left:
    1.  **`ListNode(n % 10)`**: A new node is created. In the first iteration, `n` is `80`, so `80 % 10` is `0`. A `Node(0)` is created.
    2.  **`head = ...`**: The `head` pointer is updated to point to this new `Node(0)`.
    3.  **`head.next = ...`**: The `next` attribute of the *previous* `head` (which was `Node(7)`) is set to point to the new `head` (`Node(0)`).
  * This appends a new node to the end of the list and advances the `head` pointer to the new end.

#### **Final Return**

```python
        return root
```

After the loop finishes, the complete list has been built. We return `root`, which has remained at the true start of the new list all along.

-----

### **Live Trace Table Map for List Creation**

This table traces the creation of the result list from the sum `n = 807`.

| State | `n` | `n > 9`? | Action | List Structure | `root` pointer | `head` pointer |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Initial** | 807 | - | `root=head=ListNode(7)` | `(7)` | `(7)` | `(7)` |
| **Loop 1** | 807 | Yes | `n` becomes `80`. Create `Node(0)`. Set `(7).next` to `(0)`. Move `head` to `(0)`. | `(7) -> (0)` | `(7)` | `(0)` |
| **Loop 2** | 80 | Yes | `n` becomes `8`. Create `Node(8)`. Set `(0).next` to `(8)`. Move `head` to `(8)`. | `(7) -> (0) -> (8)`| `(7)` | `(8)` |
| **End of Loop** | 8 | No | Loop terminates. | `(7) -> (0) -> (8)`| `(7)` | `(8)` |

The function returns `root`, which points to the list `7 -> 0 -> 8`.