# Day 10

## Remove Nth node from the back of the LL

### Key Idea
Maintain a pointer separation of `n` nodes between a fast and slow pointer, then advance both together to find the target's predecessor.

### Pattern
Two pointers (Fast and Slow)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Use a dummy head node to simplify the edge case where the head node itself needs to be removed.

## Add Two Numbers as LinkedList

### Key Idea
Traverse both linked lists simultaneously, computing digit sums and carrying values forward to form a new result list.

### Pattern
Digit arithmetic with carry tracker

### Complexity
Time: O(max(N, M))
Space: O(1) auxiliary space

### Revision Note
Verify that carry values remaining after both lists are exhausted are appended as a final list node.

## Delete Node in a Linked List O(1)

### Key Idea
Copy the value of the node immediately following the target node into the target node, then link past the next node.

### Pattern
In-place node value shift

### Complexity
Time: O(1)
Space: O(1)

### Revision Note
This approach assumes the node to be deleted is not the tail node of the list.

## Day Takeaway
Pointer manipulation and in-place mutations solve linear data structure transformations in optimal constant space constraints.
