class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new_map = {}
        current = head
        while current:
            old_to_new_map[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copied_node = old_to_new_map[current]
            copied_node.next = old_to_new_map.get(current.next)
            copied_node.random = old_to_new_map.get(current.random)
            current = current.next
            
        return old_to_new_map[head]