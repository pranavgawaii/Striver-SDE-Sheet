# Day 47

## Detect A cycle in Undirected Graph using BFS

### Key Idea
When traversing a graph with BFS, keep track of the `parent` node that led to the current node (using a tuple `(current_node, parent_node)` in the queue). If you encounter a neighbor that is already visited, and that neighbor is *not* the parent, it means you've found an alternative path to a previously visited node, which forms a cycle.

### Pattern
Graph Traversal (BFS with Parent Tracking)

### Complexity
Time: O(V + E)
Space: O(V) for the queue and visited array.

### Revision Note
Remember to loop through all `V` vertices initially to handle disconnected components. If a component is entirely disconnected from the start node, it wouldn't be checked otherwise.

## Detect A cycle in Undirected Graph using DFS

### Key Idea
The logic is identical to BFS, but implemented using the call stack. Pass the `parent` node as an argument to the recursive DFS function. If a neighbor is already visited and is not the parent, a cycle is detected.

### Pattern
Graph Traversal (DFS with Parent Tracking)

### Complexity
Time: O(V + E)
Space: O(V) for the recursion stack and visited array.

### Revision Note
DFS is often slightly faster to write and execute (due to avoiding queue overhead), but risks `RecursionError` on extremely deep/long graphs in Python.

## Detect A cycle in a Directed Graph using DFS

### Key Idea
In a *directed* graph, just hitting a previously visited node does *not* mean there is a cycle (it could just be two different paths merging). A cycle only exists if you encounter a node that is currently in the same DFS path (i.e., currently on the recursion stack). We use a `visited` array to avoid re-processing nodes globally, and a `path_visited` array to track nodes currently in the recursive call stack.

### Pattern
Graph Traversal (DFS with Path Tracking)

### Complexity
Time: O(V + E)
Space: O(V) for the visited arrays and recursion stack.

### Revision Note
Be absolutely sure to backtrack `path_visited[node] = False` at the end of the DFS function before returning `False`. This indicates the node is completely processed and is removed from the current DFS path.
