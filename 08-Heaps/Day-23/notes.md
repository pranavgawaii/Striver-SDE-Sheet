# Day 23

## Find Median from Data Stream

### Key Idea
Maintain two heaps: a Max Heap for the lower half of the numbers, and a Min Heap for the upper half. Keep them balanced such that the Max Heap has at most one more element than the Min Heap. The median is either the root of the Max Heap (if odd total elements) or the average of the roots of both heaps (if even).

### Pattern
Two Heaps (Running Median)

### Complexity
Time: O(log N) for `addNum`, O(1) for `findMedian`
Space: O(N)

### Revision Note
In Python, simulate the Max Heap by negating the numbers before pushing and after popping from `heapq` (which is inherently a Min Heap).

## Merge K Sorted Arrays

### Key Idea
Insert the first element of all `K` arrays into a Min Heap, storing the element's value, its source array index, and its element index within that array. Repeatedly pop the minimum element from the heap and add it to the result. Then, push the next element from the same source array into the heap.

### Pattern
K-Way Merge (Min Heap)

### Complexity
Time: O(N * K log K) where N*K is the total number of elements across all arrays.
Space: O(K) for the heap

### Revision Note
Keeping track of `array_idx` and `element_idx` alongside the value in the heap tuple `(val, array_idx, element_idx)` is the standard way to merge multiple streams without loading everything into memory at once.

## Top K Frequent Elements

### Key Idea
Count the frequencies of all elements using a Hash Map (or `Counter`). Iterate through the map, pushing `(frequency, element)` pairs into a Min Heap of size `K`. If the heap size exceeds `K`, pop the smallest frequency. The remaining elements in the heap are the top `K` most frequent.

### Pattern
Hash Map + Min Heap

### Complexity
Time: O(N log K)
Space: O(N) for the Hash Map and O(K) for the Min Heap

### Revision Note
Alternatively, you can use Bucket Sort (where index is frequency and value is a list of elements) to solve this in O(N) time, but the Min Heap approach is more generic and useful when the frequency counts can be very sparse or when data is streaming.

## Day Takeaway
Heaps excel at maintaining partial order (Top K, Min/Max) over dynamic data streams or merging multiple sorted sequences efficiently.
