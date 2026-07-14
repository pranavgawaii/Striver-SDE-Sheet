# Day 44

## Binary Tree to Doubly Linked List

### Key Idea
Perform an inorder traversal. Maintain a `prev` pointer (initially null). When visiting a node, if `prev` is null, this node is the `head` of the DLL. If `prev` is not null, link `prev.right` to `node` and `node.left` to `prev`. Finally, update `prev = node` and recurse right.

### Pattern
Tree Traversal (Inorder with global state)

### Complexity
Time: O(N)
Space: O(H)

### Revision Note
This in-place conversion elegantly uses the left and right pointers of the tree as the `prev` and `next` pointers of the DLL without requiring extra nodes.

## Find Median in a Stream

### Key Idea
Use two heaps: a max-heap (`small`) to store the smaller half of the numbers, and a min-heap (`large`) to store the larger half. The max-heap is allowed to have at most one more element than the min-heap. When adding a number, always push to the max-heap first, balance if the largest in `small` is greater than the smallest in `large`, and then balance the sizes.

### Pattern
Two Heaps (Priority Queue)

### Complexity
Time: O(log N) per `addNum`, O(1) for `findMedian`
Space: O(N) to store the stream numbers.

### Revision Note
In Python, the `heapq` module only provides a min-heap. To create a max-heap, push the negative of the number. Remember to invert it back when popping or accessing `heap[0]`.

## Kth largest element in a stream of running integers

### Key Idea
Maintain a min-heap of size exactly `K`. When a new element arrives, push it into the heap. If the heap size exceeds `K`, pop the smallest element. The Kth largest element is always the smallest element remaining in the heap (the root of the min-heap).

### Pattern
Priority Queue (Min-Heap)

### Complexity
Time: O(log K) per `add` operation.
Space: O(K) for the heap.

### Revision Note
A min-heap of size K is the standard optimal approach for tracking the "K-th largest" because it automatically ejects anything smaller than the top K elements.
