# 136. Insert Delete Getrandom O1

**Difficulty**: Medium

**Topics**: Array, Hash Table, Math, Design, Randomized

**Link**: https://leetcode.com/problems/insert-delete-getrandom-o1

Of course. Let's do a detailed line-by-line demonstration of the `RandomizedSet`.

### The Logic: The Dictionary and List Combo

This is a classic data structure design problem. The goal is to get `insert`, `remove`, and `getRandom` all in average **O(1)** time complexity.

  * A **dictionary (hash map)** provides O(1) average time for insertion, deletion, and lookup. However, you can't get a random element from a dictionary in O(1).
  * A **list (array)** provides O(1) for getting a random element (by picking a random index). However, removing an element from a list is O(n) if it's not the last element, because you have to shift all subsequent elements.

The brilliant solution is to use **both**.

1.  `self.data` (the list) stores the actual values. This makes `getRandom` easy and fast.
2.  `self.data_map` (the dictionary) stores each value as a key and its **index in the list** as the value. This gives us O(1) lookup to find where an element is.

The trickiest part is the `remove` method, which uses a "swap-and-pop" strategy to achieve O(1) time. We'll focus on that in the trace.

### The Example Scenario

Let's trace the following sequence of operations to see how the data structures evolve.

1.  `insert(10)`
2.  `insert(20)`
3.  `insert(30)`
4.  `remove(20)` (This is the most important step to understand)
5.  `insert(10)` (To show failure on duplicate)
6.  `remove(50)` (To show failure on non-existent element)

-----

### **Live Trace Table Map**

This table provides a high-level summary of the state after each operation.

| Operation | `val` | Return Value | `self.data_map` (Value -\> Index) | `self.data` (List) |
| :--- | :--- | :--- | :--- | :--- |
| **`__init__()`** | - | - | `{}` | `[]` |
| **`insert(10)`** | 10 | `True` | `{10: 0}` | `[10]` |
| **`insert(20)`** | 20 | `True` | `{10: 0, 20: 1}` | `[10, 20]` |
| **`insert(30)`** | 30 | `True` | `{10: 0, 20: 1, 30: 2}` | `[10, 20, 30]` |
| **`remove(20)`** | 20 | `True` | `{10: 0, 30: 1}` | `[10, 30]` |
| **`insert(10)`** | 10 | `False` | `{10: 0, 30: 1}` | `[10, 30]` |
| **`remove(50)`** | 50 | `False` | `{10: 0, 30: 1}` | `[10, 30]` |

-----

### **Detailed Line-by-Line Breakdown**

#### Calling `__init__()`

```python
def __init__(self):
    self.data_map = {}
    self.data = []
```

  * **State**: `data_map` is `{}`, `data` is `[]`.

-----

#### Calling `insert(10)`

```python
def insert(self, val: int) -> bool: # val is 10
    if val in self.data_map: # '10' is not in {} -> False
        return False

    self.data_map[val] = len(self.data) # len([]) is 0. data_map[10] = 0
    self.data.append(val)               # data.append(10)
    
    return True
```

  * The `if` condition fails, so we proceed.
  * We add the entry `10: 0` to `data_map`.
  * We append `10` to `data`.
  * **Final State**: `data_map` is `{10: 0}`, `data` is `[10]`. Returns `True`.

-----

#### Calling `insert(20)`

  * Follows the same logic. `len(self.data)` is now `1`.
  * **Final State**: `data_map` is `{10: 0, 20: 1}`, `data` is `[10, 20]`. Returns `True`.

-----

#### Calling `insert(30)`

  * Follows the same logic. `len(self.data)` is now `2`.
  * **Final State**: `data_map` is `{10: 0, 20: 1, 30: 2}`, `data` is `[10, 20, 30]`. Returns `True`.

-----

#### Calling `remove(20)` (The Swap-and-Pop Trick)

This is the key part of the algorithm.
**Initial State**: `data_map = {10: 0, 20: 1, 30: 2}`, `data = [10, 20, 30]`

```python
def remove(self, val: int) -> bool: # val is 20
    if not val in self.data_map: # '20' is in the map -> False
        return False

    # 1. Get the last element and the index of the element to remove
    last_elem_in_list = self.data[-1]              # last_elem_in_list = 30
    index_of_elem_to_remove = self.data_map[val]   # index_of_elem_to_remove = 1

    # 2. Update the map for the last element, giving it the index of the element we're about to overwrite
    self.data_map[last_elem_in_list] = index_of_elem_to_remove # data_map[30] = 1
    # State: data_map = {10: 0, 20: 1, 30: 1} (temporarily inconsistent)

    # 3. Perform the swap in the list. Move the last element to the position of the one being removed.
    self.data[index_of_elem_to_remove] = last_elem_in_list # data[1] = 30
    # State: data = [10, 30, 30]

    # (This is an extra step for visualization, not in the original code, but helps understand the next step)
    # self.data[-1] = val
    # State: data = [10, 30, 20]
    
    # 4. Now pop the last element. This is O(1).
    self.data.pop() # Removes the last element
    # State: data = [10, 30]

    # 5. Remove the target value from the map.
    self.data_map.pop(val) # Removes the key '20'
    # State: data_map = {10: 0, 30: 1}

    return True
```

  * The `if` condition fails, so we proceed.
  * We identify that `20` is at index `1` and the last element is `30`.
  * **The Swap**: We overwrite the `20` at index `1` with `30`. The list becomes `[10, 30, 30]`. We also update the dictionary to reflect that `30` is now at index `1`.
  * **The Pop**: We remove the last element of the list (`30`), which is an O(1) operation. The list becomes `[10, 30]`.
  * **Final Cleanup**: We remove `20` from the dictionary entirely.
  * **Final State**: `data_map` is `{10: 0, 30: 1}`, `data` is `[10, 30]`. Returns `True`.

-----

#### Calling `insert(10)`

```python
def insert(self, val: int) -> bool: # val is 10
    if val in self.data_map: # '10' is in {10: 0, 30: 1} -> True
        return False
```

  * The `if` condition is now true, so it immediately returns `False`. No changes are made.

-----

#### Calling `remove(50)`

```python
def remove(self, val: int) -> bool: # val is 50
    if not val in self.data_map: # '50' is not in the map -> True
        return False
```

  * The `if` condition is now true, so it immediately returns `False`. No changes are made.

-----

#### Calling `getRandom()`

```python
def getRandom(self) -> int:
    return random.choice(self.data)
```

  * This method simply takes the current list, `self.data`.
  * `random.choice` selects a random element from this list by picking a random index from `0` to `len(self.data) - 1`.
  * This is an O(1) operation. If `self.data` were `[10, 30]`, it would return either `10` or `30` with equal probability.