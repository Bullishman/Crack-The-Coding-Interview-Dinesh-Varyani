# 13. Lru Cache

**Difficulty**: Medium

**Topics**: Hash Table, Linked List, Design, Doubly-Linked List

**Link**: https://leetcode.com/problems/lru-cache

Of course. This code implements a **Least Recently Used (LRU) Cache** using the standard, optimal approach. It's a fantastic example of how two data structures can be combined to overcome each other's weaknesses.

### The Core Idea

This implementation uses two data structures working together to achieve fast O(1) time complexity for both `get` and `put` operations:

1.  **A Dictionary (Hash Map) `self.cache`**: This provides O(1) lookup to find any node instantly using its key. It stores `key -> Node` mappings.
2.  **A Doubly-Linked List**: This is used to track the usage order of the nodes. It's ordered from Least Recently Used (LRU) to Most Recently Used (MRU). Because it's a doubly-linked list, we can add or remove any node in O(1) time *if we have a direct reference to it* (which the hash map gives us).

To simplify the logic, the list uses two dummy nodes, `self.head` and `self.tail`, which act as fixed sentinels. The actual LRU item is always `self.head.next`, and the MRU item is always `self.tail.prev`.

Let's break down the code with a sequence of operations.

**Example Scenario:** We will create a cache with a `capacity` of 2.
`cache = LRUCache(2)`

-----

### **The `Node` and `__init__` Method**

```python
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
        self.head = Node()  # Least recently used side
        self.tail = Node()  # Most recently used side
        self.head.next = self.tail
        self.tail.prev = self.head
```

  * **`Node` class**: Defines the structure for our doubly-linked list nodes. Each node stores its own key and value, plus pointers to the previous and next nodes.
  * **`__init__`**:
      * `self.cache = {}`: Initializes the hash map.
      * `self.head`, `self.tail`: Creates the two dummy nodes.
      * `self.head.next = self.tail` and `self.tail.prev = self.head`: Links the dummy nodes together to form the initial empty list structure: `head <-> tail`.

-----

### **Helper Methods**

These private methods handle the low-level pointer manipulation of the linked list.

  * `_remove_node(self, node)`: Takes a node and "unplugs" it from the list by connecting its previous and next neighbors to each other.
  * `_add_to_end(self, node)`: Takes a node and adds it right before the dummy `tail`. This makes it the new Most Recently Used (MRU) node.
  * `_move_to_end(self, node)`: A convenience method that simply removes a node and then adds it back to the end. This is the "update usage" operation.

-----

### **`get(self, key: int)` Method**

```python
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Update usage by moving node to end
            self._move_to_end(node)
            return node.value
        return -1
```

  * **`if key in self.cache:`**: Checks the hash map for the key (O(1) operation).
  * **`node = self.cache[key]`**: Retrieves the node object directly (O(1)).
  * **`self._move_to_end(node)`**: Marks the node as most recently used by moving it to the end of the linked list (O(1) operation).
  * **`return node.value`**: Returns the node's value. If the key isn't in the cache, it returns -1.

-----

### **`put(self, key: int, value: int)` Method**

```python
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
```

  * **`if key in self.cache:`**: Handles updating an existing item. It finds the node (O(1)), updates its value, and moves it to the end of the list (O(1)).
  * **`else:`**: Handles adding a new item.
      * **`if len(self.cache) >= self.capacity:`**: Checks if the cache is full.
      * **Eviction**: If full, it identifies the LRU node, which is always `self.head.next`. It removes this node from the linked list and deletes it from the `cache` dictionary. All these are O(1) operations.
      * **Insertion**: It creates a `new_node`, adds it to the end of the linked list, and adds it to the `cache` dictionary. All O(1) operations.

-----

### **Live Trace Table Map**

**Scenario:** A cache with `capacity = 2`.

| Operation | Action and Explanation | `self.cache` State | Doubly-Linked List State | Return |
| :--- | :--- | :--- | :--- | :--- |
| `LRUCache(2)` | Initialize with capacity 2. Dummy nodes are linked. | `{}` | `head <-> tail` | `None` |
| `put(1, 1)` | Key 1 is new. Cache not full. Create `Node(1,1)` and add to end. Add to cache. | `{1: Node(1)}` | `head <-> (1,1) <-> tail` | `None` |
| `put(2, 2)` | Key 2 is new. Cache not full. Create `Node(2,2)` and add to end. Add to cache. | `{1:Node(1), 2:Node(2)}` | `head <-> (1,1) <-> (2,2) <-> tail` | `None` |
| `get(1)` | Key 1 exists. **Move node (1,1) to end**. The list becomes `head <-> (2,2) <-> (1,1) <-> tail`. | `{1:Node(1), 2:Node(2)}` | `head <-> (2,2) <-> (1,1) <-> tail` | `1` |
| `put(3, 3)` | Key 3 is new. Cache is full. **Evict LRU (`head.next`)**, which is `Node(2)`. Remove 2 from list and cache. Then add `Node(3,3)` to end. | `{1:Node(1), 3:Node(3)}` | `head <-> (1,1) <-> (3,3) <-> tail` | `None` |
| `get(2)` | Key 2 is not in the cache. | `{1:Node(1), 3:Node(3)}` | `head <-> (1,1) <-> (3,3) <-> tail` | `-1` |
| `put(4, 4)` | Key 4 is new. Cache is full. **Evict LRU (`head.next`)**, which is `Node(1)`. Remove 1 from list and cache. Then add `Node(4,4)` to end. | `{3:Node(3), 4:Node(4)}` | `head <-> (3,3) <-> (4,4) <-> tail` | `None` |