# Day 4

## Find Duplicate Number

### Key Idea
Treat the array values as pointers to form a linked list and use cycle detection to find the duplicate node at the start of the cycle.

### Pattern
Floyd's Cycle Detection (Tortoise and Hare)

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
First find the intersection point inside the cycle, then reset one pointer to index 0 and move both one step at a time to find the start.

## Find Repeating and Missing Number

### Key Idea
Set up mathematical equations comparing actual and expected sums of values and their squares to solve for the missing and repeating elements.

### Pattern
Algebraic equation solving / Math

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Compute diff of sums (X - Y) and diff of squared sums (X^2 - Y^2) to derive the sum (X + Y).

## Inversion Count

### Key Idea
Utilize a divide-and-conquer strategy similar to merge sort, counting elements in the right partition that are smaller than elements in the left partition during the merge step.

### Pattern
Divide and conquer (Merge Sort variation)

### Complexity
Time: O(N log N)
Space: O(N)

### Revision Note
Add `(mid - i + 1)` to the inversion count when elements from the right subarray are merged before elements from the left subarray.

## Day Takeaway
Solving index-based challenges efficiently often involves mapping array values directly to address pointers or modeling them mathematically.
