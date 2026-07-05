# Day 35

## Pre, Post, Inorder in one traversal

### Key Idea
Use a single stack to simulate the recursive call stack. Each element in the stack is a pair `(node, state)`. 
- State `1` means preorder (add to preorder, increment state, push left child).
- State `2` means inorder (add to inorder, increment state, push right child).
- State `3` means postorder (add to postorder, pop from stack).

### Pattern
Iterative Tree Traversal (State Machine)

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
This state-based approach is incredibly powerful and unifies all three DFS traversals into one logical framework, making it much easier to understand than the separate iterative algorithms.

## Vertical Order Traversal

### Key Idea
Use BFS to traverse the tree, keeping track of the `(row, col)` coordinates. The root is at `(0, 0)`. The left child is at `(row + 1, col - 1)` and the right child is at `(row + 1, col + 1)`. Store the node values in a nested hash map `map[col][row]`. Finally, iterate through the sorted columns and sorted rows, sorting the values if they occupy the exact same `(row, col)` position.

### Pattern
Tree Traversal (BFS with Coordinates)

### Complexity
Time: O(N log N) dominated by sorting the keys and values.
Space: O(N)

### Revision Note
Nodes at the exact same row and column need to be sorted by their values. A nested map (or `defaultdict(lambda: defaultdict(list))` in Python) handles this multi-dimensional grouping perfectly.

## Print Root to Leaf Path in BT

### Key Idea
Use a DFS backtracking approach. Maintain a list representing the current path. When visiting a node, append it to the path. If it's a leaf node (no left and no right child), convert the path to the required format (e.g., joined by `->`) and store it. Backtrack by popping the node off the path before returning.

### Pattern
Tree Traversal (DFS Backtracking)

### Complexity
Time: O(N)
Space: O(H) for the call stack, where H is the height of the tree.

### Revision Note
Remember to always `pop()` the element at the end of the recursive function to properly backtrack and restore the state for other branches.

## Maximum Width of BT

### Key Idea
Use BFS level-order traversal. Assign a unique index to every node (as if it were in a complete binary tree array representation). If a node has index `i`, its left child is `2 * i + 1` and right child is `2 * i + 2`. The width of a level is simply the index of the last node minus the index of the first node plus `1`.

### Pattern
Tree Traversal (BFS with Indexing)

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
Because the indices can grow exponentially, they might overflow in languages like C++ or Java (requiring normalization by subtracting the first index of the level). Python handles arbitrarily large integers automatically, so direct indexing is perfectly safe.
