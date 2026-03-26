# 182. Remove Duplicates from Sorted List II

**Difficulty**: Medium

**Topics**: Linked List, Two Pointers

**Link**: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

This problem can be solved gracefully using an elegant **Recursive Approach**. 

### The Core Idea

The goal is to delete *all* nodes that share duplicate values in a sorted linked list, leaving only mathematically distinct elements.

Because the list is sorted, any duplicates will be positioned adjacently. By evaluating the list recursively, we can look at the current `head` and its immediate neighbor `head.next`:
1. **If they match:** We use a loop to safely skip completely past the entire contiguous block of duplicates. We then return the recursive result of whatever comes *after* that block, inherently deleting the duplicates.
2. **If they differ:** We know the current `head` is safe to keep. We attach the recursive result of the rest of the list continuously to `head.next` and return `head`.

Let's break down the code line by line with an example.

**Example List:** `[1, 2, 3, 3, 4, 4, 5]`
**Expected Result:** `[1, 2, 5]` (Nodes with 3 and 4 are entirely removed)

-----

### **Base Case: End of List**

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
```

  * **What it does:** This is the recursive base case. If the list is empty (`not head`) or we've reached the very last node (`not head.next`), there is no possibility of any duplicates existing from this point onward. We safely return the node as-is.

-----

### **The Duplication Handler**

```python
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
                
            return self.deleteDuplicates(head.next)
```

  * **What it does:** 
      * We check if the current node shares the same value as its downstream neighbor.
      * If it does, we enter a `while` loop that advances the `head` pointer until it rests on the **last instance** of that duplicated value.
      * We then call `self.deleteDuplicates(head.next)`. By returning this recursive call directly, we successfully bypass and orphan all nodes involving the duplicated value, effectively deleting them from the list block.

-----

### **The Distinct Handler**

```python
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
```

  * **What it does:** 
      * If `head.val != head.next.val`, the current node stands alone securely.
      * We don't skip it; instead, we set its `.next` pointer to be whatever safely comes back from the recursive processing of the remainder of the list.
      * Finally, we return `head` upward through the call stack so the previous steps can latch onto it.

-----

### **Live Trace Table Map**

Let's execute the logic systematically with the example `1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5`.

| Call Stack Depth | Current `head` Node | `head.next` Node | Condition | State / Action | Return Value Passing Upward |
|:---:|:---:|:---:|:---|:---|:---|
| **1** | Node `1` | Node `2` | `1 != 2` (Distinct) | Recurse on `2`. Wait for result to attach to `1.next`. | `1 -> [result of Depth 2]` |
| **2** | Node `2` | Node `3` | `2 != 3` (Distinct) | Recurse on `3`. Wait for result to attach to `2.next`. | `2 -> [result of Depth 3]` |
| **3** | Node `3` | Node `3` | `3 == 3` (Duplicate!) | Loop advances `head` past both `3`s to point to `4`. Return `deleteDuplicates(Node 4)`. | `[result of Depth 4]` |
| **4** | Node `4` | Node `4` | `4 == 4` (Duplicate!) | Loop advances `head` past both `4`s to point to `5`. Return `deleteDuplicates(Node 5)`. | `[result of Depth 5]` |
| **5** | Node `5` | `None` | Base case triggered! | No duplicates possible. Returns Node `5` as-is. | Node `5` |

**Unwinding the Call Stack:**

1. **Depth 5** returns Node `5` immediately to Depth 4.
2. **Depth 4** directly returns Node `5` upward to Depth 3, effectively bypassing the `4`s!
3. **Depth 3** directly returns Node `5` upward to Depth 2, effectively bypassing the `3`s!
4. **Depth 2** receives Node `5` and attaches it: `2.next = Node 5`. It returns Node `2`.
5. **Depth 1** receives Node `2` (which is now linked to `5`!) and attaches it: `1.next = Node 2`. It returns Node `1`.

**Final List Returned to Caller:**
`1 -> 2 -> 5`
