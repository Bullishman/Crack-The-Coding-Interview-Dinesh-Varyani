# 121. Reverse Linked List Ii

**Difficulty**: Medium

**Topics**: Linked List

**Link**: https://leetcode.com/problems/reverse-linked-list-ii

Of course. This code provides a very clear and well-commented implementation for reversing a portion of a linked list. Let's break it down in detail.

### Algorithm Goal

The function `reverseBetween` is designed to reverse the nodes of a linked list from a starting position `left` to an ending position `right`. It achieves this by cleverly re-wiring the `next` pointers of the nodes in place, which is a memory-efficient approach.

The strategy is:

1.  **Use a Dummy Node:** A `dummy` node is placed before the actual `head`. This is a powerful trick that standardizes the logic, especially for the edge case where the reversal starts from the very first node (`left = 1`).
2.  **Find the Starting Point:** A pointer, `prev`, is moved to the node *just before* the section to be reversed. This node's `next` pointer is the one we will manipulate to attach the reversed sublist.
3.  **Iterative Reversal:** The code then iterates `right - left` times. In each iteration, it takes the node that needs to be moved to the front of the sublist, detaches it, and re-inserts it right after `prev`.

### Line-by-Line Code Explanation

Let's go through the code block by block.

```python
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
```

  * Defines the class `Solution` and the method `reverseBetween`.

<!-- end list -->

```python
        if not head or left == right:
            return head
```

  * **Purpose:** Handle simple edge cases. If the list is empty or the sublist to reverse has only one element (`left == right`), no action is needed, so we return the original `head`.

<!-- end list -->

```python
        # Step 1: Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
```

  * **Purpose:** Set up a dummy node to simplify pointer manipulation.
  * **`dummy = ListNode(0)`**: Creates a new node that will sit before the actual `head`.
  * **`dummy.next = head`**: Links the dummy node to the start of the list. The list is now: `Dummy -> 1 -> 2 -> ...`
  * **`prev = dummy`**: Initializes a pointer `prev`. This pointer's job is to find and "anchor" the position just before the reversal starts.

<!-- end list -->

```python
        # Step 2: Move `prev` just before the `left` position
        for _ in range(left - 1):
            prev = prev.next
```

  * **Purpose:** Position the `prev` pointer correctly.
  * The loop runs `left - 1` times. For example, if `left = 2`, it runs once, moving `prev` from `dummy` to `Node(1)`. After this loop, `prev` is pointing to the node that will precede the reversed section.

<!-- end list -->

```python
        # Step 3: Reverse sublist from left to right
        curr = prev.next
```

  * **Purpose:** Initialize the `curr` pointer.
  * `curr` points to the first node of the sublist to be reversed (the node at position `left`). This pointer will mark the effective "tail" of the reversing section, as nodes will be moved from *after* `curr` to *before* it.

<!-- end list -->

```python
        for _ in range(right - left):
```

  * **Purpose:** This is the main loop that performs the reversal. It iterates exactly as many times as there are nodes to move.

Let's look at the four crucial lines inside this loop:

```python
            temp = curr.next        # node to move
```

  * **1. Identify the node to move:** A `temp` pointer is created to hold the node that will be moved to the front. This is always the node immediately following `curr`.

<!-- end list -->

```python
            curr.next = temp.next     # remove temp from sublist
```

  * **2. Detach the node:** `curr`'s `next` pointer bypasses `temp` and points to whatever `temp` was pointing to. This effectively removes `temp` from its current position in the list.

<!-- end list -->

```python
            temp.next = prev.next     # insert temp after prev
```

  * **3. Point the moved node forward:** The `next` pointer of our moved node (`temp`) is set to point to what `prev` is currently pointing to. This links `temp` to the beginning of the sublist.

<!-- end list -->

```python
            prev.next = temp          # move temp to front of sublist
```

  * **4. Point the anchor node backward:** `prev`'s `next` pointer is now updated to point to `temp`. This completes the insertion of `temp` at the front of the sublist.

<!-- end list -->

```python
        return dummy.next
```

  * **Purpose:** Return the correct head of the modified list.
  * Because of the dummy node, `dummy.next` will always point to the true head of the list, even if the original `head` (Node 1) was part of the reversal.

-----

### Live Trace Table Example

Let's trace with `head = 1 -> 2 -> 3 -> 4 -> 5 -> NULL`, `left = 2`, `right = 4`.
The goal is to transform the list into `1 -> 4 -> 3 -> 2 -> 5`.

**Initial Setup:**

1.  List: `dummy -> 1 -> 2 -> 3 -> 4 -> 5`
2.  `prev` points to `dummy`.
3.  **Step 2:** Loop runs `left - 1 = 1` time. `prev` moves to `Node(1)`.
4.  **Step 3:** `curr` is set to `prev.next`, so `curr` points to `Node(2)`.

**Pointers Before Reversal Loop:**

  * `prev` -\> `Node(1)`
  * `curr` -\> `Node(2)`

**Reversal Loop: `for _ in range(right - left)`** (runs `4 - 2 = 2` times)

| Iteration | Pointers | Step 3.1: `temp = curr.next` | Step 3.2: `curr.next = temp.next` | Step 3.3: `temp.next = prev.next` | Step 3.4: `prev.next = temp` | List State (visual) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | `prev` -\> 1\<br/\>`curr` -\> 2 | - | - | - | - | `dummy -> 1 -> 2 -> 3 -> 4 -> 5` |
| **1**\<br/\>(Move Node 3) | `prev` -\> 1\<br/\>`curr` -\> 2 | `temp` -\> 3 | `curr`(2) now points to 4 | `temp`(3) now points to `prev.next`(2) | `prev`(1) now points to `temp`(3) | `dummy -> 1 -> 3 -> 2 -> 4 -> 5` |
| **2**\<br/\>(Move Node 4) | `prev` -\> 1\<br/\>`curr` -\> 2 | `temp` -\> 4 | `curr`(2) now points to 5 | `temp`(4) now points to `prev.next`(3) | `prev`(1) now points to `temp`(4) | `dummy -> 1 -> 4 -> 3 -> 2 -> 5` |

**Final Step:**

1.  The loop finishes.
2.  The function returns `dummy.next`.
3.  `dummy.next` points to `Node(1)`.

The final returned list is **`1 -> 4 -> 3 -> 2 -> 5 -> NULL`**.