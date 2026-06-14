# Day 14

## Trapping Rainwater

### Key Idea
Use two pointers, `left` and `right`. Maintain the maximum height seen from the left (`left_max`) and right (`right_max`). The amount of water trapped at a given position is determined by the minimum of the two maximums minus the current height. By moving the pointer with the smaller maximum, we can calculate the trapped water safely.

### Pattern
Two Pointers

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Always update the pointer which points to the smaller maximum (`left_max` or `right_max`) because the smaller maximum is the bottleneck for trapping water.

## Remove Duplicates from Sorted Array

### Key Idea
Use two pointers: one (`i`) to keep track of the position of the last unique element, and another (`j`) to iterate through the array. When a new unique element is found, increment `i` and copy the element to `nums[i]`.

### Pattern
Two Pointers (Fast and Slow)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
This problem requires modifying the array in-place and returning the new length. The elements after the new length don't matter.

## Maximum Consecutive Ones

### Key Idea
Iterate through the array. Keep a running count of consecutive ones. If a zero is encountered, reset the count. Update the maximum count seen so far continuously.

### Pattern
Linear Scan / Counting

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Reset the counter to 0 whenever a `0` is encountered, and ensure the maximum is updated when counting `1`s.

## Day Takeaway
Two-pointer techniques are versatile for array traversal problems, especially when comparing elements (like removing duplicates) or computing aggregates bound by extremes (like trapping rainwater).
