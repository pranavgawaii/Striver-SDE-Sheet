# Day 37

## LCA in BT

### Key Idea
If the current node is `null`, `p`, or `q`, return it. Otherwise, recursively search the left and right subtrees. If both recursive calls return non-null, the current node is the Lowest Common Ancestor. If only one call returns non-null, propagate that result up.

### Pattern
Tree Traversal (DFS/Recursion)

### Complexity
Time: O(N)
Space: O(H)

### Revision Note
This elegant recursive logic handles both cases: when `p` and `q` are on different branches, the node where the branches diverge receives non-null from both sides and returns itself. When `p` is an ancestor of `q`, `p` is returned first and propagated up without ever searching for `q`.

## Check if two trees are identical or not

### Key Idea
Recursively compare the root values and then structurally compare their left and right subtrees. If both are `null`, they are identical. If one is `null` and the other is not, or if their values differ, they are not identical.

### Pattern
Tree Traversal (Parallel DFS)

### Complexity
Time: O(min(N, M)) where N and M are the number of nodes in the two trees.
Space: O(min(H1, H2))

### Revision Note
The base cases `if not p and not q` and `if not p or not q` gracefully handle all structure mismatch checks.

## Zig Zag or Spiral Traversal

### Key Idea
Perform a standard Level Order Traversal using a BFS Queue. Maintain a boolean flag `left_to_right`. If the flag is true, populate the level array left-to-right. If the flag is false, populate the level array right-to-left. Flip the flag after every level.

### Pattern
Tree Traversal (BFS with Flag)

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
Instead of physically reversing the array at the end of each level, you can pre-allocate an array of size `len(queue)` and fill it by assigning `current_level[index] = node.val` where `index` is determined by the `left_to_right` flag.

## Boundary Traversal

### Key Idea
The boundary of a binary tree is formed by the Left Boundary (excluding leaves), the Leaves (from left to right), and the Right Boundary (excluding leaves, in reverse order). Write three separate functions for each of these parts and assemble the results.

### Pattern
Tree Traversal (Segmented Traversal)

### Complexity
Time: O(N)
Space: O(H) for recursion stack of leaves.

### Revision Note
Pay special attention to the root. If the root is a leaf, make sure you don't add it multiple times. Also, remember that the right boundary must be traversed top-down but added bottom-up (which is why a temporary array is reversed before adding to the result).
