# 102. Sort List

**Difficulty**: Medium

**Topics**: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort

**Link**: https://leetcode.com/problems/sort-list

Of course. Let's break down this code for sorting a singly-linked list.

### High-Level Overview

The provided code sorts a linked list using a simple and intuitive, though not the most space-efficient, method. The strategy can be broken down into three main steps:

1.  **Extract:** Traverse the entire linked list from head to tail. As each node is visited, extract its value and store it in a standard Python list (an array).
2.  **Sort:** Use Python's highly optimized built-in `list.sort()` method to sort the list of extracted values. This happens in memory, completely separate from the linked list structure.
3.  **Overwrite:** Traverse the linked list a second time from the head. As each node is visited, update its value with the corresponding value from the now-sorted list.

Essentially, it converts the linked list problem into an array-sorting problem and then maps the solution back onto the original linked list structure.

-----

### Prerequisites: The ListNode

For the examples to be clear, we need the `ListNode` class definition and a helper function to print the list's contents.

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to print the linked list
def print_list(head: Optional[ListNode]):
    if not head:
        print("Empty List")
        return
    nodes = []
    curr = head
    while curr:
        nodes.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(nodes))
```

-----

### Line-by-Line Code Explanation

Here is the code with comments explaining the purpose of each line.

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Line 1: lst: List = []
        # Initialize an empty Python list. This will be used to store the
        # values from the linked list nodes.
        lst: List = []
        
        # Line 2: cur = head
        # Create a pointer `cur` (for "current") and set it to the head of the
        # linked list. This pointer will be used to traverse the list.
        cur = head
        
        # Line 3: while cur:
        # Start a loop that will continue as long as `cur` is not None,
        # meaning we haven't reached the end of the list yet.
        while cur:
            
            # Line 4: lst.append(cur.val)
            # Take the value of the current node (`cur.val`) and append it
            # to our Python list `lst`.
            lst.append(cur.val)
            
            # Line 5: cur = cur.next
            # Move the `cur` pointer one step forward to the next node in the list.
            cur = cur.next
        
        # At this point, the loop is finished and `lst` contains all the values
        # from the linked list, in their original order.
        
        # Line 6: lst.sort()
        # Use the built-in sort method to sort the Python list `lst` in ascending order.
        # This is a highly efficient sort (Timsort, O(N log N)).
        lst.sort()
        
        # Line 7: cur = head
        # Reset the `cur` pointer back to the head of the linked list
        # to begin a second traversal.
        cur = head
        
        # Line 8: for i in range(len(lst)):
        # Start a `for` loop that iterates from `i = 0` to the length of the list minus one.
        # This loop will run exactly once for each node in the list.
        for i in range(len(lst)):
            
            # Line 9: cur.val = lst[i]
            # Overwrite the value of the current node (`cur.val`) with the
            # sorted value at index `i` from our Python list `lst`.
            cur.val = lst[i]
            
            # Line 10: cur = cur.next
            # Move the `cur` pointer to the next node, just like before.
            cur = cur.next
        
        # At this point, the second loop is finished, and all node values in the
        # original linked list have been updated with the sorted values.
        
        # Line 11: return head
        # Return the head of the modified linked list. The structure of the list
        # (the pointers) is unchanged, but the values are now sorted.
        return head
```

-----

### Example Walkthrough

Let's trace the code with an unsorted linked list.

**Initial State:** `head -> 4 -> 2 -> 1 -> 3 -> None`

#### Live Trace Table Map

The process can be broken into three phases.

**Phase 1: Extracting Values into the List** (Lines 2-5)

