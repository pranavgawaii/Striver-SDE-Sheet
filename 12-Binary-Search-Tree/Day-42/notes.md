# Day 42

## Floor in a BST

### Key Idea
The floor of `X` is the greatest value in the BST that is smaller than or equal to `X`. Traverse the tree: if `node.val == X`, return it. If `node.val > X`, the answer must be in the left subtree. If `node.val < X`, this node is a potential floor. Save it and search the right subtree for a potentially larger, but still valid, floor.

### Pattern
BST Traversal (Binary Search logic)

### Complexity
Time: O(H)
Space: O(1)

### Revision Note
Always save the potential answer *before* moving to the right subtree. The iterative approach is extremely clean and avoids stack memory overhead.

## Ceil in a BST

### Key Idea
The ceil of `X` is the smallest value in the BST that is greater than or equal to `X`. Traverse the tree: if `node.val == X`, return it. If `node.val < X`, the answer must be in the right subtree. If `node.val > X`, this node is a potential ceil. Save it and search the left subtree for a potentially smaller, but still valid, ceil.

### Pattern
BST Traversal (Binary Search logic)

### Complexity
Time: O(H)
Space: O(1)

### Revision Note
This is perfectly symmetrical to the Floor problem. Save the potential answer before moving to the left subtree.

## Find K-th smallest element in BST

### Key Idea
An inorder traversal of a BST visits nodes in strictly increasing order. To find the K-th smallest element, simply perform an inorder traversal and keep a global counter. Stop as soon as the counter reaches `K`.

### Pattern
Tree Traversal (Inorder + Counter)

### Complexity
Time: O(H + K) where H is the height of the tree.
Space: O(H) for the recursion stack.

### Revision Note
Short-circuiting the recursion (`if count >= k: return`) prevents the algorithm from traversing the entire tree when `K` is small.

## Kth Smallest and Largest element in BST

### Key Idea
To find the K-th smallest element, we use the standard left-root-right inorder traversal. To find the K-th largest element efficiently, we can use a reverse inorder traversal (right-root-left), which visits nodes in strictly decreasing order. Keep a counter for both.

### Pattern
Tree Traversal (Inorder and Reverse Inorder)

### Complexity
Time: O(H + K) for each traversal.
Space: O(H) for the recursion stack.

### Revision Note
Using the reverse inorder traversal (Right -> Root -> Left) is vastly more efficient than trying to find the total number of nodes `N` and then looking for the `(N - K + 1)`-th smallest element.
