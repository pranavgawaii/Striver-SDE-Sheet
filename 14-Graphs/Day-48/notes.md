# Day 48

## Detect Cycle in a Directed Graph (BFS)

### Key Idea
We use Kahn's Algorithm (BFS-based Topological Sort). A valid topological sort is only possible for a Directed Acyclic Graph (DAG). If we attempt to generate a topological sort and the number of nodes processed is less than the total number of vertices `V`, it implies that there is a cycle because nodes in a cycle will never have their in-degree reach zero.

### Pattern
Graph Traversal (Kahn's Algorithm / BFS)

### Complexity
Time: O(V + E)
Space: O(V) for the queue and in-degree array.

### Revision Note
Tracking the `count` of processed nodes is a brilliant and simple way to detect cycles without needing recursion or complex `path_visited` arrays.

## Topological Sort (BFS)

### Key Idea
Also known as Kahn's Algorithm. First, calculate the in-degree (number of incoming edges) for all vertices. Push all vertices with an in-degree of 0 into a queue. While the queue is not empty, pop a node, add it to the result, and reduce the in-degree of all its neighbors by 1. If any neighbor's in-degree becomes 0, push it into the queue.

### Pattern
Graph Traversal (Kahn's Algorithm / BFS)

### Complexity
Time: O(V + E)
Space: O(V)

### Revision Note
Nodes with an in-degree of 0 have no dependencies, so they can be processed first. This mirrors resolving dependency trees in real life (e.g., package managers, task scheduling).

## Topological Sort (DFS)

### Key Idea
Perform a standard DFS. After fully exploring all the neighbors of a node (i.e., just before the DFS function returns), push that node onto a stack. Once the DFS is complete for all components, pop everything from the stack to get the topological order.

### Pattern
Graph Traversal (DFS with Stack)

### Complexity
Time: O(V + E)
Space: O(V) for the stack, visited array, and recursion stack.

### Revision Note
The stack naturally reverses the post-order traversal. In Python, appending to a list and then calling `stack.reverse()` (or returning `stack[::-1]`) is equivalent to using an explicit stack structure.
