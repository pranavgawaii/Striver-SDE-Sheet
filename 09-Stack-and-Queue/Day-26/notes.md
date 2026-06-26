# Day 26

## Next Smaller Element

### Key Idea
Iterate through the array. Maintain a stack of elements seen so far. For the current element, pop elements from the stack that are greater than or equal to it. The top of the stack is now the previous smaller element (or `-1` if empty). Push the current element to the stack.

### Pattern
Monotonic Stack

### Complexity
Time: O(N) because each element is pushed and popped at most once.
Space: O(N)

### Revision Note
A monotonic increasing stack is the standard way to find the next/previous smaller element efficiently.

## LRU Cache

### Key Idea
Use a hash map mapping keys to Doubly Linked List nodes for O(1) access. The Doubly Linked List maintains the recency of usage, with the most recently used at the head and least recently used at the tail. Every `get` or `put` operation moves the accessed node to the head. When capacity is exceeded, pop the tail node and remove its key from the map.

### Pattern
Data Structure Design (Hash Map + Doubly Linked List)

### Complexity
Time: O(1) for both `get` and `put`
Space: O(Capacity)

### Revision Note
Using dummy `head` and `tail` nodes in the doubly linked list prevents having to write edge case checks for `node.prev is None` or `node.next is None` during node removals and insertions.

## LFU Cache

### Key Idea
Use two hash maps: one mapping keys to nodes, and another mapping frequencies to Doubly Linked Lists (where each list holds nodes of that frequency). Maintain a `min_freq` variable. On every access, remove the node from its current frequency list, increment its frequency, and add it to the next frequency list. If the old frequency list becomes empty and it was the `min_freq`, increment `min_freq`. Evict the tail of the `min_freq` list when capacity is exceeded.

### Pattern
Data Structure Design (Two Hash Maps + Doubly Linked List)

### Complexity
Time: O(1) for both `get` and `put`
Space: O(Capacity)

### Revision Note
LFU is essentially an extension of LRU, but instead of one global timeline of recency, we maintain separate timelines of recency for *each* access frequency.
