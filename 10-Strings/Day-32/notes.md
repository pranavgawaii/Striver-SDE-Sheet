# Day 32

## Valid Anagram

### Key Idea
Two strings are anagrams if they contain the exact same frequencies of characters. This can be checked by building a frequency map for both strings and comparing them.

### Pattern
Hash Map (Frequency Counting)

### Complexity
Time: O(N)
Space: O(1) assuming the character set is fixed (e.g., lowercase English letters).

### Revision Note
In Python, `collections.Counter(s) == collections.Counter(t)` is the most idiomatic and readable way to solve this.

## Count and Say

### Key Idea
This is a recursive sequence generation problem. To find the `N`th term, find the `(N-1)`th term. Then iterate through the `(N-1)`th term, counting identical adjacent characters. When a different character is found, append the count followed by the character to the result string.

### Pattern
Recursion + String Parsing

### Complexity
Time: O(2^N) approximately, as the length of the string grows exponentially.
Space: O(2^N) for storing the strings in the call stack.

### Revision Note
Using a list to accumulate the characters and then `"".join()` at the end is much faster in Python than repeatedly concatenating strings with `+`.

## Compare Version Numbers

### Key Idea
Split both version strings by the dot `.` character. Iterate up to the maximum length of the two resulting arrays. If one array is shorter, treat its missing parts as `0`. Compare the integer representations of the corresponding parts from left to right.

### Pattern
String Parsing (Split)

### Complexity
Time: O(N + M) where N and M are the lengths of the two strings.
Space: O(N + M) for the split arrays.

### Revision Note
Python's `int()` function automatically handles leading zeros, making `int("001") == 1` work seamlessly without extra parsing logic.

## Day Takeaway
Built-in string and list operations (`split`, `Counter`, `int` conversion) significantly simplify string manipulation problems. When generating strings iteratively, always prefer building a list of characters/substrings over using the `+` operator.
