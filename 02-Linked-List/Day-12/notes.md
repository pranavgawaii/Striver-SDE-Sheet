# Day 12

## Check if LL is Palindrome or Not

### Key Idea
Find the middle using slow-fast pointers, reverse the second half in-place, then compare both halves node by node.

### Pattern
Two pointers (Fast and Slow) + In-place reversal

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Use `fast.next and fast.next.next` to land slow at the end of the first half, making the split clean for both odd and even length lists.

## Find the Starting Point in LL

### Key Idea
Detect the cycle using Floyd's algorithm, then reset one pointer to head and advance both one step at a time — they meet at the cycle's entry point.

### Pattern
Two pointers (Floyd's Cycle Detection + Entry Point)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
The mathematical proof relies on the fact that the distance from head to cycle start equals the distance from the meeting point to cycle start (modulo cycle length).

## Flattening of LL

### Key Idea
Recursively flatten from the tail end, then merge each sub-list (connected via `bottom` pointers) with the already-flattened portion using a merge-sort style merge.

### Pattern
Recursion + Merge two sorted lists

### Complexity
Time: O(N × M) where N is the number of horizontal nodes and M is the average depth
Space: O(N) recursion stack

### Revision Note
Always set `result.next = None` after merging to disconnect the horizontal links and keep the flattened list purely vertical.

## Day Takeaway
Floyd's algorithm extends beyond cycle detection to pinpointing cycle entry points, while recursive merge patterns from merge sort translate directly to multi-dimensional linked list problems.
