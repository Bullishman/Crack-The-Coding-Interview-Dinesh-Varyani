class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # {key: node}
        
        # Initialize dummy head and tail nodes
        self.head = Node()  # Least recently used
        self.tail = Node()  # Most recently used
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        # Remove node from doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_end(self, node):
        # Add node to end (most recently used position)
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    
    def _move_to_end(self, node):
        # Move existing node to end (most recently used position)
        self._remove_node(node)
        self._add_to_end(node)
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Update usage by moving node to end
            self._move_to_end(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        # If key exists, update value and move to end
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_end(node)
        else:
            # If at capacity, remove least recently used item (head.next)
            if len(self.cache) >= self.capacity:
                lru_node = self.head.next
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            
            # Add new node to end and to cache
            new_node = Node(key, value)
            self._add_to_end(new_node)
            self.cache[key] = new_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)