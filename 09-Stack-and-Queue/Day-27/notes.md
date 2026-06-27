# Day 27

## Largest Rectangle in a Histogram

### Key Idea
Maintain an array of indices using a monotonic stack. The stack stores indices in increasing order of their corresponding heights. When we encounter a bar lower than the top of the stack, we know the right boundary for the bar at the top of the stack. The left boundary is the element just below it in the stack. We calculate the area and pop.

### Pattern
Monotonic Stack

### Complexity
Time: O(N) because every element is pushed and popped at most once.
Space: O(N) for the stack.

### Revision Note
Processing the remaining elements in the stack after the loop is crucial, representing rectangles that extend all the way to the right end of the histogram.

## Sliding Window Maximum

### Key Idea
Use a doubly ended queue (Deque) to store indices of elements in the array. We maintain the deque such that elements are in strictly decreasing order. The maximum for any window is always at the front of the deque. As the window slides, remove indices from the front that are out of bounds, and remove elements from the back that are smaller than the current element (since they are useless).

### Pattern
Deque (Monotonic Queue)

### Complexity
Time: O(N) because each element is pushed and popped at most once.
Space: O(K) for the deque where K is window size.

### Revision Note
Storing indices rather than values in the deque is necessary because we must check if the maximum element's index has fallen out of the sliding window (`dq[0] == i - k`).

## Implement Min Stack

### Key Idea
Use two stacks. The primary stack stores all the elements, and the auxiliary `min_stack` tracks the minimum element at each corresponding state. When pushing, if the value is less than or equal to the top of `min_stack`, push it there too. When popping, if the value equals the top of `min_stack`, pop it there too.

### Pattern
Stack (Auxiliary State)

### Complexity
Time: O(1) for all operations
Space: O(N) for the extra stack

### Revision Note
Using `<= self.min_stack[-1]` instead of `<` is vital to handle duplicate minimum values properly so we don't accidentally lose the min track when popping one of the duplicates.

## Rotten Oranges

### Key Idea
This is a classic Breadth-First Search (BFS) problem on a grid. Find all initially rotten oranges and push them into a queue along with time `0`. Keep track of the total number of fresh oranges. Perform level-order BFS, rotting adjacent fresh oranges and decrementing the count while tracking the maximum time. If fresh oranges remain after the queue is empty, return `-1`.

### Pattern
Multi-source BFS (Grid)

### Complexity
Time: O(R * C) where R and C are rows and columns.
Space: O(R * C) for the queue.

### Revision Note
Using a queue pre-loaded with all initially rotten oranges (Multi-source BFS) is required; doing a single-source BFS from each rotten orange would result in overlapping and inefficient time recalculations.
