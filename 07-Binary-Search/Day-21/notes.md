# Day 21

## Median of 2 Sorted Arrays

### Key Idea
Instead of merging, use binary search to partition the smaller array. The partition of the larger array is determined automatically because the total elements on the left side of both partitions must equal half the total elements. Check the boundary conditions across the partition.

### Pattern
Binary Search (Partitioning two arrays)

### Complexity
Time: O(log(min(N, M)))
Space: O(1)

### Revision Note
Always ensure you run binary search on the smaller array to minimize the search space. Use infinity and negative infinity to handle edge cases where a partition falls at the very beginning or end of an array.

## Kth Element of 2 Sorted Arrays

### Key Idea
Similar to the median problem, but the total elements on the left side should equal `K`. Binary search for the partition in the smaller array, ensuring the partition bounds are valid `[max(0, k-m), min(k, n)]`.

### Pattern
Binary Search (Partitioning two arrays)

### Complexity
Time: O(log(min(N, M)))
Space: O(1)

### Revision Note
The lower bound of the binary search `max(0, k-m)` ensures that if `k` is larger than the size of the second array, we *must* take some elements from the first array.

## Allocate Minimum Number of Pages

### Key Idea
The minimum possible maximum pages is the largest single book (`max(A)`). The maximum possible is if one student reads all books (`sum(A)`). Binary search this range `[max, sum]`. For a candidate value `mid`, check if books can be allocated such that no student exceeds `mid` pages and the number of students required is `<= M`.

### Pattern
Binary Search on Answer Space (Minimax)

### Complexity
Time: O(N log(sum - max))
Space: O(1)

### Revision Note
If the number of students `M` is greater than the number of books `N`, it's impossible to allocate at least one book to each student, so return `-1`.

## Aggressive Cows

### Key Idea
Sort the stalls first. The minimum possible distance between cows is 1, and the maximum is `stalls[-1] - stalls[0]`. Binary search this distance range. For a distance `mid`, greedily place cows in stalls ensuring the gap is at least `mid`. If you can place all `K` cows, `mid` is possible; try for a larger distance.

### Pattern
Binary Search on Answer Space (Maximin)

### Complexity
Time: O(N log N + N log(max_dist))
Space: O(1)

### Revision Note
Aggressive Cows is the classic "Maximize the Minimum" problem. The greedy verification step `canPlaceCows` works because placing a cow as early as possible maximizes the remaining space for subsequent cows.

## Day Takeaway
Binary Search on the answer space is the go-to technique for optimization problems involving "minimize the maximum" or "maximize the minimum", as the answer space is always monotonic.
