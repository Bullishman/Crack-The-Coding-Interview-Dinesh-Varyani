# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node: ListNode) -> int:
            return node.val + (10 * toint(node.next)) if node else 0
        n = toint(l1) + toint(l2)
        root = head = ListNode(n % 10)
        while n > 9:
            n //= 10
            head.next = head = ListNode(n % 10)
        return root