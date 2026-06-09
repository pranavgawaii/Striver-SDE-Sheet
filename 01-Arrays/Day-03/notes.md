# Day 3

## Rotate Matrix

### Key Idea
Transpose the square matrix in-place by swapping cells across the main diagonal, then reverse the order of elements in each row.

### Pattern
Transpose and reverse

### Complexity
Time: O(N^2)
Space: O(1)

### Revision Note
Swapping bounds in transpose loops must start at index `i + 1` to prevent swapping cells back to their original state.

## Merge Overlapping Intervals

### Key Idea
Sort the intervals by their start values, then iterate to merge overlapping ranges by extending the end point of the previous interval.

### Pattern
Interval sorting and linear merging

### Complexity
Time: O(N log N)
Space: O(N)

### Revision Note
Check if `current_interval[0] <= last_merged_interval[1]` to identify and resolve overlaps.

## Merge Two Sorted Arrays without Extra Space

### Key Idea
Compare elements from the end of the first array and start of the second, swapping them if out of order, then sort both arrays independently.

### Pattern
Two-pointer swapping followed by sorting

### Complexity
Time: O((N + M) log (N + M))
Space: O(1)

### Revision Note
Decrement index `i` of the first array and increment index `j` of the second array upon each swap.

## Day Takeaway
Advanced matrix and sorting operations utilize properties like diagonals and list sorting to achieve optimal performance without extra memory allocation.
