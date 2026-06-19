# Day 19

## M Coloring Problem

### Key Idea
Use backtracking to try assigning each of the `M` colors to the nodes one by one. For each node, check if placing a specific color is safe (i.e., no adjacent node has the same color). If safe, recursively color the remaining nodes.

### Pattern
Backtracking (Graph Coloring)

### Complexity
Time: O(M^V) where V is the number of vertices and M is the number of colors
Space: O(V) for the color array and recursion stack

### Revision Note
A helper function `is_safe` is critical here to check the adjacency matrix and ensure no conflicts before recursing.

## Rat in a Maze

### Key Idea
Explore the maze starting from `(0,0)`. Try all four possible directions (Down, Left, Right, Up). If a move is valid (within bounds, not visited, and not a blocked cell), mark it visited, record the direction, and recurse. Backtrack by unmarking the cell.

### Pattern
Backtracking (2D Grid / DFS)

### Complexity
Time: O(4^(N*N))
Space: O(N*N) for the visited array and recursion stack

### Revision Note
Using direction arrays `di` and `dj` along with a corresponding characters array makes iterating over the 4 possible moves much cleaner than writing 4 separate `if` blocks.

## Word Break (Print all ways)

### Key Idea
Iterate through the string, extracting prefixes. If a prefix exists in the dictionary, add it to the current sentence state and recursively break the rest of the string.

### Pattern
Backtracking (String Partitioning)

### Complexity
Time: O(2^N) in the worst case (e.g., dictionary has all single letter words)
Space: O(N)

### Revision Note
Converting the list of dictionary words to a `set` allows O(1) lookups during the backtracking, significantly improving practical execution time.

## Day Takeaway
Backtracking effectively handles multi-dimensional search spaces (grids, graphs, string partitions) by systematically exploring choices and undoing them when a path is exhausted.
