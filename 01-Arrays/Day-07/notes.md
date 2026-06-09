# Day 7

## Two Sum

### Key Idea
Search for the target complement of the current element in a hash map of previously seen values, returning their index values when located.

### Pattern
Complement lookup / Hash Map

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
Store the element value as the key and its index value as the hash map value to retrieve coordinates.

## Four Sum

### Key Idea
Sort the array and run double nested loops, utilizing a two-pointer scan inside the inner loop to find unique quadruplets that sum to target.

### Pattern
Sorting, nested loops, and two-pointer traversal

### Complexity
Time: O(N^3)
Space: O(1) auxiliary space

### Revision Note
Ensure duplication checks (`if val == prev_val`) are implemented inside loops and two-pointer steps to avoid matching identical index duplicates.

## Longest Consecutive Sequence

### Key Idea
Insert all values into a hash set, and for elements that represent the start of a sequence (no preceding element in set), count the length of the sequence.

### Pattern
Set-based sequence scanning

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
Only begin counting streaks when `num - 1` is absent from the set to guarantee each element is visited at most twice.

## Day Takeaway
Using hash sets and hash maps reduces polynomial time complexities down to linear boundaries at the expense of linear auxiliary memory.
