# Day 2

## Kadane's Algorithm

### Key Idea
Iterate through the array keeping a running sum of the current subarray, resetting it to 0 if it drops below zero, while updating the maximum sum found.

### Pattern
Greedy running sum

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Ensure max_sum is initialized to the first element to handle arrays containing exclusively negative numbers.

## Sort 0s 1s 2s

### Key Idea
Use three pointers (low, mid, high) to partition the array in-place, swapping 0s to the left and 2s to the right.

### Pattern
Three-way partitioning (Dutch National Flag)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Only increment the mid pointer when swapping 0s or processing 1s; do not increment when swapping 2s.

## Stock Buy and Sell

### Key Idea
Keep track of the minimum price seen so far and calculate potential profit on each step, updating the maximum profit.

### Pattern
Single-pass prefix minimum tracking

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Initialize min_price to infinity and update min_price before calculating max_profit.

## Day Takeaway
Subarray and sorting partition boundaries are handled optimally in linear time by maintaining running state variables or multiple pointers.
