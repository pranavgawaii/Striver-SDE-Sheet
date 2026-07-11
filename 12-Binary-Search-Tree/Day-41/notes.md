# Day 41

## Construct a BST from a preorder traversal

### Key Idea
Unlike constructing a normal BT where you need both preorder and inorder traversals, a BST can be constructed from *just* a preorder traversal using upper bounds. As we iterate through the preorder array, we check if the current element fits within the valid range for the current subtree. If it does, we consume it and recurse for left (with an updated upper bound of `node.val`) and right (with the same upper bound).

### Pattern
Tree Construction (Upper Bound Approach)

### Complexity
Time: O(N)
Space: O(H)

### Revision Note
Using just an upper bound (and a global index) is a brilliant trick that builds the BST in a single pass O(N) time, without needing to sort the array to get the inorder traversal (which would be O(N log N)).

## Check if a tree is a BST or not

### Key Idea
A valid BST must have every node satisfying a strict range `(low, high)`. The root starts with `(-infinity, infinity)`. When traversing left, the upper bound becomes `node.val`. When traversing right, the lower bound becomes `node.val`. If any node violates its range, it's not a BST.

### Pattern
Tree Traversal (Range Validation)

### Complexity
Time: O(N)
Space: O(H)

### Revision Note
Checking `node.left.val < node.val` and `node.right.val > node.val` is *incorrect* because it only checks local parents, not the global ancestors. Range validation is the only robust way.

## LCA in BST

### Key Idea
Finding the Lowest Common Ancestor is incredibly simple in a BST. If both `p` and `q` are strictly smaller than the current node, the LCA must be in the left subtree. If both are strictly larger, the LCA must be in the right subtree. The very first node where `p` and `q` diverge (or where one matches the current node) is the LCA.

### Pattern
BST Traversal

### Complexity
Time: O(H)
Space: O(1) iterative

### Revision Note
Because we only ever go down a single path, this runs in O(H) time and requires O(1) extra space iteratively, a huge improvement over the O(N) normal BT LCA algorithm.

## Inorder Successor and Predecessor in BST

### Key Idea
**Successor (next larger):** Traverse the tree. If `node.val > key`, this node is a *potential* successor, so save it and go left to find a smaller one. If `node.val <= key`, go right.
**Predecessor (next smaller):** Traverse the tree. If `node.val < key`, this node is a *potential* predecessor, so save it and go right to find a larger one. If `node.val >= key`, go left.

### Pattern
BST Traversal

### Complexity
Time: O(H)
Space: O(1)

### Revision Note
Storing the potential answer before diving deeper guarantees that even if we hit `null` later, we have the correct closest ancestor stored.
