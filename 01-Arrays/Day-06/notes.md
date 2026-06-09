# Day 6

## Majority Element II

### Key Idea
Find elements appearing more than floor(N/3) times by keeping up to two majority candidates and their respective vote weights.

### Pattern
Extended Boyer-Moore Voting Algorithm

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Always verify the counts of the two candidates in a second pass since the voting step only yields potential candidates.

## Grid Unique Paths

### Key Idea
Formulate the movement from top-left to bottom-right as choosing which steps to move down out of the total steps, using combinations.

### Pattern
Combinatorics (Combinations)

### Complexity
Time: O(min(M, N))
Space: O(1)

### Revision Note
The result is given by combinations C(M + N - 2, M - 1). Optimize computing steps to avoid overflow.

## Reverse Pairs

### Key Idea
Count index pairs (i, j) where i < j and nums[i] > 2 * nums[j] using a split-and-merge process, checking criteria before standard merge sorting.

### Pattern
Divide and conquer (Merge Sort variation)

### Complexity
Time: O(N log N)
Space: O(N)

### Revision Note
Use a two-pointer pass inside the merge step to count matching pairs linearly before merging the arrays.

## Day Takeaway
Advanced search partitions and combinatorial math solve complex multi-candidate voting and coordinate pathing without using dynamic programming arrays.
