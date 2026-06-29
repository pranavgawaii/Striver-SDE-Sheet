# Day 29

## Reverse Words in a String

### Key Idea
Split the string by spaces, which automatically handles multiple spaces and trims leading/trailing spaces. Reverse the resulting list of words and join them back together with a single space.

### Pattern
String Manipulation (Built-in functions)

### Complexity
Time: O(N)
Space: O(N) for the split list and the new string.

### Revision Note
In Python, `s.split()` without arguments splits on all whitespace and discards empty strings, making it incredibly robust for this specific problem compared to doing it manually.

## Longest Palindromic Substring

### Key Idea
A palindrome mirrors around its center. There are `2N - 1` possible centers (each character, and between every two characters). For each center, expand outwards as long as the characters match. Keep track of the longest string found.

### Pattern
String Manipulation (Expand Around Center)

### Complexity
Time: O(N^2)
Space: O(1) beyond the output string allocation

### Revision Note
Using a helper function `expand_around_center(left, right)` cleanly handles both odd-length palindromes (where `left == right`) and even-length palindromes (where `right == left + 1`).

## Roman to Integer

### Key Idea
Iterate through the string. Generally, you add the value of the current Roman numeral. However, if the current numeral is strictly less than the next numeral (e.g., `I` before `V`), you subtract its value instead.

### Pattern
String Parsing (Hash Map lookups)

### Complexity
Time: O(N)
Space: O(1) (Hash map is fixed size of 7)

### Revision Note
Always check `i < n - 1` before comparing the current character with the next character to avoid index out of bounds errors.

## Day Takeaway
String problems often benefit significantly from language-specific built-ins (like Python's `split`), but foundational logic like "expand around center" remains universal and optimal for avoiding O(N^3) brute force approaches.
