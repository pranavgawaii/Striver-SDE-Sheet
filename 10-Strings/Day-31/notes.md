# Day 31

## Z Function

### Key Idea
The Z-array `Z[i]` stores the length of the longest substring starting from `s[i]` which is also a prefix of `s`. Concatenate the pattern and text with a separator (`pattern + "$" + text`). Compute the Z-array. Any index `i` after the separator where `Z[i] == len(pattern)` indicates a match.

### Pattern
String Matching (Z-Algorithm)

### Complexity
Time: O(N + M)
Space: O(N + M)

### Revision Note
Maintaining a `[L, R]` window representing the rightmost matching prefix block reduces the number of character comparisons significantly, yielding linear time.

## KMP Algorithm (LPS array)

### Key Idea
Compute the Longest Proper Prefix which is also Suffix (LPS) array for the pattern. `LPS[i]` tells us how many characters to skip when a mismatch occurs at `i`. When traversing the text, if characters match, move both pointers. If a mismatch occurs, use the LPS array to backtrack the pattern pointer without rewinding the text pointer.

### Pattern
String Matching (KMP)

### Complexity
Time: O(N + M)
Space: O(M) for the LPS array

### Revision Note
The core logic `prev_lps = lps[prev_lps - 1]` allows the algorithm to gracefully fall back to shorter prefix matches instead of restarting from index 0.

## Minimum Insertions to Make String Palindrome

### Key Idea
The minimum number of insertions required to make a string a palindrome is exactly the string's length minus the length of its Longest Palindromic Subsequence (LPS). The LPS of a string can be found by finding the Longest Common Subsequence (LCS) of the string and its reverse.

### Pattern
Dynamic Programming (LCS adaptation)

### Complexity
Time: O(N^2)
Space: O(N) optimized from O(N^2) by using two 1D arrays

### Revision Note
`min_insertions = len(s) - LCS(s, reverse(s))` is a beautiful and highly reusable mathematical relationship for palindrome problems.

## Day Takeaway
Advanced string matching relies heavily on pre-computing arrays (like Z-array or LPS-array) to skip redundant comparisons. Palindrome DP problems often boil down to LCS on a string and its reverse.
