# Day 22

## Implement Max Heap

### Key Idea
A Max Heap can be represented as an array where the parent is at index `(i-1)//2` and children are at `2i+1` and `2i+2`. Insertion adds to the end and "sifts up". Extraction replaces the root with the last element and "sifts down".

### Pattern
Data Structure Design (Complete Binary Tree)

### Complexity
Time: O(log N) for insert and extract_max
Space: O(N) for the underlying array

### Revision Note
Always verify heap bounds (`left < len(self.heap)`) during the `_sift_down` operation to avoid index out of bounds errors.

## K-th Largest Element in an Array

### Key Idea
Maintain a Min Heap of size `K`. As you iterate through the array, push elements into the heap. If the heap size exceeds `K`, pop the smallest element. The remaining `K` elements are the largest seen so far, and the root of the Min Heap is the K-th largest.

### Pattern
Min Heap Tracking Top-K

### Complexity
Time: O(N log K)
Space: O(K)

### Revision Note
Using a Min Heap of size K is more space-efficient than throwing all elements into a Max Heap (which takes O(N) space).

## Maximum Sum Combination

### Key Idea
Sort both arrays descending. Push the sum of the largest elements `(A[0]+B[0])` into a Max Heap along with their indices `(0, 0)`. Pop the maximum, and then push the next two possible largest combinations: `(i+1, j)` and `(i, j+1)`. Use a `set` to avoid processing the same index pair twice.

### Pattern
Max Heap + Visited Set (BFS style expansion)

### Complexity
Time: O(N log N + C log C)
Space: O(C) for the heap and visited set

### Revision Note
In Python, `heapq` implements a Min Heap. To simulate a Max Heap, push the negated sum `-(A[i] + B[j])` and negate it again when popping.

## Day Takeaway
Heaps are the ultimate tool for "Top K" or "K-th Extremum" problems. Whether maintaining a sliding window of the top K items using a Min Heap or exploring combinations optimally with a Max Heap, they drastically reduce the time complexity compared to full sorting.