| Line \# | Code Executed       | State of `cur` | State of `lst`    | Condition Check (`while cur`) |
| :----: | ------------------- | :------------- | :---------------- | :---------------------------- |
| 2      | `cur = head`        | `Node(4)`      | `[]`              | -                             |
| 3      | `while cur:`        | `Node(4)`      | `[]`              | `Node(4)` is not `None` -\> True |
| 4      | `lst.append(cur.val)` | `Node(4)`      | `[4]`             | -                             |
| 5      | `cur = cur.next`    | `Node(2)`      | `[4]`             | -                             |
| 3      | `while cur:`        | `Node(2)`      | `[4]`             | `Node(2)` is not `None` -\> True |
| 4      | `lst.append(cur.val)` | `Node(2)`      | `[4, 2]`          | -                             |
| 5      | `cur = cur.next`    | `Node(1)`      | `[4, 2]`          | -                             |
| 3      | `while cur:`        | `Node(1)`      | `[4, 2]`          | `Node(1)` is not `None` -\> True |
| 4      | `lst.append(cur.val)` | `Node(1)`      | `[4, 2, 1]`       | -                             |
| 5      | `cur = cur.next`    | `Node(3)`      | `[4, 2, 1]`       | -                             |
| 3      | `while cur:`        | `Node(3)`      | `[4, 2, 1]`       | `Node(3)` is not `None` -\> True |
| 4      | `lst.append(cur.val)` | `Node(3)`      | `[4, 2, 1, 3]`    | -                             |
| 5      | `cur = cur.next`    | `None`         | `[4, 2, 1, 3]`    | -                             |
| 3      | `while cur:`        | `None`         | `[4, 2, 1, 3]`    | `None` is not `None` -\> False   |

**Phase 2: Sorting the Python List** (Line 6)

| Line \# | Code Executed | State of `lst` Before | State of `lst` After |
| :----: | :------------ | :-------------------- | :------------------- |
| 6      | `lst.sort()`  | `[4, 2, 1, 3]`        | `[1, 2, 3, 4]`       |

**Phase 3: Overwriting Node Values** (Lines 7-10)

| Line \# | Code Executed       | State of `cur` | `i` value | `lst[i]` value | State of Linked List (values only) |
| :----: | ------------------- | :------------- | :-------: | :------------: | :--------------------------------- |
| 7      | `cur = head`        | `Node(4)`      | -         | -              | `4 -> 2 -> 1 -> 3`                 |
| 8      | `for i ...`         | `Node(4)`      | `0`       | `1`            | -                                  |
| 9      | `cur.val = lst[i]`  | `Node(1)`      | `0`       | `1`            | `1 -> 2 -> 1 -> 3`                 |
| 10     | `cur = cur.next`    | `Node(2)`      | `0`       | `1`            | `1 -> 2 -> 1 -> 3`                 |
| 8      | `for i ...`         | `Node(2)`      | `1`       | `2`            | -                                  |
| 9      | `cur.val = lst[i]`  | `Node(2)`      | `1`       | `2`            | `1 -> 2 -> 1 -> 3`                 |
| 10     | `cur = cur.next`    | `Node(1)`      | `1`       | `2`            | `1 -> 2 -> 1 -> 3`                 |
| 8      | `for i ...`         | `Node(1)`      | `2`       | `3`            | -                                  |
| 9      | `cur.val = lst[i]`  | `Node(3)`      | `2`       | `3`            | `1 -> 2 -> 3 -> 3`                 |
| 10     | `cur = cur.next`    | `Node(3)`      | `2`       | `3`            | `1 -> 2 -> 3 -> 3`                 |
| 8      | `for i ...`         | `Node(3)`      | `3`       | `4`            | -                                  |
| 9      | `cur.val = lst[i]`  | `Node(4)`      | `3`       | `4`            | `1 -> 2 -> 3 -> 4`                 |
| 10     | `cur = cur.next`    | `None`         | `3`       | `4`            | `1 -> 2 -> 3 -> 4`                 |

The loop now terminates.

**Final Step**

| Line \# | Code Executed  | Action                                    |
| :----: | :------------- | :---------------------------------------- |
| 11     | `return head`  | Returns the head of the now-sorted list. |

**Final Result:** The function returns `head`, which points to the list `1 -> 2 -> 3 -> 4 -> None`.

### Complexity Analysis

  * **Time Complexity:** $O(N \\log N)$, where $N$ is the number of nodes in the linked list.
      * The first traversal takes $O(N)$ time.
      * Sorting the Python list takes $O(N \\log N)$ time.
      * The second traversal takes $O(N)$ time.
      * The dominant step is the sort, making the overall complexity $O(N \\log N)$.
  * **Space Complexity:** $O(N)$.
      * This is the main drawback of this approach. We create an auxiliary Python list (`lst`) that stores one element for every node in the linked list. This requires extra memory proportional to the size of the input. More advanced solutions, like merge sort adapted for linked lists, can achieve the same time complexity with only $O(\\log N)$ or $O(1)$ space.