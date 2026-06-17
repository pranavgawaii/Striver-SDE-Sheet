# Day 17

## Combination Sum

### Key Idea
Use backtracking to explore two choices for each candidate: either pick the current candidate (and stay at the same index, since we can reuse it) or don't pick it (and move to the next index).

### Pattern
Backtracking (Pick / Don't Pick)

### Complexity
Time: O(2^T) where T is the target value
Space: O(T / min(candidates)) for the recursion stack

### Revision Note
Since elements can be reused, when making the recursive call to include the element, do not increment the index.

## Combination Sum II

### Key Idea
Sort the array first to bring duplicates together. Use backtracking and skip duplicates at the same level (`i > index and candidates[i] == candidates[i - 1]`) to avoid generating duplicate combinations.

### Pattern
Backtracking (Combinations with Duplicates)

### Complexity
Time: O(2^N)
Space: O(N)

### Revision Note
Unlike Combination Sum, elements cannot be reused, so the recursive call must always increment the index (`i + 1`).

## Palindrome Partitioning

### Key Idea
Iterate over all possible prefixes of the remaining string. If a prefix is a palindrome, add it to the current partition and recursively partition the rest of the string.

### Pattern
Backtracking (Partitioning)

### Complexity
Time: O(N * 2^N)
Space: O(N)

### Revision Note
A helper function to check if a string is a palindrome (`s == s[::-1]`) keeps the logic clean. The base case is when the start index reaches the end of the string.

## Permutation Sequence

### Key Idea
Instead of generating all permutations, mathematically calculate which number should be at each position using factorials. There are `(n-1)!` permutations starting with each available number.

### Pattern
Math / Factorial Block Grouping

### Complexity
Time: O(N^2) (due to list popping)
Space: O(N)

### Revision Note
Always convert the target `k` to 0-indexed (`k -= 1`) before performing integer division and modulo operations.

## Day Takeaway
Backtracking provides a systematic way to explore combinations and partitions, but for specific sequence problems (like Permutation Sequence), mathematical patterns can bypass exhaustive generation entirely.
