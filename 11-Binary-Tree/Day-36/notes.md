# Day 36

## Level Order Traversal

### Key Idea
Use a Queue (BFS approach). Keep track of the number of nodes at the current level using `len(queue)`. Iterate exactly that many times, popping from the front and pushing children to the back. This naturally segregates the tree level by level.

### Pattern
Tree Traversal (BFS)

### Complexity
Time: O(N) where N is the number of nodes in the tree.
Space: O(W) where W is the maximum width of the tree, which is O(N) in the worst case (perfect binary tree).

### Revision Note
Using `len(queue)` inside the `while` loop but before the `for` loop is the crucial trick to process the tree one distinct level at a time.

## Maximum Depth in BT

### Key Idea
The maximum depth of a binary tree is `1 + max(depth of left subtree, depth of right subtree)`. This recursive relationship holds true for every node down to the base case (an empty tree has depth 0).

### Pattern
Tree Traversal (DFS/Recursion)

### Complexity
Time: O(N)
Space: O(H) where H is the height of the tree (for the recursion stack).

### Revision Note
This is the most fundamental tree recursion algorithm and forms the basis for many other more complex tree algorithms.

## Diameter of Binary Tree

### Key Idea
The diameter (longest path between any two nodes) might or might not pass through the root. However, the path passing through any specific node has length `left_depth + right_depth`. We can calculate the maximum depth of each subtree recursively, and simultaneously update a global/class variable `diameter = max(diameter, left_depth + right_depth)` during the post-order step.

### Pattern
Tree Traversal (DFS with Global State)

### Complexity
Time: O(N)
Space: O(H)

### Revision Note
Calculating the diameter directly in the depth recursion avoids doing redundant work (O(N) instead of O(N^2)).

## Check for Balanced Binary Tree

### Key Idea
A tree is height-balanced if the absolute difference in heights of the left and right subtrees of *every* node is at most 1. We can modify the standard "find height" function to return `-1` if it detects that any subtree is unbalanced. When a recursive call returns `-1`, we immediately propagate that `-1` up the call stack to short-circuit the execution.

### Pattern
Tree Traversal (DFS with Sentinels)

### Complexity
Time: O(N)
Space: O(H)

### Revision Note
Propagating `-1` upwards as soon as an imbalance is found makes this an optimal O(N) solution. Otherwise, calling a separate `height()` function at every node would result in O(N^2) time.
