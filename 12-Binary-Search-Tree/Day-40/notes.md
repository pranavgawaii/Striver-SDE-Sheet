# Day 40

## Populating Next Right Pointers in Each Node

### Key Idea
Instead of using a BFS queue which takes O(N) space, we can utilize the `next` pointers that we are actively building. If a node has children, its left child's next pointer is always its right child. Its right child's next pointer is its own `next` pointer's left child. We traverse level by level, using the previously established `next` pointers to traverse across a single level.

### Pattern
Tree Traversal (Level-linked list approach)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
This O(1) space optimization relies entirely on the assumption that the tree is a *perfect* binary tree. If it's not perfect, finding the "next" node becomes slightly more complex, requiring skipping missing children.

## Search in a Binary Search Tree (BST)

### Key Idea
Exploit the BST property: all values in the left subtree are smaller than the root, and all values in the right subtree are greater. If the target value is smaller than the current node, move left. If it's larger, move right.

### Pattern
Binary Search (Tree form)

### Complexity
Time: O(H) where H is the height of the tree. In the worst case (skewed tree), O(N). In the best/average case (balanced tree), O(log N).
Space: O(1) using iterative approach.

### Revision Note
Always prefer the iterative approach over recursion for simple BST searching to avoid unnecessary call stack overhead.

## Construct BST from given keys (Sorted Array to BST)

### Key Idea
To construct a height-balanced BST from a sorted array, the root must be the middle element of the array. Elements to the left of the middle form the left subtree, and elements to the right form the right subtree. Recursively apply this logic.

### Pattern
Divide and Conquer

### Complexity
Time: O(N)
Space: O(log N) for the recursion stack (since the tree will be perfectly balanced).

### Revision Note
This is the classic way to perfectly balance a BST. Choosing `mid = (left + right) // 2` ensures that the number of nodes in the left and right subtrees differ by at most one, guaranteeing height balance.
