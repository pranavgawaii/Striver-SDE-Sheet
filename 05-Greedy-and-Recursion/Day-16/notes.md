# Day 16

## Minimum Coins

### Key Idea
Start from the largest denomination coin. Keep subtracting its value from the target amount and increment the coin count until the remaining amount is strictly less than the coin's value. Repeat for smaller coins.

### Pattern
Greedy Algorithm

### Complexity
Time: O(N) where N is the number of coin denominations
Space: O(1)

### Revision Note
This greedy approach works optimally for the standard Indian/US coin systems but might fail for arbitrary coin systems (which would require DP).

## Assign Cookies

### Key Idea
Sort both the greed factors of the children and the sizes of the cookies. Use two pointers to iterate through both arrays. If the current cookie can satisfy the current child, move both pointers. Otherwise, try the next cookie.

### Pattern
Greedy Algorithm / Two Pointers

### Complexity
Time: O(N log N + M log M)
Space: O(1)

### Revision Note
Sorting is crucial here to ensure we satisfy children with the minimum possible cookie size, saving larger cookies for greedier children.

## Subset Sums

### Key Idea
Use recursion to explore both possibilities for each element: either include it in the current subset sum or exclude it. Add the accumulated sum to the result list when the end of the array is reached.

### Pattern
Recursion (Pick and Don't Pick)

### Complexity
Time: O(2^N)
Space: O(2^N) for storing the sums

### Revision Note
The final output is often expected to be sorted, so make sure to sort the resulting sums array before returning.

## Subsets II

### Key Idea
Sort the array first. Use backtracking to generate subsets. To handle duplicates, skip elements that are identical to the previous element in the current recursive step (i.e., when `i > index`).

### Pattern
Backtracking (Combinations with Duplicates)

### Complexity
Time: O(2^N * N)
Space: O(N) recursion stack and subset storage

### Revision Note
Sorting is mandatory to bring duplicates together. Skipping `nums[i] == nums[i - 1]` prevents generating the same subset in the same recursion level.

## Day Takeaway
Combining Greedy algorithms and Recursion/Backtracking highlights the difference between making locally optimal choices (Greedy) versus exploring all possible combinations systematically (Recursion).
