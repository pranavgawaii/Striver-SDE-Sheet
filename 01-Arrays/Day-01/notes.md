# Day 1

## Set Matrix Zeroes

### Key Idea
Use the first row and first column of the matrix as marker trackers to record zero occurrences, with two auxiliary flags for the first row/column boundaries.

### Pattern
In-place matrix marking

### Complexity
Time: O(M * N)
Space: O(1)

### Revision Note
Update the inner matrix first using indices row/column 1 to M-1/N-1, then update row 0 and column 0.

## Pascal's Triangle

### Key Idea
Construct rows sequentially, where each element is the sum of the two elements directly above it from the previous row.

### Pattern
Iterative tabulation (Dynamic Programming)

### Complexity
Time: O(N^2)
Space: O(N^2)

### Revision Note
Pre-fill each row with 1s and only compute elements between the first and last columns.

## Next Permutation

### Key Idea
Locate the first decreasing element from the right (pivot), swap it with the next larger suffix element, then reverse the suffix in-place.

### Pattern
Single-pass suffix permutation scanning

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Search right-to-left for the pivot index `i`, find the swap target, swap, and reverse all elements to the right of `i`.

## Day Takeaway
Achieving optimal space complexity in arrays and matrices requires utilizing in-place swaps or reusing existing rows/columns as marker buffers.
