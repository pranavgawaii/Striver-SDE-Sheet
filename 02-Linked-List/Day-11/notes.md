# Day 11

## Find the Intersection Point of Y LinkedList

### Key Idea
Use two pointers starting at each head; when a pointer reaches the end of its list, redirect it to the head of the other list. They will meet at the intersection node after at most two passes.

### Pattern
Two pointers (Synchronised traversal)

### Complexity
Time: O(N + M)
Space: O(1)

### Revision Note
Both pointers traverse exactly `lenA + lenB` nodes, so the length difference is naturally compensated without explicitly computing it.

## Detect a Loop in LinkedList

### Key Idea
Use Floyd's Cycle Detection — advance a slow pointer by one step and a fast pointer by two steps. If they ever meet, a cycle exists.

### Pattern
Two pointers (Fast and Slow / Tortoise and Hare)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Always check `fast and fast.next` before advancing fast to avoid null pointer errors on acyclic lists.

## Reverse LinkedList in Groups of Size K

### Key Idea
Count total nodes, then repeatedly reverse k-node segments in-place by re-linking pointers, stopping when fewer than k nodes remain.

### Pattern
Iterative in-place reversal with group tracking

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
A dummy node before the head simplifies edge cases when the first group itself gets reversed, avoiding special-case head reassignment.

## Day Takeaway
Floyd's cycle detection and symmetric two-pointer traversals are foundational techniques for linked list problems that avoid auxiliary space by exploiting pointer arithmetic.
