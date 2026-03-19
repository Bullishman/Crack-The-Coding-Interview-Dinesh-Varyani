# 120. Swap Nodes In Pairs

**Difficulty**: Medium

**Topics**: Linked List, Recursion

**Link**: https://leetcode.com/problems/swap-nodes-in-pairs

Of course. Let's break down this Python code for swapping pairs in a linked list.

### Algorithm Goal

The function `swapPairs` is designed to modify a linked list by swapping every two adjacent nodes. For example, a list `1 -> 2 -> 3 -> 4` should become `2 -> 1 -> 4 -> 3`.

The specific approach in this code is interesting: instead of re-wiring the `next` pointers of the nodes (which can be complex), it simply **swaps the values (`val`)** between adjacent nodes. This is a simpler and often faster way to achieve the goal if modifying the node's data is acceptable.

### Line-by-Line Code Explanation

Here is a detailed breakdown of each line.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

  * This defines the `Solution` class and the `swapPairs` method which takes the `head` of a linked list as input.

<!-- end list -->

```python
        cur = head
```

  * **Purpose:** Initialize a pointer `cur` (for "current").
  * This pointer will be used to traverse the linked list. It starts at the beginning of the list (`head`).

<!-- end list -->

```python
        while cur and cur.next:
```

  * **Purpose:** This is the main loop condition that controls the traversal.
  * The loop continues as long as there is a valid pair of nodes to swap.
  * **`cur`**: This checks that the current node is not `None`.
  * **`cur.next`**: This checks that the node *following* the current one is also not `None`. If `cur.next` is `None`, it means `cur` is the last node and there's no pair to swap.

<!-- end list -->

```python
            cur.val, cur.next.val = cur.next.val, cur.val
```

  * **Purpose:** This is the core logic that performs the swap.
  * It uses Python's elegant tuple assignment syntax to swap the values of two variables in one line.
  * `cur.val` gets the value from `cur.next.val`.
  * `cur.next.val` gets the value from `cur.val`.
  * For example, if `cur` is node `1` and `cur.next` is node `2`, their values are swapped, so the list becomes `2 -> 1 -> ...`.

<!-- end list -->

```python
            cur = cur.next.next
```

  * **Purpose:** Move the `cur` pointer forward to the next pair.
  * After swapping the pair `(cur, cur.next)`, we need to move to the beginning of the next pair to continue the process.
  * So, we jump two steps ahead: from the current node, past its (now swapped) partner, to the start of the next pair.

<!-- end list -->

```python
        return head
```

  * **Purpose:** Return the head of the modified list.
  * Since this method only changes the `val` attributes of the nodes and doesn't alter the actual node pointers or the structure of the list, the original `head` node is still the starting point of the list.

-----

### Live Trace Table Example

Let's trace the execution with the example linked list: `head = 1 -> 2 -> 3 -> 4 -> NULL`.

**Initial State:**

  * `head` points to Node(1).
  * `cur` points to Node(1).

**Trace Map:**

| Iteration | `cur` (Node Value) | `while cur and cur.next`? | Action | `cur` after move | List Values State |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | 1 | `True` (Node(1) and Node(2) exist) | - | - | `1 -> 2 -> 3 -> 4` |
| **1** | 1 | `True` | Swap values of Node(1) and Node(2). | `cur` becomes `cur.next.next` (Node 3). | `2 -> 1 -> 3 -> 4` |
| **2** | 3 | `True` (Node(3) and Node(4) exist) | Swap values of Node(3) and Node(4). | `cur` becomes `cur.next.next` (NULL). | `2 -> 1 -> 4 -> 3` |
| **3** | `NULL` | `False` (`cur` is `NULL`) | Loop terminates. | - | `2 -> 1 -> 4 -> 3` |

**Final Step:**

1.  The `while` loop condition `while cur and cur.next` is now `False` because `cur` is `NULL`.
2.  The loop exits.
3.  The function executes `return head`.
4.  The original `head` (which was Node 1, but now has the value 2) is returned.

The final modified list is **`2 -> 1 -> 4 -> 3 -> NULL`**.