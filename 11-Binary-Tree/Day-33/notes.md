# Day 33

## Inorder Traversal

### Key Idea
Visit nodes in the order: Left Subtree -> Root -> Right Subtree. This is naturally implemented using recursion.

### Pattern
Tree Traversal (DFS)

### Complexity
Time: O(N)
Space: O(N) for the recursive call stack (in the worst case of a skewed tree).

### Revision Note
In a Binary Search Tree (BST), Inorder Traversal yields the values in strictly increasing sorted order.

## Preorder Traversal

### Key Idea
Visit nodes in the order: Root -> Left Subtree -> Right Subtree. 

### Pattern
Tree Traversal (DFS)

### Complexity
Time: O(N)
Space: O(N) for the recursive call stack.

### Revision Note
Preorder traversal is often used to create a copy of the tree or to serialize the tree into an array/string.

## Postorder Traversal

### Key Idea
Visit nodes in the order: Left Subtree -> Right Subtree -> Root.

### Pattern
Tree Traversal (DFS)

### Complexity
Time: O(N)
Space: O(N) for the recursive call stack.

### Revision Note
Postorder traversal is heavily used when you need to process leaves before the root, such as when deleting a tree or evaluating an abstract syntax tree.

## Morris Inorder Traversal

### Key Idea
Traverse the tree without using any extra space for a stack or recursion. This is achieved by creating temporary threads (links) from the rightmost node of a left subtree back to the root of that subtree. Once the left subtree is fully visited, the thread is removed to restore the original tree structure.

### Pattern
Threaded Binary Tree Traversal

### Complexity
Time: O(N). Although there are nested loops, every edge in the tree is traversed at most 3 times.
Space: O(1) extra space!

### Revision Note
The core logic revolves around finding the in-order predecessor (`pre.right`). If it points to `null`, make it point to `current`. If it already points to `current`, it means the left subtree is done, so break the link and process `current`.
