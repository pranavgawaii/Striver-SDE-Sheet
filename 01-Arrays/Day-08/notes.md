# Day 8

## Largest Subarray with K Sum

### Key Idea
Maintain a running prefix sum and track the earliest index at which each sum is seen to find the maximum distance for a target diff `current_sum - k`.

### Pattern
Prefix Sum hash map lookup

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
Only store prefix sum index values on their first occurrence to maximize the length of the matching subarray.

## Count Subarrays with XOR K

### Key Idea
Use a hash map to store the frequencies of prefix XOR values, calculating the number of subarrays ending at the current index that satisfy the XOR requirement.

### Pattern
Prefix XOR frequency hash map

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
The math relation `current_xor ^ target = B` translates to searching for `target = current_xor ^ B` in the frequency map.

## Longest Substring Without Repeating Characters

### Key Idea
Use a sliding window where the right boundary advances characters and the left boundary slides forward past any repeating characters using a map.

### Pattern
Sliding Window / Hash Map lookup

### Complexity
Time: O(N)
Space: O(min(N, S)) where S is the size of the alphabet

### Revision Note
Update the left boundary to `char_map[char] + 1` only if the duplicate character falls inside the active window.

## Day Takeaway
Sliding windows and prefix frequency mapping optimize dynamic subarray constraints from quadratic to linear time bounds.
