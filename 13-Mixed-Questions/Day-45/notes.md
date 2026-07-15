# Day 45

## Distinct Numbers in Each Subarray

### Key Idea
Use a sliding window of size `B` and a hash map (or frequency array) to keep track of the count of elements currently in the window. As the window slides to the right, decrement the frequency of the element leaving the window (and decrement the distinct count if its frequency hits 0) and increment the frequency of the new element entering the window (and increment the distinct count if its frequency was 0).

### Pattern
Sliding Window + Hash Map

### Complexity
Time: O(N)
Space: O(B) for the frequency map.

### Revision Note
This approach avoids creating a new set for every subarray, bringing the time complexity down from O(N * B) to a highly optimal O(N).

## K-th largest element in an unsorted array

### Key Idea
Maintain a min-heap of size exactly `K`. Iterate through the array, pushing each element into the heap. If the heap size exceeds `K`, pop the smallest element. After iterating through the entire array, the top of the min-heap (the smallest element among the largest K elements) will be the K-th largest element overall.

### Pattern
Priority Queue (Min-Heap) / QuickSelect

### Complexity
Time: O(N log K)
Space: O(K)

### Revision Note
QuickSelect (Hoare's selection algorithm) can do this in O(N) average time, but the min-heap approach is extremely concise and has a guaranteed worst-case time complexity, making it heavily preferred in many coding interviews unless O(N) is strictly demanded.

## Flood-fill Algorithm

### Key Idea
This is a classic Graph Traversal problem (DFS or BFS on a 2D grid). Start at the given pixel `(sr, sc)`. If its color is already the target `color`, do nothing. Otherwise, record its original color, change it to the target color, and recursively apply the same process to its 4-directionally adjacent neighbors if they share the original color.

### Pattern
Graph Traversal (DFS/BFS in 2D Grid)

### Complexity
Time: O(M * N) where M is rows and N is cols.
Space: O(M * N) for the recursion stack in the worst case where all pixels are filled.

### Revision Note
The check `if original_color == color: return image` is absolutely crucial. Without it, the DFS would enter an infinite loop because the pixels would never stop matching the original color check.
