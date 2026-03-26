from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, there are no duplicates
        if not head or not head.next:
            return head
            
        if head.val == head.next.val:
            # We found a sequence of duplicates.
            # Fast-forward 'head' until it reaches the last node of this duplicate sequence.
            while head.next and head.val == head.next.val:
                head = head.next
                
            # 'head' is now the last duplicate. 
            # We completely SKIP this entire group by recursing on head.next
            return self.deleteDuplicates(head.next)
        else:
            # The current head is unique relative to its immediate neighbor.
            # We safely keep this 'head' and recursively process the remainder of the list.
            head.next = self.deleteDuplicates(head.next)
            return head
