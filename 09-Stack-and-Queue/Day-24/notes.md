# Day 24

## Implement Stack using Arrays

### Key Idea
Maintain a `top` pointer initialized to `-1`. On push, increment `top` and assign the value to the array. On pop, return the value at `top` and decrement `top`.

### Pattern
Data Structure Design (Stack)

### Complexity
Time: O(1) for all operations
Space: O(N) where N is the capacity

### Revision Note
Always check for overflow (`top == capacity - 1`) and underflow (`top == -1`) before pushing and popping respectively.

## Implement Queue using Arrays

### Key Idea
Maintain `front` and `rear` pointers along with `current_size`. Use modulo arithmetic (`% capacity`) to make the queue circular. Push at `rear`, pop from `front`.

### Pattern
Data Structure Design (Circular Queue)

### Complexity
Time: O(1) for all operations
Space: O(N) where N is the capacity

### Revision Note
A circular queue optimally reuses space that was freed by popped elements, which a simple linear queue with two pointers fails to do.

## Implement Stack using Queue

### Key Idea
Use a single queue. When pushing an element, append it to the back. Then, to make it behave like a stack, dequeue all elements before it and enqueue them again at the back. This makes the newly pushed element the front of the queue.

### Pattern
Data Structure Design (Adapter)

### Complexity
Time: O(N) for push, O(1) for pop and top
Space: O(N)

### Revision Note
Using a single queue instead of two queues requires exactly `size - 1` pop-and-push operations during every insertion.

## Implement Queue using Stack

### Key Idea
Use two stacks: `input` and `output`. Push elements into `input`. For pop or peek operations, if `output` is empty, transfer all elements from `input` to `output`. This reverses their order, bringing the oldest element to the top of `output`.

### Pattern
Data Structure Design (Adapter)

### Complexity
Time: O(1) amortized for pop/peek, O(1) for push
Space: O(N)

### Revision Note
The amortized O(1) time complexity for pop is the beauty of this approach. Elements are only moved from `input` to `output` when `output` is empty, avoiding O(N) work on every pop.

## Day Takeaway
Understanding how to build foundational data structures from each other reinforces the core concepts of LIFO and FIFO and highlights the trade-offs between different time complexities for specific operations.
