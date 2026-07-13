# Day 43

## Two sum in BST

### Key Idea
Instead of doing a full inorder traversal to get a sorted array and then using two pointers (which takes O(N) space), we can use two custom `BSTIterator` objects. One iterator yields elements in increasing order (normal inorder), and the other yields elements in decreasing order (reverse inorder). We then use the classic two-pointer approach, fetching the `next()` elements lazily.

### Pattern
Two Pointers + BST Iterator

### Complexity
Time: O(N)
Space: O(H) for the iterator stacks.

### Revision Note
Lazy evaluation via iterators is incredibly powerful. It reduces space from O(N) to O(H) and time can be substantially less than O(N) if the target sum is found early.

## BST Iterator

### Key Idea
Maintain a stack to simulate the recursion stack of an inorder traversal. When initialized, push all left children of the root into the stack. A call to `next()` pops the top element (the smallest), and then pushes all left children of that element's right child.

### Pattern
Tree Traversal (Iterative Inorder)

### Complexity
Time: O(1) amortized for `next()`, O(1) for `hasNext()`.
Space: O(H)

### Revision Note
Even though a single `next()` call might trigger a `while` loop that takes O(H) time, across a full traversal of N nodes, the `while` loop body runs exactly N times. Thus, the amortized time per `next()` call is O(1).

## Size of the largest BST in a Binary Tree

### Key Idea
Use a bottom-up postorder traversal. A tree is a valid BST if its left subtree is a BST, its right subtree is a BST, and its root's value is strictly greater than the maximum value in the left subtree and strictly less than the minimum value in the right subtree. Each recursive call returns `(min_val, max_val, max_size)`. If the current node violates the BST property, we return `(-inf, inf, max(left_size, right_size))` to ensure it fails all future BST checks above it while propagating the max size found so far.

### Pattern
Tree Traversal (Postorder Bottom-Up DP)

### Complexity
Time: O(N) since each node is visited exactly once.
Space: O(H)

### Revision Note
The clever part is returning `(-infinity, infinity)` for invalid subtrees. Any valid parent check `left.max < node.val < right.min` will instantly fail because `node.val` cannot be greater than `infinity` or less than `-infinity`.

## Serialize and De-serialize BT

### Key Idea
Use standard Level Order Traversal (BFS) to serialize the tree into a string. Every null node is appended as a special marker like `#`. When deserializing, split the string by commas and use a Queue to reconstruct the tree level by level, matching the exact order the nodes were serialized.

### Pattern
Tree Traversal (BFS / Level Order)

### Complexity
Time: O(N) for both serialize and deserialize.
Space: O(N) for the queues and string arrays.

### Revision Note
BFS is generally preferred over DFS for serialization because it doesn't run into maximum recursion depth issues on very skewed trees (e.g., deep linked lists) and the queue iteratively handles large node counts smoothly.
