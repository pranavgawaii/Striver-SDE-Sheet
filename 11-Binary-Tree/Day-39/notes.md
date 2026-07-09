# Day 39

## Symmetric Binary Tree / Check for Symmetrical BTs

### Key Idea
A tree is symmetric if its left subtree is a mirror reflection of its right subtree. We can recursively check if two nodes are mirrors: they must both be null, or they must both have the same value, and their subtrees must be mirrors in opposite directions (`left.left` with `right.right`, and `left.right` with `right.left`).

### Pattern
Tree Traversal (Parallel DFS)

### Complexity
Time: O(N)
Space: O(H)

### Revision Note
This is conceptually similar to "Check if two trees are identical", but with inverted left/right child comparisons.

## Flatten Binary Tree to Linked List

### Key Idea
The goal is to flatten the tree in-place to follow preorder traversal. We can use the Morris Traversal idea. For any node, if it has a left child, find the rightmost node of that left child. Make that rightmost node point to the current node's right child. Then, move the current node's left child to its right child, and set the left child to null.

### Pattern
Tree Traversal (Morris-like constant space approach)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
You can also solve this recursively using a global `prev` pointer and doing a reverse postorder traversal (Right -> Left -> Root), but the Morris approach is O(1) space.

## Children Sum Property in Binary Tree

### Key Idea
The property states that a node's value must equal the sum of its children's values. If the children's sum is smaller than the root, we propagate the root's value down to the children so that we never run out of "value" to distribute. After recursively fixing the left and right subtrees, we update the root's value to exactly equal the sum of the newly adjusted children.

### Pattern
Tree Traversal (DFS with Top-down Propagation and Bottom-up Aggregation)

### Complexity
Time: O(N)
Space: O(H)

### Revision Note
The trick is that we are allowed to *increase* node values arbitrarily, but not decrease them. Pushing large values downwards guarantees we can safely balance the tree on the way back up without violating the property.
