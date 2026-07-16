# Day 46

## Clone Graph

### Key Idea
Use a hash map to keep track of the original nodes and their corresponding cloned nodes. Traverse the graph using DFS or BFS. When visiting a node, if it's already in the hash map, just return its clone. If not, create a new clone, put it in the hash map, and recursively clone all its neighbors.

### Pattern
Graph Traversal (DFS/BFS) with Hash Map

### Complexity
Time: O(V + E) where V is the number of vertices and E is the number of edges.
Space: O(V) for the hash map and recursion stack.

### Revision Note
Storing the cloned node in the hash map *before* recursing into its neighbors is critical to prevent infinite loops when dealing with cycles in the graph.

## DFS of Graph

### Key Idea
Depth First Search uses a `visited` array to keep track of visited nodes to avoid cycles. Start at the source node, mark it as visited, add it to the result, and recursively call DFS on all its unvisited neighbors.

### Pattern
Graph Traversal (DFS)

### Complexity
Time: O(V + E)
Space: O(V) for the visited array and recursion stack.

### Revision Note
In Python, using a nested `dfs` helper function simplifies passing the `visited` array and `result` array around, keeping the code clean.

## BFS of Graph (Traversal Techniques)

### Key Idea
Breadth First Search uses a Queue to explore the graph level by level. Push the starting node to the queue and mark it visited. While the queue is not empty, pop the front node, add it to the result, and push all its unvisited neighbors to the queue, marking them visited immediately.

### Pattern
Graph Traversal (BFS)

### Complexity
Time: O(V + E)
Space: O(V) for the queue and visited array.

### Revision Note
Always mark a node as visited the moment it is pushed onto the queue, *not* when it is popped off. This prevents duplicate nodes from being added to the queue if multiple paths lead to the same unvisited node.
