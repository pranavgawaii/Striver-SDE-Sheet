# Day 9

## Reverse Linked List

### Key Idea
Iteratively change the next pointers of the nodes to point to their previous node.

### Pattern
Iterative pointer swapping

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Maintain prev, curr, and temporary next_node references to advance through the list in one pass.

## Find Middle of Linked List

### Key Idea
Use a slow pointer that moves one step at a time and a fast pointer that moves two steps at a time.

### Pattern
Fast and slow pointers (Tortoise and Hare)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Ensure conditions handle both odd (fast.next is null) and even (fast is null) length lists correctly.

## Merge Two Sorted Lists

### Key Idea
Compare node values from both lists sequentially and attach the smaller node to a dummy-anchored result list.

### Pattern
Dummy node, two pointers

### Complexity
Time: O(N + M)
Space: O(1)

### Revision Note
Initialize a dummy node as head, append remaining elements of non-empty list at the end.

## Day Takeaway
Linked list modifications leverage dummy nodes to simplify edge cases and multiple pointers to track steps dynamically.
