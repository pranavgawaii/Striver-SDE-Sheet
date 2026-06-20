# Day 20

## The N-th root of an integer

### Key Idea
Use binary search on the answer range `[1, M]`. For a chosen `mid`, calculate `mid^N`. If it equals `M`, return `mid`. If it's less, search right; if greater, search left.

### Pattern
Binary Search on Answer Space

### Complexity
Time: O(log M * log N) (assuming exponentiation takes log N time)
Space: O(1)

### Revision Note
Python handles arbitrarily large integers, making direct exponentiation safe. In other languages, you must be careful about integer overflow and break the exponentiation loop early if the product exceeds `M`.

## Matrix Median

### Key Idea
Find the global min and max in the matrix. Use binary search on this range. For a `mid` value, count how many numbers in the matrix are less than or equal to `mid` using `upper_bound` (binary search) on each row. The true median is the smallest number where this count is greater than `(R*C)/2`.

### Pattern
Binary Search on Answer Space + Binary Search on Arrays

### Complexity
Time: O(R * log C * log(max-min))
Space: O(1)

### Revision Note
The requirement `count <= req` moving `low = mid + 1` correctly ensures that when the loop terminates, `low` points to the exact median element present in the matrix.

## Single Element in Sorted Array

### Key Idea
Every element appears twice except one. In the array, pairs before the single element occur at indices `(even, odd)`. Pairs after the single element occur at indices `(odd, even)`. We can use binary search to find this disruption point.

### Pattern
Binary Search (Index Parity Check)

### Complexity
Time: O(log N)
Space: O(1)

### Revision Note
Handling edge cases first (like the single element being at the very beginning or end) simplifies the bounds of the binary search to `low = 1` and `high = n - 2`.

## Search Element in a Sorted and Rotated Array

### Key Idea
In any rotated sorted array, dividing it by `mid` guarantees that at least one half (either left to mid, or mid to right) is completely sorted. Identify the sorted half, check if the target falls within its range, and eliminate half the search space accordingly.

### Pattern
Binary Search (Rotated Array)

### Complexity
Time: O(log N)
Space: O(1)

### Revision Note
The condition `nums[low] <= nums[mid]` checks if the left half is the sorted one. If true, verify if the target is between `nums[low]` and `nums[mid]`.

## Day Takeaway
Binary search is not just for finding elements in sorted arrays; it is a powerful technique for optimizing monotonic search spaces (Binary Search on Answer) and identifying inflection points.
