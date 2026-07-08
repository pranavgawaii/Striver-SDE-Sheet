# Day 38

## Maximum path sum

### Key Idea
Similar to finding the diameter of a binary tree, we use a recursive function `max_gain` that computes the maximum path sum of a single branch extending downwards from a node. If a branch sum is negative, we can just ignore it (treat as 0) since it would only decrease the total sum. At each node, we check if the path passing *through* the node (left branch + right branch + node value) is the global maximum.

### Pattern
Tree Traversal (DFS with Global State)

### Complexity
Time: O(N) where N is the number of nodes.
Space: O(H) where H is the height of the tree (for recursion stack).

### Revision Note
The crucial difference between `price_newpath` (which updates the global max and includes both children) and the return value (which can only include one child, as a path cannot split) is the core logic.

## Construct a BT from Preorder and Inorder

### Key Idea
In a preorder traversal, the first element is always the root. We can look up this root value in the inorder traversal to find its position. Elements to the left of this position in the inorder array form the left subtree, and elements to the right form the right subtree. By recursively picking the next element in the preorder array and splitting the inorder bounds, we construct the tree.

### Pattern
Tree Construction (Divide and Conquer)

### Complexity
Time: O(N) using a hash map to look up indices in O(1) time.
Space: O(N) for the hash map and the recursion stack.

### Revision Note
Building the `inorder_map` upfront avoids O(N) lookups at every step, dropping the overall time complexity from O(N^2) to O(N). Always build the left child *before* the right child, because preorder visits the left subtree first.

## Construct a BT from Postorder and Inorder

### Key Idea
Very similar to the Preorder/Inorder problem. In a postorder traversal, the *last* element is always the root. We look up this root in the inorder array to divide the tree into left and right subtrees. Since postorder visits Left -> Right -> Root, traversing the postorder array backwards gives us Root -> Right -> Left.

### Pattern
Tree Construction (Divide and Conquer)

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
Unlike the preorder traversal, you must construct the *right* child *before* the left child when reading the postorder array backwards.
