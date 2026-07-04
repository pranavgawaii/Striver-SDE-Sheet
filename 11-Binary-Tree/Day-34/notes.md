# Day 34

## Morris Preorder Traversal

### Key Idea
Similar to Morris Inorder, but you visit the node *before* going down to the left child (when you first create the thread). Traverse the tree without extra space by creating temporary links from the rightmost node of a left subtree back to the root.

### Pattern
Threaded Binary Tree Traversal

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
In Morris Preorder, you append the value when `pre.right` is `None` (first visit), whereas in Morris Inorder you append the value when `pre.right == current` (second visit after returning from the left subtree).

## Right/Left View of BT

### Key Idea
Use DFS with a depth parameter. For Right View, traverse the right subtree before the left subtree. For Left View, traverse the left subtree before the right subtree. If `depth == len(res)`, it's the first node you've seen at that depth, so append it to the result.

### Pattern
Tree Traversal (DFS with Depth Tracking)

### Complexity
Time: O(N)
Space: O(H) where H is the height of the tree (for the recursion stack).

### Revision Note
Level-order traversal (BFS) also works perfectly (take the last/first element of each level), but the DFS approach is often cleaner to write recursively.

## Bottom View of BT

### Key Idea
Use BFS with a horizontal distance (`hd`) tracking parameter. The root has `hd = 0`, left child has `hd - 1`, right child has `hd + 1`. Use a map to store `hd -> node.val`. Overwrite the map value for `hd` every time you see a new node at that `hd`. The final values in the map for each `hd` represent the bottom view.

### Pattern
Tree Traversal (BFS with Horizontal Distance)

### Complexity
Time: O(N log N) to sort the keys at the end, or O(N) if you track the min and max `hd` during traversal.
Space: O(N) for the queue and map.

### Revision Note
BFS is mandatory here (not DFS). A DFS might reach a node lower in the tree but earlier in the traversal order, overwriting the map incorrectly. BFS ensures nodes are processed top-to-bottom.

## Top View of BT

### Key Idea
Exactly the same as the Bottom View, but instead of overwriting the map, only insert into the map if the `hd` is not already present. This ensures only the first node seen at any horizontal distance (the top-most one) is recorded.

### Pattern
Tree Traversal (BFS with Horizontal Distance)

### Complexity
Time: O(N log N) (or O(N) if tracking min/max bounds)
Space: O(N)

### Revision Note
Like Bottom View, BFS is essential to guarantee that the first time you see a horizontal distance, it is truly the highest node at that vertical line.
