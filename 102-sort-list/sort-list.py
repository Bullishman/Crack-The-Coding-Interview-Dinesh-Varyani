# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst: List = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        
        lst.sort()
        cur = head
        for i in range(len(lst)):
            cur.val = lst[i]
            cur = cur.next
        
        return head